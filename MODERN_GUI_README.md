# pyEng Modern GUI - Enhanced Interface with Gradients and Shadows

## 🎨 Overview

The pyEng Modern GUI brings a beautiful, modern interface to the pyEng language learning application with:

- **Gradient Buttons**: Custom buttons with smooth gradients and shadow effects
- **Modern Color Schemes**: Three beautiful color themes (Blue, Purple, Green)
- **Enhanced Typography**: Improved fonts and text styling
- **Smooth Animations**: Hover effects and button press animations
- **Professional Layout**: Clean, organized interface with proper spacing
- **Emoji Icons**: Visual indicators for better user experience

## 🚀 Quick Start

### Run the Modern GUI Launcher
```bash
python run_gui_modern.py
```

### Run Specific Modern GUI Versions
```bash
# Basic Modern GUI (Simple translation practice)
python gui_main_modern.py

# Advanced Modern GUI (Full features with blanking mode)
python gui_advanced_modern.py
```

### Test the Components
```bash
python test_modern_gui.py
```

## 🎨 Features

### 1. Modern Styling System (`gui_tk/modern_styles.py`)

#### Color Schemes
- **Blue Theme**: Professional and clean (default)
- **Purple Theme**: Creative and modern
- **Green Theme**: Fresh and natural

#### Components
- `ModernStyles`: Main styling class with color schemes
- `GradientButton`: Custom buttons with gradients and shadows
- `ModernFrame`: Enhanced frame with modern styling
- `ModernLabelFrame`: Modern labeled frames
- `ModernEntry`: Styled entry widgets
- `ModernText`: Enhanced text widgets

### 2. Basic Modern GUI (`gui_main_modern.py`)

**Features:**
- Simple translation practice
- Modern interface with gradients
- Easy-to-use design
- Perfect for beginners
- Quick study sessions

**Key Components:**
- Gradient start button
- Modern text areas with enhanced styling
- Color-coded feedback system
- Smooth animations

### 3. Advanced Modern GUI (`gui_advanced_modern.py`)

**Features:**
- Full feature set with sentence blanking
- Word shuffling and interactive learning
- All three study modes (Standard, Review, Check)
- Modern interface with animations
- Best for regular study sessions

**Key Components:**
- Interactive word shuffling area
- Sentence blanking with visual feedback
- Multiple gradient buttons for different actions
- Enhanced study area with modern styling

### 4. Modern Launcher (`run_gui_modern.py`)

**Features:**
- Choose between all GUI versions
- Modern interface with descriptions
- Easy navigation between options
- Visual indicators for each option

## 🎯 Usage Guide

### Starting a Study Session

1. **Launch the Modern GUI**
   ```bash
   python run_gui_modern.py
   ```

2. **Choose Your Interface**
   - **Modern Advanced** (Recommended): Full features with modern styling
   - **Modern Basic**: Simple interface with modern styling
   - **Legacy Advanced**: Original advanced features
   - **Legacy Basic**: Original basic interface
   - **Original CLI**: Command-line interface

3. **Configure Study Settings**
   - Select Dictionary Group
   - Choose Dictionary
   - Pick Study Mode (Standard, Review, Check mode)
   - Enable/disable Random Text Order

4. **Start Learning**
   - Click the gradient "Start Study Session" button
   - Follow the prompts and practice translations

### Advanced Features (Advanced GUI)

#### Sentence Blanking Mode
- Korean sentences are displayed
- English sentences have key words replaced with blanks
- Shuffled words are provided for filling blanks
- Click words to add them to your answer

#### Word Shuffling
- Important words are extracted from sentences
- Words are shuffled and displayed separately
- Click words to use them in your answer
- Interactive learning experience

## 🎨 Customization

### Changing Color Themes

You can easily change the color theme by modifying the theme parameter:

```python
# In any modern GUI file, change this line:
self.styles = ModernStyles('blue')  # Options: 'blue', 'purple', 'green'
```

### Available Themes

#### Blue Theme (Default)
- Primary: `#2563eb` (Modern blue)
- Background: `#f8fafc` (Light gray)
- Surface: `#ffffff` (White)
- Text: `#1e293b` (Dark gray)

