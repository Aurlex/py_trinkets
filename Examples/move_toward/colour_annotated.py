# Import game_dev from the py_trinkets library
from py_trinkets.g import *

# Function that takes lists of 3 Values, [R, G, B] and interpolates it to another list of different values
# "parameter: datatype" tells python to only accept parameters of that specific type
def colour_interp(col1: list, col2: list, step: int) -> list:
    temp = col1  # making a temporary list of values
    step_val = 255 / step  # If step = 100, step_val = 2.55
    # Step val is 2.55, and it runs 100 times, so equals 255 in the end
    for x in range(step):
        # Updating the list using move_toward(), where temp[] is the value to be moved,
        # col2[] is the value to move to, and step_val is the value to increase by
        temp = [
            move_toward(temp[0], col2[0], step_val),
            move_toward(temp[1], col2[1], step_val),
            move_toward(temp[2], col2[2], step_val),
        ]
        print(temp)


# Call the function and input 2 lists, and an int
colour_interp([0, 0, 0], [255, 255, 255], 100)
