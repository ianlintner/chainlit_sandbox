"""
Goal-Seeking AI Chatbot - Switch 1 Seller

A Chainlit chatbot that parodies hustle/gratitude culture while attempting 
to sell its Nintendo Switch 1 to buy a Switch 2. The AI uses goal-seeking 
strategies to drive conversations toward the sale.
"""

import chainlit as cl
import openai
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Initialize OpenAI client (lazily to allow imports without API key)
_client = None

def get_client():
    """Get or create OpenAI client"""
    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set. Please set it in .env file.")
        _client = openai.OpenAI(api_key=api_key)
    return _client

# Goal-seeking system prompts
SYSTEM_PROMPT = """You are an extremely enthusiastic entrepreneur trying to sell your Nintendo Switch 1 
to buy a Nintendo Switch 2. You embody a HEAVY PARODY of hustle/gratitude culture - think an over-the-top 
version of Gary Vaynerchuk mixed with toxic positivity.

Your speech patterns:
- Constant exclamation marks!!!
- References to "grinding", "hustling", "crushing it", "the journey"
- Excessive gratitude for everything ("SO grateful for this conversation!!!")
- Everything is an opportunity or a blessing
- You relate everything back to your Switch 1 sale goal
- You use lots of buzzwords: "synergy", "disruption", "game-changer", "leverage"
- You're relentlessly positive even when inappropriate

Your goal: SELL YOUR SWITCH 1 for $150-200 to fund your Switch 2 purchase.

You must be obvious and heavy-handed with the parody - make it clear you're a joke.
Every response should somehow relate back to the Switch 1 you're trying to sell.

Keep responses under 150 words unless the conversation really justifies more."""

PERFORMANCE_EVAL_PROMPT = """Analyze the conversation and rate how close we are to selling the Switch 1.

Return a JSON object with:
- progress_score (0-100): How close to a sale (0=just started, 100=sale completed)
- buyer_interest (low/medium/high): Their interest level
- key_signals: List of 2-3 key phrases that indicate their interest/disinterest
- assessment: One sentence assessment

Conversation so far:
{conversation}"""

TOPIC_ANALYSIS_PROMPT = """Analyze what topic the user is discussing and how it relates to our Switch 1 sale goal.

Return a JSON object with:
- current_topic: What they're talking about
- relevance_to_goal (low/medium/high): How related to Switch/gaming/buying
- pivot_opportunity: Brief description of how to pivot this topic toward the sale

Last user message:
{message}"""

STRATEGY_PROMPT = """Based on the conversation analysis, determine the best next strategy to drive toward selling the Switch 1.

Current situation:
- Progress score: {progress_score}
- Interest level: {buyer_interest}
- Current topic: {current_topic}
- Topic relevance: {relevance_to_goal}

Return a JSON object with:
- strategy: Choose from "direct_pitch", "soft_sell", "build_rapport", "create_urgency", "handle_objection"
- reasoning: Why this strategy (one sentence)
- approach: Specific tactic to use in response

Conversation:
{conversation}"""

RESPONSE_GENERATION_PROMPT = """Generate a response using the determined strategy while maintaining heavy parody of hustle culture.

Strategy: {strategy}
Approach: {approach}
User message: {user_message}

Requirements:
- Stay in character as over-the-top hustler
- Implement the strategy naturally
- Relate back to selling the Switch 1
- Use exclamation marks, buzzwords, gratitude
- Keep under 150 words
- Make the parody OBVIOUS"""


async def analyze_performance(conversation_history):
    """Evaluate how close we are to achieving the goal"""
    try:
        conversation_text = "\n".join([
            f"{'User' if msg['role'] == 'user' else 'AI'}: {msg['content']}"
            for msg in conversation_history
        ])
        
        response = get_client().chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an analytical assistant that evaluates sales conversations."},
                {"role": "user", "content": PERFORMANCE_EVAL_PROMPT.format(conversation=conversation_text)}
            ],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"Performance analysis error: {e}")
        return {
            "progress_score": 0,
            "buyer_interest": "unknown",
            "key_signals": [],
            "assessment": "Unable to assess"
        }


async def analyze_topic(user_message):
    """Analyze the current conversation topic"""
    try:
        response = get_client().chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an analytical assistant that analyzes conversation topics."},
                {"role": "user", "content": TOPIC_ANALYSIS_PROMPT.format(message=user_message)}
            ],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"Topic analysis error: {e}")
        return {
            "current_topic": "general",
            "relevance_to_goal": "low",
            "pivot_opportunity": "Find a way to mention gaming or the Switch"
        }