#### Purple Theme
- Primary: `#7c3aed` (Modern purple)
- Background: `#faf5ff` (Light purple)
- Surface: `#ffffff` (White)
- Text: `#1e1b4b` (Dark purple)

#### Green Theme
- Primary: `#059669` (Modern green)
- Background: `#f0fdf4` (Light green)
- Surface: `#ffffff` (White)
- Text: `#14532d` (Dark green)

### Customizing Gradients

The gradient buttons automatically create:
- **Shadow effects**: Subtle shadows for depth
- **Hover effects**: Color changes on mouse hover
- **Press effects**: Visual feedback when clicked
- **Highlight effects**: Lighter top edges for 3D appearance

## 🔧 Technical Details

### Dependencies
- `tkinter`: Built-in Python GUI framework
- `threading`: For background operations
- `queue`: For data management
- `random`: For word shuffling
- `numpy`: For advanced calculations (optional)

### File Structure
```
pyeng/
├── gui_tk/
│   └── modern_styles.py          # Modern styling components
├── gui_main_modern.py            # Basic modern GUI
├── gui_advanced_modern.py        # Advanced modern GUI
├── run_gui_modern.py             # Modern launcher
├── test_modern_gui.py            # Test script
└── MODERN_GUI_README.md          # This file
```

### Component Architecture

#### ModernStyles Class
- Manages color schemes and themes
- Configures ttk styles
- Provides consistent styling across the application

#### GradientButton Class
- Custom canvas-based button
- Implements gradient effects and shadows
- Handles mouse events (hover, press, click)
- Supports multiple button styles (primary, secondary, success, warning, danger)

#### Modern Widgets
- Enhanced versions of standard tkinter widgets
- Consistent styling with the modern theme
- Better visual hierarchy and spacing

## 🎯 Best Practices

### For Users
1. **Start with Modern Advanced**: Best overall experience
2. **Use the launcher**: Easy way to choose your preferred interface
3. **Try different themes**: Find the color scheme you prefer
4. **Practice regularly**: Use the modern interface for consistent learning

### For Developers
1. **Extend ModernStyles**: Add new color schemes easily
2. **Use GradientButton**: For consistent button styling
3. **Follow the pattern**: Use ModernFrame and ModernLabelFrame for containers
4. **Test thoroughly**: Use the test script to verify components

## 🐛 Troubleshooting

### Common Issues

#### Import Errors
```bash
# If you get import errors, make sure you're in the correct directory
cd /path/to/pyeng
python run_gui_modern.py
```

#### Display Issues
- **macOS**: The GUI automatically scales for Retina displays
- **Windows**: Should work with standard DPI settings
- **Linux**: May need to adjust scaling manually

#### Performance Issues
- Close other applications to free up memory
- The modern GUI uses more resources than the basic version
- Consider using the basic modern GUI for older systems

### Getting Help

1. **Run the test script**: `python test_modern_gui.py`
2. **Check the console**: Look for error messages
3. **Try the legacy versions**: If modern GUI has issues
4. **Report issues**: Include your system information and error messages

## 🎉 What's New

### Version 2.0 - Modern GUI
- ✅ Gradient buttons with shadows
- ✅ Three beautiful color themes
- ✅ Enhanced typography and spacing
- ✅ Smooth animations and hover effects
- ✅ Professional layout design
- ✅ Emoji icons for better UX
- ✅ Interactive word shuffling
- ✅ Modern launcher interface
- ✅ Comprehensive documentation

### Future Enhancements
- [ ] Dark mode support
- [ ] Custom theme creation
- [ ] More animation effects
- [ ] Accessibility improvements
- [ ] Mobile-responsive design
- [ ] Additional color schemes

## 📝 License

This modern GUI enhancement is built on top of the original pyEng application. The modern styling and enhancements are designed to improve the user experience while maintaining all original functionality.

---

**Enjoy learning Korean with the beautiful new pyEng Modern GUI! 🎓🇰🇷** 