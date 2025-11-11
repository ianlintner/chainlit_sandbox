#!/bin/bash
# Quick start script for the Goal-Seeking AI Chatbot

echo "🚀 Goal-Seeking AI Chatbot - Quick Start 🚀"
echo "==========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip &> /dev/null && ! command -v pip3 &> /dev/null; then
    echo "❌ pip is not installed. Please install pip."
    exit 1
fi

echo "✓ pip found"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1 || pip3 install -r requirements.txt > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  No .env file found!"
    echo ""
    echo "Creating .env from template..."
    cp .env.example .env
    echo ""
    echo "📝 Please edit the .env file and add your OpenAI API key:"
    echo "   nano .env  (or use your favorite editor)"
    echo ""
    echo "Then run this script again or start the chatbot with:"
    echo "   chainlit run app.py -w"
    exit 0
fi

# Check if API key is set
if grep -q "your_openai_api_key_here" .env; then
    echo "⚠️  OpenAI API key not set in .env file!"
    echo ""
    echo "Please edit the .env file and add your OpenAI API key:"
    echo "   nano .env  (or use your favorite editor)"
    echo ""
    echo "Then run this script again or start the chatbot with:"
    echo "   chainlit run app.py -w"
    exit 0
fi

echo "✓ .env file configured"
echo ""
echo "🎉 Everything is ready!"
echo ""
echo "Starting the chatbot..."
echo ""
echo "The chatbot will open in your browser at http://localhost:8000"
echo "Press Ctrl+C to stop the chatbot"
echo ""

# Start the chatbot
chainlit run app.py -w
