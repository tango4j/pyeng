#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pyEng Advanced GUI - Complete GUI implementation with all original features
Author: inctrl (original) + Advanced GUI enhancement
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import queue
import sys
import os
import random
import math
import numpy as np
from datetime import datetime
import calendar

# Import the original module
from module import ThisStudy

class PyEngAdvancedGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("pyEng - Advanced Language Learning Application")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        
        # Set macOS-specific styling
        if sys.platform == "darwin":
            self.root.tk.call('tk', 'scaling', 2.0)
        
        # Initialize the study engine
        self.study_engine = ThisStudy()
        self.current_mode = tk.StringVar(value="Standard")
        self.current_group = tk.StringVar(value="1")
        self.current_dictionary = tk.StringVar(value="1")
        
        # Study state
        self.is_studying = False
        self.current_sentence_index = 0
        self.current_blank_level = 0
        self.blank_levels = []
        self.current_sentence = ""
        self.key_words = ""
        self.shuffled_words = ""
        self.erased_sentence = ""
        
        # Create GUI components
        self.setup_styles()
        self.create_widgets()
        self.load_dictionary_data()
        
        # Center the window
        self.center_window()
        
    def setup_styles(self):
        """Configure modern styling for the GUI"""
        style = ttk.Style()
        
        # Configure modern theme
        if 'clam' in style.theme_names():
            style.theme_use('clam')
        
        # Define color scheme
        self.colors = {
            'primary': '#2E86AB',      # Blue
            'secondary': '#A23B72',    # Purple
            'success': '#28A745',      # Green
            'warning': '#FFC107',      # Yellow
            'danger': '#DC3545',       # Red
            'info': '#17A2B8',         # Cyan
            'light': '#F8F9FA',        # Light gray
            'dark': '#343A40',         # Dark gray
            'white': '#FFFFFF',        # White
            'background': '#F5F5F5'    # Light background
        }
        
        # Configure colors and fonts with enhanced styling
        style.configure('Title.TLabel', 
                       font=('Helvetica', 20, 'bold'), 
                       foreground=self.colors['primary'],
                       background=self.colors['background'])
        
        style.configure('Header.TLabel', 
                       font=('Helvetica', 12, 'bold'), 
                       foreground=self.colors['dark'])
        
        style.configure('Info.TLabel', 
                       font=('Helvetica', 10), 
                       foreground=self.colors['dark'])
        
        style.configure('Success.TLabel', 
                       font=('Helvetica', 10, 'bold'), 
                       foreground=self.colors['success'])
        
        style.configure('Error.TLabel', 
                       font=('Helvetica', 10, 'bold'), 
                       foreground=self.colors['danger'])
        
        style.configure('Highlight.TLabel', 
                       font=('Helvetica', 11, 'bold'), 
                       foreground=self.colors['primary'])
        
        # Configure enhanced buttons with colors
        style.configure('Primary.TButton', 
                       font=('Helvetica', 11, 'bold'),
                       background=self.colors['primary'],
                       foreground=self.colors['white'])
        
        style.configure('Secondary.TButton', 
                       font=('Helvetica', 10),
                       background=self.colors['secondary'],
                       foreground=self.colors['white'])
        
        style.configure('Success.TButton', 
                       font=('Helvetica', 10, 'bold'), 
                       background=self.colors['success'],
                       foreground=self.colors['white'])
        
        style.configure('Warning.TButton', 
                       font=('Helvetica', 10, 'bold'),
                       background=self.colors['warning'],
                       foreground=self.colors['dark'])
        
        style.configure('Danger.TButton', 
                       font=('Helvetica', 10, 'bold'),
                       background=self.colors['danger'],
                       foreground=self.colors['white'])
        
        # Add Info button style
        style.configure('Info.TButton', 
                       font=('Helvetica', 10, 'bold'),
                       background=self.colors['info'],
                       foreground=self.colors['white'])
        
        # Configure checkbox style
        style.configure('Check.TCheckbutton', 
                       font=('Helvetica', 10),
                       foreground=self.colors['dark'],
                       background=self.colors['white'])
        
        # Configure frames with subtle borders
        style.configure('Card.TFrame', 
                       background=self.colors['white'],
                       relief='solid',
                       borderwidth=1)
        
        # Configure LabelFrames with enhanced styling
        style.configure('Card.TLabelframe', 
                       background=self.colors['white'],
                       relief='solid',
                       borderwidth=2)
        
        style.configure('Card.TLabelframe.Label', 
                       font=('Helvetica', 11, 'bold'),
                       foreground=self.colors['primary'],
                       background=self.colors['white'])
        
    def create_widgets(self):
        """Create and organize all GUI widgets"""
        # Set background color for root window
        self.root.configure(bg=self.colors['background'])
        
        # Main container with enhanced styling
        main_frame = ttk.Frame(self.root, padding="15", style='Card.TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title with enhanced styling
        title_frame = ttk.Frame(main_frame, style='Card.TFrame')
        title_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        title_frame.columnconfigure(0, weight=1)
        
        title_label = ttk.Label(title_frame, text="🎓 pyEng Advanced Language Learning", style='Title.TLabel')
        title_label.grid(row=0, column=0, pady=15)
        
        # Configuration Frame with enhanced styling
        config_frame = ttk.LabelFrame(main_frame, text="⚙️ Study Configuration", padding="15", style='Card.TLabelframe')
        config_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        config_frame.columnconfigure(1, weight=1)
        config_frame.columnconfigure(3, weight=1)
        
        # Group selection
        ttk.Label(config_frame, text="Dictionary Group:", style='Header.TLabel').grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.group_combo = ttk.Combobox(config_frame, textvariable=self.current_group, state="readonly", width=15)
        self.group_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 20))
        self.group_combo.bind('<<ComboboxSelected>>', self.on_group_changed)
        
        # Dictionary selection
        ttk.Label(config_frame, text="Dictionary:", style='Header.TLabel').grid(row=0, column=2, sticky=tk.W, padx=(0, 10))
        self.dictionary_combo = ttk.Combobox(config_frame, textvariable=self.current_dictionary, state="readonly", width=15)
        self.dictionary_combo.grid(row=0, column=3, sticky=(tk.W, tk.E), padx=(0, 20))
        
        # Study mode
        ttk.Label(config_frame, text="Study Mode:", style='Header.TLabel').grid(row=1, column=0, sticky=tk.W, padx=(0, 10), pady=(10, 0))
        self.mode_combo = ttk.Combobox(config_frame, textvariable=self.current_mode, state="readonly", width=15)
        self.mode_combo['values'] = ('Standard', 'Review', 'Check mode')
        self.mode_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(0, 20), pady=(10, 0))

        # Random order checkbox
        self.random_order_var = tk.BooleanVar(value=False)
        self.random_checkbox = ttk.Checkbutton(config_frame, text="🎲 Random Text Order", 
                                              variable=self.random_order_var, style='Check.TCheckbutton')
        self.random_checkbox.grid(row=1, column=2, sticky=tk.W, padx=(0, 20), pady=(10, 0))
        
        # Start button with enhanced styling
        self.start_button = ttk.Button(config_frame, text="🚀 Start Study Session", style='Primary.TButton', 
                                      command=self.start_study_session)
        self.start_button.grid(row=1, column=3, sticky=(tk.W, tk.E), padx=(0, 20), pady=(10, 0))
        
        # Study Area Frame with enhanced styling
        study_frame = ttk.LabelFrame(main_frame, text="📚 Study Area", padding="15", style='Card.TLabelframe')
        study_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 15))
        study_frame.columnconfigure(0, weight=1)
        study_frame.rowconfigure(1, weight=1)
        study_frame.rowconfigure(3, weight=1)
        study_frame.rowconfigure(5, weight=1)
        
        # Progress info with enhanced styling
        progress_frame = ttk.Frame(study_frame, style='Card.TFrame')
        progress_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        progress_frame.columnconfigure(0, weight=1)
        
        self.progress_label = ttk.Label(progress_frame, text="🎯 Ready to start study session", style='Info.TLabel')
        self.progress_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        
        # Korean sentence display with enhanced styling (single line)
        ttk.Label(study_frame, text="🇰🇷 Korean Sentence:", style='Header.TLabel').grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        self.korean_text = scrolledtext.ScrolledText(study_frame, height=1, wrap=tk.WORD, font=('Helvetica', 12),
                                                    bg=self.colors['light'], fg=self.colors['dark'],
                                                    insertbackground=self.colors['primary'],
                                                    selectbackground=self.colors['primary'],
                                                    selectforeground=self.colors['white'])
        self.korean_text.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # Shuffled words display (for blanking mode) with enhanced styling (single line)
        self.shuffled_frame = ttk.LabelFrame(study_frame, text="🔤 Shuffled Words", padding="10", style='Card.TLabelframe')
        self.shuffled_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        self.shuffled_frame.columnconfigure(0, weight=1)
        
        self.shuffled_text = scrolledtext.ScrolledText(self.shuffled_frame, height=1, wrap=tk.WORD, font=('Helvetica', 11),
                                                      bg=self.colors['info'], fg=self.colors['white'],
                                                      insertbackground=self.colors['white'],
                                                      selectbackground=self.colors['warning'],
                                                      selectforeground=self.colors['dark'])
        self.shuffled_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # English sentence display (with blanks) with enhanced styling (single line)
        ttk.Label(study_frame, text="🇺🇸 English Sentence (with blanks):", style='Header.TLabel').grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
        self.english_display = scrolledtext.ScrolledText(study_frame, height=1, wrap=tk.WORD, font=('Helvetica', 12),
                                                        bg=self.colors['light'], fg=self.colors['dark'],
                                                        insertbackground=self.colors['primary'],
                                                        selectbackground=self.colors['primary'],
                                                        selectforeground=self.colors['white'])
        self.english_display.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # English input area with enhanced styling (single line)
        ttk.Label(study_frame, text="✍️ Your Answer:", style='Header.TLabel').grid(row=6, column=0, sticky=tk.W, pady=(0, 5))
        self.english_input = scrolledtext.ScrolledText(study_frame, height=1, wrap=tk.WORD, font=('Helvetica', 12),
                                                      bg=self.colors['white'], fg=self.colors['dark'],
                                                      insertbackground=self.colors['primary'],
                                                      selectbackground=self.colors['primary'],
                                                      selectforeground=self.colors['white'])
        self.english_input.grid(row=7, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        self.english_input.bind('<Return>', self._on_enter_submit)
        
        # Control buttons with enhanced styling
        button_frame = ttk.Frame(study_frame, style='Card.TFrame')
        button_frame.grid(row=8, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        button_frame.columnconfigure(1, weight=1)
        
        self.submit_button = ttk.Button(button_frame, text="✅ Submit Answer", style='Success.TButton', 
                                       command=self.submit_answer, state='disabled')
        self.submit_button.grid(row=0, column=0, padx=(10, 10), pady=10)
        
        self.show_answer_button = ttk.Button(button_frame, text="👁️ Show Answer", style='Info.TButton', 
                                            command=self.show_correct_answer, state='disabled')
        self.show_answer_button.grid(row=0, column=1, padx=(0, 10), pady=10)
        
        self.skip_button = ttk.Button(button_frame, text="⏭️ Skip", style='Warning.TButton', 
                                     command=self.skip_sentence, state='disabled')
        self.skip_button.grid(row=0, column=2, padx=(0, 10), pady=10)
        
        self.end_button = ttk.Button(button_frame, text="⏹️ End Session", style='Danger.TButton', 
                                    command=self.end_study_session, state='disabled')
        self.end_button.grid(row=0, column=3, padx=(0, 10), pady=10)
        
        # Feedback area with enhanced styling
        feedback_frame = ttk.LabelFrame(study_frame, text="💬 Feedback", padding="10", style='Card.TLabelframe')
        feedback_frame.grid(row=9, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 15))
        feedback_frame.columnconfigure(0, weight=1)
        feedback_frame.rowconfigure(0, weight=1)
        
        self.feedback_text = scrolledtext.ScrolledText(feedback_frame, height=1, wrap=tk.WORD, font=('Helvetica', 10),
                                                      bg=self.colors['light'], fg=self.colors['dark'],
                                                      insertbackground=self.colors['primary'],
                                                      selectbackground=self.colors['primary'],
                                                      selectforeground=self.colors['white'])
        self.feedback_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Status bar with enhanced styling
        status_frame = ttk.Frame(main_frame, style='Card.TFrame')
        status_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        status_frame.columnconfigure(0, weight=1)
        
        self.status_var = tk.StringVar(value="🚀 Ready")
        status_bar = ttk.Label(status_frame, textvariable=self.status_var, 
                              font=('Helvetica', 9, 'bold'),
                              foreground=self.colors['primary'],
                              background=self.colors['light'],
                              anchor=tk.W)
        status_bar.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=10, pady=5)
        
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def load_dictionary_data(self):
        """Load dictionary groups and populate combo boxes"""
        try:
            pyEng_dic, pyEng_folder, _ = self.study_engine.read_dic_table()
            
            # Populate group combo with string indices
            group_names = [str(i+1) for i in range(len(pyEng_dic))]
            self.group_combo['values'] = group_names
            self.group_combo.current(0)
            
            # Populate dictionary combo for first group
            self.update_dictionary_combo()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load dictionary data: {str(e)}")
            
    def update_dictionary_combo(self):
        """Update dictionary combo box based on selected group"""
        try:
            pyEng_dic, pyEng_folder, _ = self.study_engine.read_dic_table()
            group_index = int(self.current_group.get()) - 1
            
            if 0 <= group_index < len(pyEng_dic):
                dictionaries = pyEng_dic[group_index]
                self.dictionary_combo['values'] = dictionaries
                self.dictionary_combo.current(0)
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update dictionary list: {str(e)}")
            
    def on_group_changed(self, event=None):
        """Handle group selection change"""
        self.update_dictionary_combo()
        

            
    def start_study_session(self):
        """Start a new study session"""
        try:
            # Configure study engine
            self.study_engine.group_index_out = int(self.current_group.get())
            self.study_engine.dic_index_out = self.dictionary_combo.current() + 1
            
            # Set study mode
            mode_map = {'Standard': 1, 'Review': 2, 'Check mode': 3}
            self.study_engine.mode = mode_map[self.current_mode.get()]
            self.study_engine.mode_str = ['[1] Standard', '[2] Review', '[3] Check mode']
            
            # Load study files
            self.study_engine.read_file()
            
            if not self.study_engine.list_kor or not self.study_engine.list_eng:
                messagebox.showerror("Error", "No study content found for selected dictionary")
                return
                
            # Initialize study session
            self.is_studying = True
            self.current_sentence_index = 0
            self.current_blank_level = 0
            self.total_sentences = len(self.study_engine.list_kor)

            # Create sentence order (random or sequential)
            if self.random_order_var.get():
                self.sentence_order = list(range(self.total_sentences))
                random.shuffle(self.sentence_order)
            else:
                self.sentence_order = list(range(self.total_sentences))
            
            # Update UI
            self.start_button.config(state='disabled')
            self.submit_button.config(state='normal')
            self.show_answer_button.config(state='normal')
            self.skip_button.config(state='normal')
            self.end_button.config(state='normal')
            self.group_combo.config(state='disabled')
            self.dictionary_combo.config(state='disabled')
            self.mode_combo.config(state='disabled')
            self.random_checkbox.config(state='disabled')
            
            # Show first sentence
            self.show_current_sentence()
            
            # Update status with random order info
            random_info = " (Random Order)" if self.random_order_var.get() else ""
            self.status_var.set(f"🚀 Study session started - {self.current_mode.get()} mode{random_info}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start study session: {str(e)}")
            
    def show_current_sentence(self):
        """Display the current sentence for study"""
        if self.current_sentence_index < self.total_sentences:
            # Get the actual sentence index based on random order if enabled
            actual_index = self.sentence_order[self.current_sentence_index]
            
            # Get Korean sentence
            korean_sentence = self.study_engine.list_kor[actual_index].strip()
            self.korean_text.delete(1.0, tk.END)
            self.korean_text.insert(1.0, korean_sentence)
            
            # Get English sentence
            self.current_sentence = self.study_engine.list_eng[actual_index].strip()
            
            # Clear previous input and feedback
            self.english_input.delete(1.0, tk.END)
            self.feedback_text.delete(1.0, tk.END)
            
            # Update progress
            progress_text = f"📝 Sentence {self.current_sentence_index + 1} of {self.total_sentences}"
            self.progress_label.config(text=progress_text)
            
            # Handle different study modes
            mode = self.current_mode.get()
            if mode == "Check mode":
                # Show Korean sentence and wait for input
                self.english_display.delete(1.0, tk.END)
                self.english_display.insert(1.0, "Type your translation below...")
                self.shuffled_frame.grid_remove()  # Hide shuffled words
            else:
                # Standard or Review mode - show blanked sentence
                self.prepare_blanked_sentence()
            
            # Focus on input
            self.english_input.focus()
            
        else:
            self.end_study_session()
            
    def prepare_blanked_sentence(self):
        """Prepare the blanked sentence for Standard/Review mode"""
        # Calculate blank levels
        len_sent = len(self.current_sentence)
        regressed_level = self.study_engine.lin_reg_out(len_sent)
        
        if self.current_mode.get() == "Standard":
            # Ensure regressed_level is at least 1 to avoid division by zero
            if regressed_level < 1:
                regressed_level = 1
            self.blank_levels = np.arange(0.3, 1, (1 / regressed_level))
        elif self.current_mode.get() == "Review":
            self.blank_levels = [0]  # No blanks for review mode
            
        self.current_blank_level = 0
        self.show_blanked_sentence()
        
    def show_blanked_sentence(self):
        """Show the current blanked sentence"""
        if self.current_blank_level < len(self.blank_levels):
            degree = self.blank_levels[self.current_blank_level]
            
            # Create blanked sentence
            self.erased_sentence, self.key_words = self.study_engine.sentence_eraser(self.current_sentence, degree)
            self.shuffled_words = self.study_engine.sentence_shuffler(self.key_words)
            
            # Display shuffled words
            self.shuffled_text.delete(1.0, tk.END)
            self.shuffled_text.insert(1.0, self.shuffled_words)
            self.shuffled_frame.grid()  # Show shuffled words
            
            # Display blanked sentence
            self.english_display.delete(1.0, tk.END)
            self.english_display.insert(1.0, self.erased_sentence)
            
            # Update progress
            progress_text = f"📝 Sentence {self.current_sentence_index + 1} of {self.total_sentences} - 🎯 Level {self.current_blank_level + 1} of {len(self.blank_levels)}"
            self.progress_label.config(text=progress_text)
            
        else:
            # All blank levels completed, move to next sentence
            self.next_sentence()
            
    def submit_answer(self):
        """Submit user's answer for evaluation"""
        if not self.is_studying:
            return
            
        user_answer = self.english_input.get(1.0, tk.END).strip()
        if not user_answer:
            messagebox.showwarning("Warning", "Please enter your answer")
            return
            
        # Compare answers
        is_correct = user_answer.lower() == self.current_sentence.lower()
        
        # Show feedback
        feedback = f"Your answer: {user_answer}\n\n"
        if is_correct:
            feedback += "🎉 Correct! Well done! 🌟"
            self.feedback_text.config(foreground=self.colors['success'])
            
            # Move to next blank level or sentence
            if self.current_mode.get() in ["Standard", "Review"]:
                self.current_blank_level += 1
                self.root.after(1000, self.show_blanked_sentence)
            else:
                self.root.after(1000, self.next_sentence)
        else:
            feedback += f"❌ Incorrect. Try again or click 'Show Answer' to see the correct answer."
            self.feedback_text.config(foreground=self.colors['danger'])
            
        self.feedback_text.delete(1.0, tk.END)
        self.feedback_text.insert(1.0, feedback)
        
        # Clear the answer input box
        self.english_input.delete(1.0, tk.END)
        
    def show_correct_answer(self):
        """Show the correct answer"""
        feedback = f"📖 Correct answer: {self.current_sentence}\n\n"
        feedback += "💡 Study this sentence and try to remember it!"
        
        self.feedback_text.delete(1.0, tk.END)
        self.feedback_text.insert(1.0, feedback)
        self.feedback_text.config(foreground=self.colors['info'])
        
        # Move to next after showing answer
        if self.current_mode.get() in ["Standard", "Review"]:
            self.current_blank_level += 1
            self.root.after(3000, self.show_blanked_sentence)
        else:
            self.root.after(3000, self.next_sentence)
        
    def skip_sentence(self):
        """Skip current sentence"""
        if self.is_studying:
            self.next_sentence()
            
    def next_sentence(self):
        """Move to next sentence"""
        if self.is_studying:
            self.current_sentence_index += 1
            if self.current_sentence_index < self.total_sentences:
                self.show_current_sentence()
            else:
                self.end_study_session()
                
    def end_study_session(self):
        """End the current study session"""
        self.is_studying = False
        
        # Reset UI
        self.start_button.config(state='normal')
        self.submit_button.config(state='disabled')
        self.show_answer_button.config(state='disabled')
        self.skip_button.config(state='disabled')
        self.end_button.config(state='disabled')
        self.group_combo.config(state='readonly')
        self.dictionary_combo.config(state='readonly')
        self.mode_combo.config(state='readonly')
        self.random_checkbox.config(state='normal')
        
        # Clear study area
        self.korean_text.delete(1.0, tk.END)
        self.english_display.delete(1.0, tk.END)
        self.english_input.delete(1.0, tk.END)
        self.feedback_text.delete(1.0, tk.END)
        self.shuffled_text.delete(1.0, tk.END)
        self.shuffled_frame.grid_remove()
        self.progress_label.config(text="🎯 Ready to start study session")
        
        self.status_var.set("🏁 Study session ended")
        
        if self.current_sentence_index >= self.total_sentences:
            messagebox.showinfo("🎉 Session Complete", "🎊 Congratulations! You've completed all sentences in this session. 🌟")

    def _on_enter_submit(self, event):
        self.submit_answer()
        return 'break'  # Prevent newline in the input box

def main():
    """Main function to run the GUI application"""
    root = tk.Tk()
    app = PyEngAdvancedGUI(root)
    
    # Handle window close
    def on_closing():
        if app.is_studying:
            if messagebox.askokcancel("Quit", "Study session in progress. Are you sure you want to quit?"):
                root.destroy()
        else:
            root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    main() 