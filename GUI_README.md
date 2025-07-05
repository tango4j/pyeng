# pyEng GUI - Modern GUI for Language Learning

This project provides modern GUI versions of the pyEng language learning application, making it much more user-friendly while maintaining all the original functionality.

## 🚀 Quick Start

### Option 1: Launcher (Recommended)
Run the launcher to choose your preferred interface:
```bash
python run_gui.py
```

### Option 2: Direct Launch
- **Advanced GUI** (Full features): `python gui_advanced.py`
- **Basic GUI** (Simple interface): `python gui_main.py`
- **Original CLI**: `python main.py`

## 📋 Features

### Advanced GUI (`gui_advanced.py`)
- ✅ **Complete Feature Set**: All original pyEng features
- ✅ **Sentence Blanking**: Interactive word removal with progressive difficulty
- ✅ **Word Shuffling**: Clickable shuffled words for easy reconstruction
- ✅ **Three Study Modes**:
  - **Standard**: Progressive sentence blanking with word shuffling
  - **Review**: Simple sentence display without blanks
  - **Check Mode**: Direct translation practice
- ✅ **Modern Interface**: Clean, responsive design optimized for macOS
- ✅ **Progress Tracking**: Visual progress indicators
- ✅ **Interactive Feedback**: Immediate answer validation
- ✅ **Session Management**: Start, pause, and end study sessions

### Basic GUI (`gui_main.py`)
- ✅ **Simple Translation Practice**: Korean to English translation
- ✅ **Easy-to-Use Interface**: Minimal learning curve
- ✅ **Quick Study Sessions**: Perfect for beginners
- ✅ **Answer Validation**: Basic correct/incorrect feedback

## 🎯 Study Modes Explained

### Standard Mode
1. Shows Korean sentence
2. Displays English sentence with progressively more words blanked out
3. Provides shuffled words that can be clicked to insert
4. Multiple difficulty levels per sentence
5. Perfect for learning sentence structure

### Review Mode
1. Shows Korean sentence
2. Displays complete English sentence
3. No blanks or shuffling
4. Good for quick review and memorization

### Check Mode
1. Shows Korean sentence
2. User types English translation
3. Immediate feedback on correctness
4. Best for testing translation skills

## 🖥️ System Requirements

- **Python**: 3.6 or higher
- **Dependencies**: 
  - `tkinter` (usually included with Python)
  - `numpy` (for advanced features)
  - `csv` (for progress tracking)
- **OS**: macOS (optimized), Windows, Linux

## 📁 File Structure

```
pyeng/
├── run_gui.py          # Launcher application
├── gui_advanced.py     # Advanced GUI with all features
├── gui_main.py         # Basic GUI for simple practice
├── main.py             # Original command-line version
├── module.py           # Core study engine
├── display.py          # Display utilities
├── textdata0/          # Study content groups
├── textdata1/
├── textdata2/
└── textdata3/
```

## 🎮 How to Use

### Getting Started
1. **Launch the application**: `python run_gui.py`
2. **Choose your interface**: Select Advanced GUI (recommended)
3. **Configure your session**:
   - Select Dictionary Group (1-4)
   - Choose specific Dictionary
   - Pick Study Mode (Standard/Review/Check)
4. **Start studying**: Click "Start Study Session"

### During Study Session
- **Korean Sentence**: Read the Korean text to understand
- **Shuffled Words** (Standard mode): Click words to insert them
- **English Sentence**: See the sentence with blanks (Standard/Review)
- **Your Answer**: Type your translation
- **Submit**: Click "Submit Answer" to check
- **Feedback**: See if you're correct and get the right answer

### Controls
- **Submit Answer**: Check your translation
- **Show Answer**: Reveal the correct answer
- **Skip**: Move to next sentence
- **End Session**: Finish current study session

## 🔧 Customization

### Adding New Content
1. Create new text files in `textdata0/`, `textdata1/`, etc.
2. Format: `filename.txt` (English) and `filename_kor.txt` (Korean)
3. Update the dictionary table in `module.py` if needed

### Modifying Study Parameters
- **Blank Levels**: Adjust in `module.py` `lin_reg_out()` function
- **Sentence Length**: Modify `min_sent_length` and `max_sent_length`
- **Difficulty**: Change `min_level` and `max_level`

## 🐛 Troubleshooting

### Common Issues

**"No study content found"**
- Check that text files exist in the correct directories
- Verify file naming convention: `filename.txt` and `filename_kor.txt`

**"Failed to load dictionary data"**
- Ensure `module.py` is in the same directory
- Check that `textdata` folders contain valid content

**"Failed to start study session: expected floating-point number but got a list"**
- This bug has been fixed in the latest version
- The issue was in the linear regression calculation
- Update to the latest version if you encounter this

**GUI not displaying properly on macOS**
- The application automatically scales for macOS
- If issues persist, try running: `python3 gui_advanced.py`

### Performance Tips
- Close other applications for better performance
- Use Standard mode for best learning experience
- Take breaks between study sessions

## 📊 Progress Tracking

The application automatically tracks your progress using CSV files:
- **Total Trials**: Number of study sessions started
- **Completed Trials**: Number of sessions finished
- **Recent Date**: Last study session date

Progress files are stored in the respective `textdata` folders.

## 🤝 Contributing

To enhance the GUI:
1. Modify `gui_advanced.py` for new features
2. Update `gui_main.py` for basic interface changes
3. Test on different platforms
4. Update this README with new features

## 📝 License

Original pyEng code by inctrl. GUI enhancements added for improved user experience.

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Ensure text files are properly formatted
4. Try the original CLI version if GUI has issues

---

**Happy Learning! 🇰🇷 → 🇺🇸** 