from turtle import *
speed('fastest')

def polygon(sides, length, color, width):
    pencolor(color)
    pensize(width)
    for i in range(sides):
        forward(length)
        right(360/sides)

# while True:
    polygon(4, 100, 56, 5)
    goto(400,100)
    polygon(7,100,'blue',20)

hideturtle()
mainloop()