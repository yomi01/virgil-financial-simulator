#!/bin/bash

# Virgil Financial Simulator - Startup Script

echo "🚀 Starting Virgil Financial Simulator..."

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 is required but not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📋 Installing dependencies..."
pip install -r requirements.txt

# Run tests (optional)
if [ "$1" = "--test" ]; then
    echo "🧪 Running tests..."
    python -m pytest test_app.py -v
    if [ $? -ne 0 ]; then
        echo "❌ Tests failed. Please check the issues above."
        exit 1
    fi
    echo "✅ All tests passed!"
fi

# Start the Streamlit app
echo "🌐 Starting Streamlit application..."
echo "📱 The app will be available at: http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the application"
echo "---"

streamlit run app.py 