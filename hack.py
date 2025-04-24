#with count
"""import pyautogui
import webbrowser
import time
import pyperclip

# 🚀 Ask user for input
number = input("Enter the phone number (with country code, e.g. 91XXXXXXXXXX): ").strip()
message = input("Enter the message to send: ").strip()
repeat_count = int(input("How many times to send the message?: "))

# 📲 Open WhatsApp Web with target chat
url = f"https://web.whatsapp.com/send?phone={number}&text="
webbrowser.open(url)

# 🕒 Wait for WhatsApp Web to load (adjust if needed)
print("Loading WhatsApp Web... Please wait 15 seconds.")
time.sleep(15)

# 💬 Send messages very fast
for i in range(1, repeat_count + 1):
    msg = f"{message} {i}"  # Example: "hi 1", "hi 2"
    pyperclip.copy(msg)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    print(f"Sent: {msg}")
    time.sleep(0.1)  # 🧨 Super fast! Can reduce to 0.1 if stable"""

#without count
import pyautogui
import webbrowser
import time
import pyperclip

# 🚀 Ask user for input
number = input("Enter the phone number (with country code, e.g. 91XXXXXXXXXX): ").strip()
message = input("Enter the message to send: ").strip()
repeat_count = int(input("How many times to send the message?: "))

# 📲 Open WhatsApp Web with target chat
url = f"https://web.whatsapp.com/send?phone={number}&text="
webbrowser.open(url)

# 🕒 Wait for WhatsApp Web to load (adjust if needed)
print("Loading WhatsApp Web... Please wait 15 seconds.")
time.sleep(15)

# 💬 Send messages very fast
for i in range(repeat_count):
    pyperclip.copy(message)  # Copy the original message
    pyautogui.hotkey("ctrl", "v")  # Paste the message
    pyautogui.press("enter")  # Press Enter to send
    print(f"Sent: {message}")  # Print out the message sent
    time.sleep(0.1)  # 🧨 Super fast! Can reduce to 0.1 if stable
