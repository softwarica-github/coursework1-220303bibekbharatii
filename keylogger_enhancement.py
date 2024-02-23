# keylogger_enhancements.py

import tkinter as tk
from tkinter import ttk

class KeyloggerEnhancements:
    @staticmethod
    def enhance_gui_elements(gui):
        # Set a modern theme for a sleek appearance
        gui.themed_master.set_theme("plastik")

        # Configure custom styles for buttons
        gui.themed_master.style.configure("AccentButton.TButton", font=('Helvetica', 14, 'bold'), foreground='white', background='#3498db', padding=10)

        # Create a frame for a clear and consistent layout
        form_frame = ttk.Frame(gui.themed_master)
        form_frame.pack(padx=20, pady=20)

        # Record Keylogs Button
        record_label = ttk.Label(form_frame, text="Record Keylogs:")
        record_label.grid(row=0, column=0, padx=10, pady=10)
        gui.record_button = ttk.Button(form_frame, text="Start", command=gui.start_keylogger, style="AccentButton.TButton")
        gui.record_button.grid(row=0, column=1, padx=10, pady=10)

        # Stop Keylogger Button
        stop_label = ttk.Label(form_frame, text="Stop Keylogger:")
        stop_label.grid(row=1, column=0, padx=10, pady=10)
        gui.stop_button = ttk.Button(form_frame, text="Stop", command=gui.stop_keylogger, style="AccentButton.TButton")
        gui.stop_button.grid(row=1, column=1, padx=10, pady=10)

        # Control Mouse Button
        mouse_label = ttk.Label(form_frame, text="Control Mouse:")
        mouse_label.grid(row=2, column=0, padx=10, pady=10)
        gui.mouse_button = ttk.Button(form_frame, text="Control", command=gui.control_mouse, style="AccentButton.TButton")
        gui.mouse_button.grid(row=2, column=1, padx=10, pady=10)

        # Control Keyboard Button
        keyboard_label = ttk.Label(form_frame, text="Control Keyboard:")
        keyboard_label.grid(row=3, column=0, padx=10, pady=10)
        gui.keyboard_button = ttk.Button(form_frame, text="Control", command=gui.control_keyboard, style="AccentButton.TButton")
        gui.keyboard_button.grid(row=3, column=1, padx=10, pady=10)

        # Center-align buttons
        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        # Additional refinements
        gui.themed_master.title("Enhanced Keylogger Interface")
