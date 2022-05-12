# Import mathematics from the py_trinkets library
from py_trinkets.m import *

# Function to print the direction components of a vector


def direction(vector):
    if vector.x != 0:  # Direction cannot be 0
        # Vector2D_RIGHT() is a vector with the value of (1, 0)
        if Vector2D_RIGHT().x <= vector.x:
            print("X: right")
        else:
            print("X: left")
    else:
        print("X: centre")
    if vector.y != 0:  # Direction cannot be 0
        # Vector2D_DOWN() is a vector with the value of (0, 1)
        if Vector2D_DOWN().x <= vector.y:
            print("Y: down")
        else:
            print("Y: up")
    else:
        print("Y: centre")


velocity = Vector2D(10, 20)
direction(velocity)
