import keyboard
import os
import signal
from pynput.mouse import Controller
import time
# MOVE = Mouse Movement X,Y
# SUP = Scroll Up
# SUD = Scroll Down
# Clicked+Button.left
# Released+Button.left

recording = False
recordAction = []
mouse = Controller()
print_mouse_position = False

def start_recording():
    global recording, print_mouse_position
    #without sleep, instantly record 
    time.sleep(0.05)
    recordAction.clear()  # Clear the previous recorded actions
    recording = True
    print_mouse_position = True

    # Record the mouse position and actions continuously until recording is stopped
    while recording:
        record_mouse_position()
        
        # Check if 'e' key is pressed to stop recording
        if keyboard.is_pressed('e'):
            stop_recording()
            break

def stop_recording():
    global recording, print_mouse_position
    recording = False
    print_mouse_position = False
    print("Saved")
    save_actions_to_file()
    # Get the process ID (PID) of the current Python process
    current_pid = os.getpid()

    # Terminate the Python process to end program
    os.kill(current_pid, signal.SIGTERM)

def save_actions_to_file():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "recorded_actions.txt")
    with open(file_path, "w") as file:
        for action in recordAction:
            file.write(action + "\n")
    print("Recorded actions saved to:", file_path)

def record_mouse_position():
    if recording:
        x, y = mouse.position
        if print_mouse_position:
            print(f"Mouse position: ({x}, {y})")
        recordAction.append(f"MOVE,({x}, {y})")

def on_click(x, y, button, pressed):
    if recording:
        action = "Clicked" if pressed else "Released"
        recordAction.append(f"{action}+{button},({x}, {y})")

def on_scroll(x, y, dx, dy):
    if recording:
        action = "SUP" if dy > 0 else "SUD"
        recordAction.append(f"{action},({x}, {y})")

keyboard.add_hotkey('q', start_recording)

# Start the keyboard listener
keyboard.wait('esc')

# Save the recorded actions before exiting
save_actions_to_file()