# keylogger_cli.py

import argparse
from keylogger_core import KeyloggerCore
from keylogger_GUI import run_gui

def run_cli():
    parser = argparse.ArgumentParser(description="Keylogger with GUI")
    parser.add_argument("--start", action="store_true", help="Start the keylogger")
    parser.add_argument("--stop", action="store_true", help="Stop the keylogger")

    args = parser.parse_args()
    keylogger_core = KeyloggerCore()

    if args.start:
        print("Starting keylogger...")
        output_file = "keylogs.txt"  # You can modify this to allow user input for the output file
        keylogger_core.start_keylogger(output_file)
    elif args.stop:
        print("Stopping keylogger...")
        keylogger_core.stop_keylogger()
    else:
        print("Please provide a valid option. Use --help for more information.")

    run_gui()  # Run the GUI after processing CLI arguments

if __name__ == "__main__":
    run_cli()
