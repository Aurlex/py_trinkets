# Import mathematics from the py_trinkets library
from py_trinkets.m import *

# Create a list of kinematic bodies
kinematic_bodies = []


class KinematicBody(object):  # Create a custom class called KinematicBody
    def __init__(
        self, position=Vector2D_ZERO(), velocity=Vector2D_ZERO()
    ):  # __init__ is run when the object is made
        global kinematic_bodies

        # self.variable is specific to one instance of the class
        # position and velocity are set to the Vector2D() parameter of __init__
        self.position = position
        self.velocity = velocity
        kinematic_bodies.append(
            self
        )  # Add this instance of KinematicBody to the kinematic_bodies list

    def move(self):

        # Take the Vector2D() velocity and add it to the Vector2D() position
        # e.g: position = (0, 0), velocity = (2, 5)
        # postion + velocity = (2, 5)

        self.position += self.velocity


# Creating new instances of KinematicBody called Player and Enemy and setting their positions and velocities
Player = KinematicBody(Vector2D(-10, 0), Vector2D(1, 0))
Enemy = KinematicBody(Vector2D(10, 0), Vector2D(-1, 0))

# Calculate the distance of the Player's position to the Enemy's position using Vector2D.distance_to()
distance = Vector2D.distance_to(Player.position, Enemy.position)
print(distance)


while Player.position.x != Enemy.position.x:  # != means not equal to

    # Looping through the kinematic_bodies list, make each body run it's move() function
    for body in kinematic_bodies:
        KinematicBody.move(body)

    distance = Vector2D.distance_to(Player.position, Enemy.position)
    print(distance)

    # If the Player is touching the Enemy, kill the player
    if distance == 0:
        print("You died!")
        del Player  # Delete the player instance
        break
