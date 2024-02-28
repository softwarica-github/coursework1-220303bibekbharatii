# integration_test_keylogger.py
import unittest
import threading
import time
from keylogger_core import KeyloggerCore
from keylogger_GUI import KeyloggerGUI, run_gui
from keylogger_enhancement import KeyloggerEnhancements

class TestKeyloggerIntegration(unittest.TestCase):
    def setUp(self):
        # Create instances of KeyloggerCore, KeyloggerGUI, and KeyloggerEnhancements
        self.keylogger_core = KeyloggerCore()
        self.gui_thread = threading.Thread(target=run_gui)
        self.gui_thread.start()
        time.sleep(1)  # Allow time for GUI to initialize
        self.keylogger_gui = KeyloggerGUI(root=None)
        self.keylogger_enhancements = KeyloggerEnhancements()

    def tearDown(self):
        # Stop the GUI thread
        self.gui_thread.join()

    def test_gui_and_core_interaction(self):
        # Test if GUI and KeyloggerCore interact as expected
        output_file = "integration_test_keylogs.txt"
        self.keylogger_core.start_keylogger(output_file)
        time.sleep(2)  # Allow time for keylogger to start
        self.keylogger_gui.start_keylogger()
        time.sleep(2)  # Allow time for GUI to process start keylogger
        self.assertTrue(self.keylogger_core.keylogger_thread.is_alive())
        self.assertEqual(self.keylogger_gui.record_button["state"], "disabled")

        self.keylogger_gui.stop_keylogger()
        time.sleep(2)  # Allow time for GUI to process stop keylogger
        self.assertFalse(self.keylogger_core.keylogger_thread.is_alive())
        self.assertEqual(self.keylogger_gui.record_button["state"], "normal")

    def test_enhancements_and_core_interaction(self):
        # Test if KeyloggerEnhancements and KeyloggerCore interact as expected
        output_file = "integration_test_enhancements_keylogs.txt"
        self.keylogger_core.start_keylogger(output_file)
        time.sleep(2)  # Allow time for keylogger to start
        self.keylogger_enhancements.enhance_gui_elements(self.keylogger_gui)
        self.keylogger_gui.start_keylogger()
        time.sleep(2)  # Allow time for GUI to process start keylogger
        self.assertTrue(self.keylogger_core.keylogger_thread.is_alive())
        self.assertEqual(self.keylogger_gui.record_button["state"], "disabled")

        self.keylogger_gui.stop_keylogger()
        time.sleep(2)  # Allow time for GUI to process stop keylogger
        self.assertFalse(self.keylogger_core.keylogger_thread.is_alive())
        self.assertEqual(self.keylogger_gui.record_button["state"], "normal")

if __name__ == "__main__":
    unittest.main()
