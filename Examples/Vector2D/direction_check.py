from py_trinkets.m import *


def direction(vector):
    if vector.x != 0:
        if Vector2D_RIGHT().x <= vector.x:
            print("X: right")
        else:
            print("X: left")
    else:
        print("X: centre")
    if vector.y != 0:
        if Vector2D_DOWN().x <= vector.y:
            print("Y: down")
        else:
            print("Y: up")
    else:
        print("Y: centre")


velocity = Vector2D(10, 20)
direction(velocity)