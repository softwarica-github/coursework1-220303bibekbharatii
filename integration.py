import unittest
import threading
import time
from keylogger_core import KeyloggerCore
from keylogger_GUI import KeyloggerGUI, run_gui
from keylogger_enhancement import KeyloggerEnhancements

class TestKeyloggerIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create instances of KeyloggerCore, KeyloggerGUI, and KeyloggerEnhancements
        cls.keylogger_core = KeyloggerCore()
        cls.gui_thread = threading.Thread(target=run_gui)
        cls.gui_thread.start()
        time.sleep(1)  # Allow time for GUI to initialize
        cls.keylogger_gui = KeyloggerGUI(root=None)
        cls.keylogger_enhancements = KeyloggerEnhancements()

    @classmethod
    def tearDownClass(cls):
        # Stop the GUI thread
        cls.gui_thread.join()

    def setUp(self):
        # Ensure keylogger is not running at the beginning of each test
        self.keylogger_core.stop_keylogger()
        self.keylogger_gui.stop_keylogger()

    def tearDown(self):
        # Ensure keylogger is stopped after each test
        self.keylogger_core.stop_keylogger()
        self.keylogger_gui.stop_keylogger()

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
