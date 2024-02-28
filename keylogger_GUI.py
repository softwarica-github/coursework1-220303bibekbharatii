import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from keylogger_core import KeyloggerCore

class KeyloggerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Keylogger Interface")

        # Use a modern theme
        style = ttk.Style()
        style.theme_use('clam')  # You can experiment with other themes like 'default', 'vista', etc.

        # Configure custom styles for buttons
        style.configure("Accent.TButton", font=("Arial", 14, "bold"), foreground="white", background="#3498db", padding=10)
        style.map("Accent.TButton", background=[('active', '#005580')])

        frame = ttk.Frame(master, style="TFrame")
        frame.pack(padx=20, pady=20)

        # Record Keylogs Button
        self.record_button = ttk.Button(frame, text="Record Keylogs", command=self.start_keylogger,
                                        style="Accent.TButton")
        self.record_button.grid(row=0, column=0, padx=15, pady=15)

        # Stop Keylogger Button
        self.stop_button = ttk.Button(frame, text="Stop Keylogger", command=self.stop_keylogger,
                                      style="Accent.TButton")
        self.stop_button.grid(row=0, column=1, padx=15, pady=15)
        self.stop_button["state"] = tk.DISABLED  # Initially disable stop button

        # Remove Key Logs Button
        self.remove_logs_button = ttk.Button(frame, text="Remove Key Logs", command=self.remove_key_logs,
                                             style="Accent.TButton")
        self.remove_logs_button.grid(row=1, column=0, padx=15, pady=15)

        # Control Mouse Button
        self.mouse_button = ttk.Button(frame, text="Control Mouse", command=self.control_mouse,
                                       style="Accent.TButton")
        self.mouse_button.grid(row=1, column=1, padx=15, pady=15)

        # Control Keyboard Button
        self.keyboard_button = ttk.Button(frame, text="Control Keyboard", command=self.control_keyboard,
                                          style="Accent.TButton")
        self.keyboard_button.grid(row=2, column=0, padx=15, pady=15)

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

    def remove_key_logs(self):
        output_file = "keylogs.txt"  # You can modify this to allow user input for the output file
        self.keylogger_core.remove_key_logs(output_file)
        # Update: Add logic to update GUI or display a message if needed

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

# Uncomment the line below to test the enhanced GUI
# run_gui()
