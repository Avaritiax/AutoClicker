import keyboard
import os
from pynput.mouse import Button, Controller as MouseController
import time

#MOVE = Mouse Movement X,Y
#SUP = Scroll Up
#SUD = Scroll Down
#Clicked+Button.left 
#Released+Button.left  
#Clicked+Button.right
#Released+Button.right

filename = "recorded_actions.txt"
# Check if the file exists
if os.path.exists(filename):
    # Open the file in read mode
    with open(filename, "r") as file:
        # Read the lines of the file and remove any leading/trailing whitespace
        actions = [line.strip() for line in file.readlines()]
        
    # Print the actions
    print(actions)
else:
    print("File does not exist.")

#MOVE = Mouse Movement X,Y
#SUP = Scroll Up
#SUD = Scroll Down
#Clicked+Button.left 
#Released+Button.left  

mouse = MouseController()

paused = False  # Flag to indicate if the script is paused

def toggle_pause():
    global paused
    paused = not paused
    print("Script paused" if paused else "Script resumed")

# Register a hotkey to toggle pause/resume
keyboard.add_hotkey('p', toggle_pause)

for action in actions:
    if paused:
        time.sleep(0.1)  # Pause the script execution when it's paused
        continue

    if action.startswith("MOVE"):
        x, y = map(int, action.split(',', 1)[1].strip("() ").split(","))
        mouse.position = (x, y)
        print(mouse.position)
    elif action.startswith("SUD"):
        mouse.scroll(0, -1)
    elif action.startswith("SUP"):
        mouse.scroll(0, 1)
    elif action.startswith("Clicked"):
        _, button_coords = action.split("+")
        if button_coords.startswith("Button.left"):
            coordinates = button_coords.split(",", maxsplit=1)[1].strip()
            x, y = map(int, coordinates.strip("() ").split(","))
            mouse.position = (x, y)
            mouse.press(Button.left)
        elif button_coords.startswith("Button.right"):
            coordinates = button_coords.split(",", maxsplit=1)[1].strip()
            x, y = map(int, coordinates.strip("() ").split(","))
            mouse.position = (x, y)
            mouse.press(Button.right)
    elif action.startswith("Released"):
        _, button_coords = action.split("+")
        if button_coords.startswith("Button.left"):
            coordinates = button_coords.split(",", maxsplit=1)[1].strip()
            x, y = map(int, coordinates.strip("() ").split(","))
            mouse.position = (x, y)
            mouse.release(Button.left)
        elif button_coords.startswith("Button.right"):
            coordinates = button_coords.split(",", maxsplit=1)[1].strip()
            x, y = map(int, coordinates.strip("() ").split(","))
            mouse.position = (x, y)
            mouse.release(Button.right)
    # Pause for a short interval between actions (adjust as needed)
    # time.sleep(0.05)
