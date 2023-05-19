from pynput import mouse
import keyboard
def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

def on_click(x, y, button, pressed):
    action = "Clicked" if pressed else "Released"
    print(f"{action} at ({x}, {y}) with {button}")

def on_scroll(x, y, dx, dy):
    if dy > 0:
        print(f"Scrolled up at ({x}, {y})")
    else:
        print(f"Scrolled down at ({x}, {y})")

# Create a listener for mouse actions
with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
