from py_trinkets.m import *

kinematic_bodies = []


class KinematicBody(object):
    def __init__(self, position=Vector2D_ZERO(), velocity=Vector2D_ZERO()):
        global kinematic_bodies

        self.position = position
        self.velocity = velocity
        kinematic_bodies.append(self)

    def move(self):
        self.position += self.velocity


Player = KinematicBody(Vector2D(-10, 0), Vector2D(1, 0))
Enemy = KinematicBody(Vector2D(10, 0), Vector2D(-1, 0))

distance = Vector2D.distance_to(Player.position, Enemy.position)
print(distance)


while Player.position.x != Enemy.position.x:

    for body in kinematic_bodies:
        KinematicBody.move(body)

    distance = Vector2D.distance_to(Player.position, Enemy.position)
    print(distance)

    if distance == 0:
        print("You died!")
        del Player
        break
