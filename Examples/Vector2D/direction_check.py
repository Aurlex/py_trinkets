from py_trinkets.m import *

# Remember that in vector coordinates, LEFT = (-1, 0), RIGHT = (1, 0), UP = (0, -1), and DOWN = (0, 1)
facing = Vector2D(-10, 2)


def check_direction(vector: Vector2D):

    get_distance = Vector2D.distance_to

    if get_distance(vector.normalise(), Vector2D_DOWN()) <= 1:
        print("facing down")
    else:
        print("facing up")
    if get_distance(vector.normalise(), Vector2D_RIGHT()) <= 1:
        print("facing right")
    else:
        print("facing left")


check_direction(facing)
