# keylogger_gui.py

import tkinter as tk
from tkinter import ttk
from keylogger_core import KeyloggerCore

class KeyloggerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Keylogger Interface")

        style = ttk.Style()
        style.theme_use('clam')  # You can experiment with other themes like 'default', 'vista', etc.

        style.configure("TButton", padding=10, font=("Arial", 12))
        style.configure("TLabel", font=("Arial", 14, "bold"))
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TButton", foreground="#ffffff", background="#007acc")
        style.map("TButton", background=[('active', '#005580')])

        frame = ttk.Frame(master, style="TFrame")
        frame.pack(padx=20, pady=20)

        self.record_button = ttk.Button(frame, text="Record Keylogs", command=self.start_keylogger)
        self.record_button.grid(row=0, column=0, padx=10, pady=10)

        self.stop_button = ttk.Button(frame, text="Stop Keylogger", command=self.stop_keylogger)
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)
        self.stop_button["state"] = tk.DISABLED  # Initially disable stop button

        self.mouse_button = ttk.Button(frame, text="Control Mouse", command=self.control_mouse)
        self.mouse_button.grid(row=1, column=0, padx=10, pady=10)

        self.keyboard_button = ttk.Button(frame, text="Control Keyboard", command=self.control_keyboard)
        self.keyboard_button.grid(row=1, column=1, padx=10, pady=10)

        self.keylogger_core = KeyloggerCore()

    def start_keylogger(self):
        output_file = "keylogs.txt"  # You can modify this to allow user input for the output file
        self.keylogger_core.start_keylogger(output_file)
        self.record_button["state"] = tk.DISABLED
        self.stop_button["state"] = tk.NORMAL

    def stop_keylogger(self):
        self.keylogger_core.stop_keylogger()
        self.record_button["state"] = tk.NORMAL
        self.stop_button["state"] = tk.DISABLED

    def control_mouse(self):
        # Add your mouse control logic here
        pass

    def control_keyboard(self):
        # Add your keyboard control logic here
        pass

def run_gui():
    root = tk.Tk()
    app = KeyloggerGUI(root)
    root.mainloop()
