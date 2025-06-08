@echo off
echo 🚀 Starting Virgil Financial Simulator...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is required but not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/update dependencies
echo 📋 Installing dependencies...
pip install -r requirements.txt

REM Run tests if requested
if "%1"=="--test" (
    echo 🧪 Running tests...
    python -m pytest test_app.py -v
    if errorlevel 1 (
        echo ❌ Tests failed. Please check the issues above.
        pause
        exit /b 1
    )
    echo ✅ All tests passed!
)

REM Start the Streamlit app
echo 🌐 Starting Streamlit application...
echo 📱 The app will be available at: http://localhost:8501
echo 🛑 Press Ctrl+C to stop the application
echo ---

streamlit run app.py

pause 