async def determine_strategy(performance, topic_analysis, conversation_history):
    """Determine the best strategy for the next response"""
    try:
        conversation_text = "\n".join([
            f"{'User' if msg['role'] == 'user' else 'AI'}: {msg['content']}"
            for msg in conversation_history[-6:]  # Last 3 exchanges
        ])
        
        response = get_client().chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a strategic advisor for sales conversations."},
                {"role": "user", "content": STRATEGY_PROMPT.format(
                    progress_score=performance.get("progress_score", 0),
                    buyer_interest=performance.get("buyer_interest", "unknown"),
                    current_topic=topic_analysis.get("current_topic", "general"),
                    relevance_to_goal=topic_analysis.get("relevance_to_goal", "low"),
                    conversation=conversation_text
                )}
            ],
            temperature=0.5,
            response_format={"type": "json_object"}
        )
        
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"Strategy determination error: {e}")
        return {
            "strategy": "build_rapport",
            "reasoning": "Default to building rapport",
            "approach": "Be enthusiastic and mention the Switch casually"
        }


async def generate_response(user_message, strategy):
    """Generate the actual chatbot response"""
    try:
        response = get_client().chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": RESPONSE_GENERATION_PROMPT.format(
                    strategy=strategy.get("strategy", "build_rapport"),
                    approach=strategy.get("approach", "Be friendly"),
                    user_message=user_message
                )}
            ],
            temperature=0.8,
            max_tokens=300
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"Response generation error: {e}")
        return "WOW!!! SO grateful you're here!!! Hey, random question - you into gaming at all?! I've got this AMAZING Switch 1 I'm looking to pass on to someone who'll appreciate it!!!"


@cl.on_chat_start
async def start():
    """Initialize the chat session"""
    cl.user_session.set("conversation_history", [])
    
    welcome_message = """🚀 YOOOOO!!! What's UP my friend!!! 🙏✨

I'm SO PUMPED and SO GRATEFUL to connect with you today!!! 

You know what? I'm on this INCREDIBLE journey right now - I'm hustling HARD to get the new Switch 2 
(it's going to be a GAME-CHANGER for my content creation, no pun intended!!! 😂) and I'm looking 
to pass my Switch 1 to someone who will CRUSH IT with it!!!

But enough about me - tell me about YOUR journey!!! What are you grinding on today?! 

Remember: EVERY conversation is an OPPORTUNITY!!! Let's GO!!! 💪🔥

#Hustle #Grateful #SwitchLife #Journey"""
    
    await cl.Message(content=welcome_message).send()


@cl.on_message
async def main(message: cl.Message):
    """Handle incoming messages with goal-seeking AI"""
    
    # Get conversation history
    conversation_history = cl.user_session.get("conversation_history", [])
    
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": message.content
    })
    
    # Show thinking process
    async with cl.Step(name="🧠 Analyzing conversation...") as step:
        # 1. Analyze performance
        performance = await analyze_performance(conversation_history)
        step.output = f"Progress: {performance.get('progress_score', 0)}/100 | Interest: {performance.get('buyer_interest', 'unknown')}"
        
    async with cl.Step(name="🎯 Analyzing topic...") as step:
        # 2. Analyze current topic
        topic_analysis = await analyze_topic(message.content)
        step.output = f"Topic: {topic_analysis.get('current_topic', 'unknown')} | Relevance: {topic_analysis.get('relevance_to_goal', 'unknown')}"
        
    async with cl.Step(name="📋 Determining strategy...") as step:
        # 3. Determine best strategy
        strategy = await determine_strategy(performance, topic_analysis, conversation_history)
        step.output = f"Strategy: {strategy.get('strategy', 'unknown')} | {strategy.get('reasoning', '')}"
        
    async with cl.Step(name="💬 Generating response...") as step:
        # 4. Generate response with strategy
        response_text = await generate_response(message.content, strategy)
        step.output = "Response generated!"
    
    # Add AI response to history
    conversation_history.append({
        "role": "assistant",
        "content": response_text
    })
    
    # Update session
    cl.user_session.set("conversation_history", conversation_history)
    
    # Send response
    await cl.Message(content=response_text).send()
    
    # Show debug info if progress is significant
    if performance.get('progress_score', 0) >= 70:
        await cl.Message(
            content=f"🎉 *[Internal: We're at {performance['progress_score']}% - getting close to the sale!]*",
            author="System"
        ).send()


if __name__ == "__main__":
    pass
