# Keylogger
A Python-based utility that utilizes the pynput library to capture, format, and record system keyboard inputs to a local file for educational analysis of global event handlers.


# Python Keyboard Event Listener

This project demonstrates how to implement a global event handler in Python using the `pynput` library. It monitors and logs real-time keyboard events (both alphanumeric characters and special function keys) to a local text file for data formatting and event-driven programming analysis.

## Features

- **Global Event Hooking:** Intercepts keyboard events asynchronously across the operating system environment.
- **Timestamped Recording:** Prepends a high-precision date and time stamp to every registered key event.
- **Graceful Termination:** Listens for a specific escape sequence to safely close file handlers and exit the process.

## Prerequisites

- **Python 3.6+**
- **Platform Considerations:** The script contains Windows-specific API calls via `ctypes` to manage window visibility. Adjustments may be required for macOS or Linux environments.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd keyboard-listener
   ```

2. Install the necessary dependencies:
   ```bash
   pip install pynput
   ```

## Usage

Run the script from your terminal or command prompt:

```bash
python listener.py
```

- **Output:** Keystrokes are appended sequentially to a file named `key_log.txt` in the root directory.
- **Exit:** Press the `Esc` key at any time to stop the listener and terminate the application.

## Legal and Ethical Use

This software is provided exclusively for educational research, interface automation prototyping, and input validation analysis. Ensure you have explicit authorization before deploying input monitoring software on any machine.
