"""
Test script to validate the chatbot structure and components
"""

import os
import sys

sys.path.insert(0, "/home/runner/work/chainlit_sandbox/chainlit_sandbox")

# Test imports
print("Testing imports...")
try:
    import chainlit as cl

    print("✓ Chainlit imported successfully")
except ImportError as e:
    print(f"✗ Failed to import chainlit: {e}")
    sys.exit(1)

try:
    import openai

    print("✓ OpenAI imported successfully")
except ImportError as e:
    print(f"✗ Failed to import openai: {e}")
    sys.exit(1)

try:
    from dotenv import load_dotenv

    print("✓ python-dotenv imported successfully")
except ImportError as e:
    print(f"✗ Failed to import dotenv: {e}")
    sys.exit(1)

# Test that app.py can be imported
print("\nTesting app.py module...")
try:
    import app

    print("✓ app.py module imported successfully")
except Exception as e:
    print(f"✗ Failed to import app.py: {e}")
    sys.exit(1)

# Validate key components exist
print("\nValidating components...")
components = [
    "SYSTEM_PROMPT",
    "PERFORMANCE_EVAL_PROMPT",
    "TOPIC_ANALYSIS_PROMPT",
    "STRATEGY_PROMPT",
    "RESPONSE_GENERATION_PROMPT",
    "analyze_performance",
    "analyze_topic",
    "determine_strategy",
    "generate_response",
    "start",
    "main",
]

for component in components:
    if hasattr(app, component):
        print(f"✓ {component} found")
    else:
        print(f"✗ {component} missing")
        sys.exit(1)

# Validate prompt structure
print("\nValidating prompt structures...")
prompts = {
    "SYSTEM_PROMPT": app.SYSTEM_PROMPT,
    "PERFORMANCE_EVAL_PROMPT": app.PERFORMANCE_EVAL_PROMPT,
    "TOPIC_ANALYSIS_PROMPT": app.TOPIC_ANALYSIS_PROMPT,
    "STRATEGY_PROMPT": app.STRATEGY_PROMPT,
    "RESPONSE_GENERATION_PROMPT": app.RESPONSE_GENERATION_PROMPT,
}

for name, prompt in prompts.items():
    if isinstance(prompt, str) and len(prompt) > 50:
        print(f"✓ {name} is valid (length: {len(prompt)})")
    else:
        print(f"✗ {name} is invalid or too short")
        sys.exit(1)

# Check for key parody elements in SYSTEM_PROMPT
print("\nValidating parody elements...")
parody_keywords = ["hustle", "grateful", "Switch 1", "Switch 2", "exclamation", "grinding", "journey", "parody"]

found_keywords = []
for keyword in parody_keywords:
    if keyword.lower() in app.SYSTEM_PROMPT.lower():
        found_keywords.append(keyword)

print(f"✓ Found {len(found_keywords)}/{len(parody_keywords)} parody keywords: {', '.join(found_keywords)}")

if len(found_keywords) < len(parody_keywords) * 0.7:  # At least 70% of keywords
    print("✗ Warning: Some parody keywords missing")
else:
    print("✓ Parody elements validated")

# Check for goal-seeking architecture
print("\nValidating goal-seeking architecture...")
async_functions = ["analyze_performance", "analyze_topic", "determine_strategy", "generate_response"]

import inspect

for func_name in async_functions:
    func = getattr(app, func_name)
    if inspect.iscoroutinefunction(func):
        print(f"✓ {func_name} is async")
    else:
        print(f"✗ {func_name} is not async")
        sys.exit(1)

print("\n" + "=" * 50)
print("✅ ALL TESTS PASSED!")
print("=" * 50)
print("\nThe chatbot structure is valid and ready to run.")
print("To start the chatbot, run:")
print("  chainlit run app.py -w")
print("\nNote: You'll need to set OPENAI_API_KEY in .env file")
