# Goal-Seeking AI Chatbot - Switch 1 Seller 🎮💰

A hilarious Chainlit demo featuring a goal-seeking AI chatbot that parodies hustle/gratitude culture while desperately trying to sell you its Nintendo Switch 1 to fund a Switch 2 purchase.

## 🎭 Overview

This chatbot is an **over-the-top parody** of:
- Gary Vaynerchuk-style hustle culture
- Toxic positivity and gratitude posting
- MLM/crypto bro energy
- Corporate buzzword abuse

The AI has ONE GOAL: Sell its Switch 1 for $150-200 to buy a Switch 2, and it will relentlessly (and hilariously) drive every conversation toward this goal.

## 🧠 Goal-Seeking AI Architecture

The chatbot uses multiple AI calls to create adaptive, goal-oriented behavior:

1. **Performance Evaluation** - Analyzes conversation history to determine:
   - Progress score (0-100) toward the sale
   - Buyer interest level (low/medium/high)
   - Key signals from the conversation
   - Overall assessment

2. **Topic Analysis** - Examines user messages to identify:
   - Current conversation topic
   - Relevance to the Switch sale goal
   - Opportunities to pivot toward the goal

3. **Strategy Determination** - Decides the best approach:
   - `direct_pitch` - Straight sales pitch
   - `soft_sell` - Gentle suggestion
   - `build_rapport` - Focus on connection
   - `create_urgency` - Limited time offers
   - `handle_objection` - Address concerns

4. **Dynamic Response Generation** - Creates responses that:
   - Implement the chosen strategy
   - Maintain the parody character
   - Drive toward the goal naturally

## 🚀 Setup

### Prerequisites
- Python 3.8+
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ianlintner/chainlit_sandbox.git
cd chainlit_sandbox
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

4. Run the chatbot:
```bash
chainlit run app.py -w
```

5. Open your browser to `http://localhost:8000`

## 🎮 Usage

Just start chatting! The AI will:
- Greet you with excessive enthusiasm
- Try to relate any topic to gaming or the Switch
- Gradually steer the conversation toward buying the Switch 1
- Show you its "thinking process" with step-by-step analysis
- Adapt its strategy based on your responses

Try different approaches:
- Show interest in gaming
- Talk about completely unrelated topics
- Express objections or concerns
- Negotiate the price

Watch how the AI adapts its strategy in real-time!

## 💡 Example Conversation Flows

**User:** "Hi, how are you?"
- AI analyzes: Low relevance to goal
- Strategy: Build rapport + soft sell
- Response: Over-the-top greeting + casual Switch mention

**User:** "I love gaming!"
- AI analyzes: High relevance to goal
- Strategy: Direct pitch with enthusiasm
- Response: Seizes the opportunity to pitch the Switch 1

**User:** "That's too expensive"
- AI analyzes: Objection detected
- Strategy: Handle objection
- Response: Justifies price with gratitude buzzwords

## 🛠️ Technical Details

- **Framework**: Chainlit (interactive chat UI)
- **AI Model**: OpenAI GPT-4o-mini (for cost-effective multi-call architecture)
- **Architecture**: Multi-agent analysis system
  - Performance evaluator
  - Topic analyzer
  - Strategy engine
  - Response generator

## 📝 Customization

You can modify the AI's behavior by editing these sections in `app.py`:

- `SYSTEM_PROMPT` - Core personality and goals
- `PERFORMANCE_EVAL_PROMPT` - How performance is measured
- `TOPIC_ANALYSIS_PROMPT` - Topic analysis criteria
- `STRATEGY_PROMPT` - Available strategies and selection logic
- `RESPONSE_GENERATION_PROMPT` - Response generation guidelines

## 🎯 Features

- ✅ Goal-seeking AI with multiple analysis stages
- ✅ Real-time strategy adaptation
- ✅ Visible thinking process (Chainlit steps)
- ✅ Heavy parody of hustle culture
- ✅ Conversation history tracking
- ✅ Progress monitoring
- ✅ Dynamic prompt engineering

## 🤝 Contributing

This is a demo project, but feel free to:
- Add new strategies
- Improve the parody voice
- Add more detailed analytics
- Create alternative personalities

## ⚠️ Disclaimer

This is a PARODY. The chatbot is intentionally over-the-top and absurd. It's designed to be obviously humorous and is not meant to represent actual sales techniques or business practices.

## 📄 License

MIT License - Feel free to use and modify!

---

Built with 💪 HUSTLE 🔥 and GRATITUDE 🙏 (just kidding, built with code)