#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pyEng GUI - Modern GUI for the pyEng language learning application
Author: inctrl (original) + GUI enhancement
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import queue
import sys
import os
from datetime import datetime
import calendar

# Import the original module
from module import ThisStudy

class PyEngGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("pyEng - Language Learning Application")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        
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
        self.sentence_queue = queue.Queue()
        
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
        
        # Configure colors and fonts
        style.configure('Title.TLabel', font=('Helvetica', 16, 'bold'))
        style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))
        style.configure('Info.TLabel', font=('Helvetica', 10))
        style.configure('Success.TLabel', font=('Helvetica', 10), foreground='green')
        style.configure('Error.TLabel', font=('Helvetica', 10), foreground='red')
        
        # Configure buttons
        style.configure('Primary.TButton', font=('Helvetica', 11, 'bold'))
        style.configure('Secondary.TButton', font=('Helvetica', 10))
        
    def create_widgets(self):
        """Create and organize all GUI widgets"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="pyEng Language Learning", style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Configuration Frame
        config_frame = ttk.LabelFrame(main_frame, text="Study Configuration", padding="10")
        config_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
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
        
        # Start button
        self.start_button = ttk.Button(config_frame, text="Start Study Session", style='Primary.TButton', 
                                      command=self.start_study_session)
        self.start_button.grid(row=1, column=2, columnspan=2, sticky=(tk.W, tk.E), padx=(0, 20), pady=(10, 0))
        
        # Study Area Frame
        study_frame = ttk.LabelFrame(main_frame, text="Study Area", padding="10")
        study_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        study_frame.columnconfigure(0, weight=1)
        study_frame.rowconfigure(1, weight=1)
        study_frame.rowconfigure(3, weight=1)
        
        # Progress info
        self.progress_label = ttk.Label(study_frame, text="Ready to start study session", style='Info.TLabel')
        self.progress_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        # Korean sentence display
        ttk.Label(study_frame, text="Korean Sentence:", style='Header.TLabel').grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        self.korean_text = scrolledtext.ScrolledText(study_frame, height=4, wrap=tk.WORD, font=('Helvetica', 12))
        self.korean_text.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # English input area
        ttk.Label(study_frame, text="Your English Translation:", style='Header.TLabel').grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
        self.english_input = scrolledtext.ScrolledText(study_frame, height=4, wrap=tk.WORD, font=('Helvetica', 12))
        self.english_input.grid(row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        self.english_input.bind('<Return>', self._on_enter_submit)
        
        # Control buttons
        button_frame = ttk.Frame(study_frame)
        button_frame.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        button_frame.columnconfigure(1, weight=1)
        
        self.submit_button = ttk.Button(button_frame, text="Submit Answer", style='Primary.TButton', 
                                       command=self.submit_answer, state='disabled')
        self.submit_button.grid(row=0, column=0, padx=(0, 10))
        
        self.skip_button = ttk.Button(button_frame, text="Skip", style='Secondary.TButton', 
                                     command=self.skip_sentence, state='disabled')
        self.skip_button.grid(row=0, column=1, padx=(0, 10))
        
        self.end_button = ttk.Button(button_frame, text="End Session", style='Secondary.TButton', 
                                    command=self.end_study_session, state='disabled')
        self.end_button.grid(row=0, column=2)
        
        # Feedback area
        self.feedback_text = scrolledtext.ScrolledText(study_frame, height=3, wrap=tk.WORD, font=('Helvetica', 10))
        self.feedback_text.grid(row=6, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E))
        
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
            self.total_sentences = len(self.study_engine.list_kor)
            
            # Update UI
            self.start_button.config(state='disabled')
            self.submit_button.config(state='normal')
            self.skip_button.config(state='normal')
            self.end_button.config(state='normal')
            self.group_combo.config(state='disabled')
            self.dictionary_combo.config(state='disabled')
            self.mode_combo.config(state='disabled')
            
            # Show first sentence
            self.show_current_sentence()
            
            self.status_var.set(f"Study session started - {self.current_mode.get()} mode")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start study session: {str(e)}")
            
    def show_current_sentence(self):
        """Display the current sentence for study"""
        if self.current_sentence_index < self.total_sentences:
            # Get Korean sentence
            korean_sentence = self.study_engine.list_kor[self.current_sentence_index].strip()
            self.korean_text.delete(1.0, tk.END)
            self.korean_text.insert(1.0, korean_sentence)
            
            # Clear previous input
            self.english_input.delete(1.0, tk.END)
            self.feedback_text.delete(1.0, tk.END)
            
            # Update progress
            progress_text = f"Sentence {self.current_sentence_index + 1} of {self.total_sentences}"
            self.progress_label.config(text=progress_text)
            
            # Focus on input
            self.english_input.focus()
            
        else:
            self.end_study_session()
            
    def submit_answer(self):
        """Submit user's answer for evaluation"""
        if not self.is_studying:
            return
            
        user_answer = self.english_input.get(1.0, tk.END).strip()
        if not user_answer:
            messagebox.showwarning("Warning", "Please enter your answer")
            return
            
        # Get correct answer
        correct_answer = self.study_engine.list_eng[self.current_sentence_index].strip()
        
        # Compare answers (simple comparison for now)
        is_correct = user_answer.lower() == correct_answer.lower()
        
        # Show feedback
        feedback = f"Your answer: {user_answer}\n\n"
        if is_correct:
            feedback += "✅ Correct! Well done!"
            self.feedback_text.config(foreground='green')
        else:
            feedback += f"❌ Incorrect. The correct answer is:\n{correct_answer}"
            self.feedback_text.config(foreground='red')
            
        self.feedback_text.delete(1.0, tk.END)
        self.feedback_text.insert(1.0, feedback)
        
        # Clear the answer input box
        self.english_input.delete(1.0, tk.END)
        
        # Schedule next sentence
        self.root.after(2000, self.next_sentence)
        
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
        self.skip_button.config(state='disabled')
        self.end_button.config(state='disabled')
        self.group_combo.config(state='readonly')
        self.dictionary_combo.config(state='readonly')
        self.mode_combo.config(state='readonly')
        
        # Clear study area
        self.korean_text.delete(1.0, tk.END)
        self.english_input.delete(1.0, tk.END)
        self.feedback_text.delete(1.0, tk.END)
        self.progress_label.config(text="Ready to start study session")
        
        self.status_var.set("Study session ended")
        
        if self.current_sentence_index >= self.total_sentences:
            messagebox.showinfo("Session Complete", "Congratulations! You've completed all sentences in this session.")

    def _on_enter_submit(self, event):
        self.submit_answer()
        return 'break'  # Prevent newline in the input box

def main():
    """Main function to run the GUI application"""
    root = tk.Tk()
    app = PyEngGUI(root)
    
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