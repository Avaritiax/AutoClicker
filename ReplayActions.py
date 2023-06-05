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
for action in actions:
    if action.startswith("MOVE"):
        x, y = map(int, action.split(',', 1)[1].strip("() ").split(","))
        mouse.position = (x,y)
        print(mouse.position)

    # Pause for a short interval between actions (adjust as needed)
    # time.sleep(0.05)

