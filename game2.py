from random import randint
import pgzrun

WIDTH = 1000
HEIGHT = 500

class Player(Actor):
    speed = 5

class Enemy(Actor):
    speed = 4

class Fruit(Actor):
    x = randint(50, WIDTH-50)
    y = randint(50, HEIGHT-50)

    def relocate(self):
        self.x = randint(50, WIDTH-50)
        self.y = randint(50, HEIGHT-50)

