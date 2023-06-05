text = "MOVE,(1093, 363)"
x, y = map(int, text.split(',', 1)[1].strip("() ").split(","))

leftclick = "Clicked+Button.left,(1423, 246)"
_, button_coords = leftclick.split("+")
print(_)
print(button_coords)
button, coords = button_coords.replace('(', '').replace(')', '').split(",")[:2]

print(button)  # Output: (1423
print(coords)  # Output:  246




print(x)  # Output: 1093
print(y)  # Output: 363
