text = "MOVE,(1093, 363)"
x, y = map(int, text.split(',', 1)[1].strip("() ").split(","))

# leftclick = "Clicked+Button.left,(1423, 246)"
# _, button_coords = leftclick.split("+")
# print(_)
# print(button_coords)
# button, coords = button_coords.replace('(', '').replace(')', '').split(",")[:2]

# print(button)  # Output: (1423
# print(coords)  # Output:  246

button_coords = "Button.left,(1423, 246)"
coordinates = button_coords.split(",", maxsplit=1)[1].strip()  # Extracting "(1423, 246)"

print(coordinates)
print("0-----------")
coordinates = "(1423, 246)"
x, y = map(int, coordinates.strip("() ").split(","))

print(x)
print(y)


# print(x)  # Output: 1093
# print(y)  # Output: 363
