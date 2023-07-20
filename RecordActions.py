import keyboard
import os
from pynput.mouse import Controller, Listener
import time

recording = False
recordAction = []
mouse = Controller()
print_mouse_position = False

def start_recording():
    global recording, print_mouse_position
    time.sleep(0.05)
    recordAction.clear()
    recording = True
    print_mouse_position = True

    mouse_listener = Listener(on_click=on_click, on_scroll=on_scroll)
    mouse_listener.start()

    while recording:
        record_mouse_position()
        
        if keyboard.is_pressed('e'):
            stop_recording()
            break

def stop_recording():
    global recording, print_mouse_position
    recording = False
    print_mouse_position = False
    print("Saved")
    save_actions_to_file()

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
        x, y = mouse.position
        print(x,y)
        recordAction.append(f"{action}+{button},({x}, {y})")

def on_scroll(x, y, dx, dy):
    if recording:
        action = "SUP" if dy > 0 else "SUD"
        recordAction.append(f"{action},({x}, {y})")

keyboard.add_hotkey('q', start_recording)
keyboard.wait('esc')
save_actions_to_file()
#qeqeqeqeqe