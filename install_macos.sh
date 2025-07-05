#!/bin/bash

# pyEng GUI Installation Script for macOS
# This script installs all necessary dependencies for the pyEng GUI

echo "🚀 Installing pyEng GUI dependencies for macOS..."

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew is not installed. Please install Homebrew first:"
    echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    exit 1
fi

echo "✅ Homebrew found"

# Install Python with tkinter support
echo "📦 Installing Python with tkinter support..."
brew install python-tk

# Install numpy for advanced features
echo "📦 Installing numpy for advanced features..."
brew install numpy

# Check if installation was successful
echo "🔍 Verifying installation..."

if python3 -c "import tkinter; print('✅ tkinter available')" 2>/dev/null; then
    echo "✅ tkinter is working"
else
    echo "❌ tkinter installation failed"
    exit 1
fi

if python3 -c "import numpy; print('✅ numpy available')" 2>/dev/null; then
    echo "✅ numpy is working"
else
    echo "❌ numpy installation failed"
    exit 1
fi

echo ""
echo "🎉 Installation complete!"
echo ""
echo "To run pyEng GUI:"
echo "   python3 run_gui.py"
echo ""
echo "Or run specific versions:"
echo "   python3 gui_advanced.py  # Advanced GUI with all features"
echo "   python3 gui_main.py      # Basic GUI for simple practice"
echo "   python3 main.py          # Original command-line version"
echo ""
echo "📖 For more information, see GUI_README.md" 