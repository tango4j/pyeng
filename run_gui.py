#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pyEng GUI Launcher - Choose between basic and advanced GUI versions
Author: inctrl (original) + GUI enhancement
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

def run_basic_gui():
    """Launch the basic GUI version"""
    try:
        from gui_main import main as basic_main
        basic_main()
    except ImportError as e:
        messagebox.showerror("Error", f"Could not import basic GUI: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start basic GUI: {str(e)}")

def run_advanced_gui():
    """Launch the advanced GUI version"""
    try:
        from gui_advanced import main as advanced_main
        advanced_main()
    except ImportError as e:
        messagebox.showerror("Error", f"Could not import advanced GUI: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start advanced GUI: {str(e)}")

def run_original_cli():
    """Launch the original command-line version"""
    try:
        from main import main as cli_main
        cli_main()
    except ImportError as e:
        messagebox.showerror("Error", f"Could not import original CLI: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start original CLI: {str(e)}")

class LauncherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("pyEng Launcher")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Set macOS-specific styling
        if sys.platform == "darwin":
            self.root.tk.call('tk', 'scaling', 2.0)
        
        self.setup_styles()
        self.create_widgets()
        self.center_window()
        
    def setup_styles(self):
        """Configure modern styling"""
        style = ttk.Style()
        if 'clam' in style.theme_names():
            style.theme_use('clam')
        
        style.configure('Title.TLabel', font=('Helvetica', 16, 'bold'))
        style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))
        style.configure('Info.TLabel', font=('Helvetica', 10))
        style.configure('Primary.TButton', font=('Helvetica', 11, 'bold'))
        style.configure('Secondary.TButton', font=('Helvetica', 10))
        
    def create_widgets(self):
        """Create launcher interface"""
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="pyEng Language Learning", style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        # Welcome message
        welcome_text = """Welcome to pyEng - Your Korean to English Language Learning Application!

Choose your preferred interface:"""
        welcome_label = ttk.Label(main_frame, text=welcome_text, style='Info.TLabel', justify=tk.CENTER)
        welcome_label.grid(row=1, column=0, columnspan=2, pady=(0, 30))
        
        # Advanced GUI Button
        advanced_frame = ttk.LabelFrame(main_frame, text="Recommended", padding="15")
        advanced_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        advanced_desc = """Advanced GUI (Recommended)
• Full feature set with sentence blanking
• Word shuffling and interactive learning
• All three study modes (Standard, Review, Check)
• Modern, user-friendly interface
• Best for regular study sessions"""
        
        advanced_label = ttk.Label(advanced_frame, text=advanced_desc, style='Info.TLabel', justify=tk.LEFT)
        advanced_label.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        advanced_button = ttk.Button(advanced_frame, text="Launch Advanced GUI", style='Primary.TButton',
                                    command=self.launch_advanced)
        advanced_button.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Basic GUI Button
        basic_frame = ttk.LabelFrame(main_frame, text="Simple Interface", padding="15")
        basic_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        basic_desc = """Basic GUI
• Simple translation practice
• Easy-to-use interface
• Good for beginners
• Quick study sessions"""
        
        basic_label = ttk.Label(basic_frame, text=basic_desc, style='Info.TLabel', justify=tk.LEFT)
        basic_label.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        basic_button = ttk.Button(basic_frame, text="Launch Basic GUI", style='Secondary.TButton',
                                 command=self.launch_basic)
        basic_button.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Original CLI Button
        cli_frame = ttk.LabelFrame(main_frame, text="Original Interface", padding="15")
        cli_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        cli_desc = """Original Command Line Interface
• The original pyEng experience
• Full feature set
• Terminal-based interface
• For advanced users or scripting"""
        
        cli_label = ttk.Label(cli_frame, text=cli_desc, style='Info.TLabel', justify=tk.LEFT)
        cli_label.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        cli_button = ttk.Button(cli_frame, text="Launch Original CLI", style='Secondary.TButton',
                               command=self.launch_cli)
        cli_button.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Exit button
        exit_button = ttk.Button(main_frame, text="Exit", style='Secondary.TButton',
                                command=self.root.destroy)
        exit_button.grid(row=5, column=0, columnspan=2, pady=(20, 0))
        
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def launch_advanced(self):
        """Launch advanced GUI"""
        self.root.destroy()
        run_advanced_gui()
        
    def launch_basic(self):
        """Launch basic GUI"""
        self.root.destroy()
        run_basic_gui()
        
    def launch_cli(self):
        """Launch original CLI"""
        self.root.destroy()
        run_original_cli()

def main():
    """Main launcher function"""
    root = tk.Tk()
    app = LauncherGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 