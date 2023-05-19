from pynput import mouse
import keyboard
import os

#MOVE = Mouse Movement X,Y

recording = False 
recordAction = []

def start_recording():
    global recording
    recordAction.clear()  # Clear the previous recorded actions
    recording = True

def stop_recording():
    global recording
    recording = False
    #print(recordAction)
    print("Saved")
    save_actions_to_file()

def save_actions_to_file():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "recorded_actions.txt")
    with open(file_path, "w") as file:
        for action in recordAction:
            file.write(action + "\n")
    print("Recorded actions saved to:", file_path)

def on_move(x, y):
    if recording:
        print("B")
        recordAction.append(f"MOVE,({x}, {y})")

def on_click(x, y, button, pressed):
    if recording:
        action = "Clicked" if pressed else "Released"
        recordAction.append(f"{action}+{button},({x}, {y})")

def on_scroll(x, y, dx, dy):
    if dy > 0:
        recordAction.append(f"SUP,({x}, {y})")
    else:
        recordAction.append(f"SUD,({x}, {y})")

        
keyboard.add_hotkey('q', start_recording)
keyboard.add_hotkey('e', stop_recording)
# Create a listener for mouse actions
with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()


