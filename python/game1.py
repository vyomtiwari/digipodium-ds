import pgzrun
from random import randint
# screen size
WIDTH = 1000
HEIGHT = 500
 
# OBJECTS

p = Actor('hero')
e = Actor('enemy')
c = Actor('fruit')
 
# configs

c.x = randint(50, WIDTH-50)
c.y = randint(50, HEIGHT-10)
p.x = 400
p.y = 400


# drawing on screen

def draw():
    screen.clear()
    p.draw()
    e.draw()
    c.draw()
def update(dt):
    if keyboard.left:
        p.x -=5
    if keyboard.right:
        p.x +=5
    if keyboard.down:
        p.y +=5
    if keyboard.up:
        p.y -=5


# enemy tracks player
    if p.x > e.x:
        e.x += 2
    if p.x < e.x:
        e.x -= 2
    if p.y > e.y:
        e.y += 2
    if p.y < e.y:
        e.y -= 2
     

#game loop

pgzrun.go()
