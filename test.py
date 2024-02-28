# test_keylogger_core.py
import unittest
import os
import threading
from keylogger_core import KeyloggerCore

class TestKeyloggerCore(unittest.TestCase):
    def setUp(self):
        self.keylogger_core = KeyloggerCore()

    def tearDown(self):
        self.keylogger_core = None

    def test_keylogger_initialization(self):
        # Verify that the keylogger thread is initialized correctly
        output_file = "test_keylogs.txt"
        self.keylogger_core.start_keylogger(output_file)
        self.assertTrue(self.keylogger_core.keylogger_thread.is_alive())

    def test_keylogger_termination(self):
        # Verify that the keylogger thread is terminated correctly
        output_file = "test_keylogs.txt"
        self.keylogger_core.start_keylogger(output_file)
        self.keylogger_core.stop_keylogger()
        self.assertFalse(self.keylogger_core.keylogger_thread.is_alive())

    def test_key_logs_removal(self):
        # Verify that key logs file is removed successfully
        output_file = "test_keylogs.txt"
        # Ensure the key logs file exists before removal
        open(output_file, 'w').close()
        self.keylogger_core.remove_key_logs(output_file)
        self.assertFalse(os.path.exists(output_file))

if __name__ == "__main__":
    unittest.main()
