# DAILY CODE:
# January 16th, 2025
# Evan M.

import turtle
screen = turtle.Screen()
screen.bgcolor("black") 
draw = turtle.Turtle()

# how to make square
def square(x, y):
    draw.pensize(5)
    draw.pencolor("red")
    draw.penup()
    draw.goto(x, y)
    draw.pendown()
    for i in range(4): 
        draw.forward(50) 
        draw.right(90)

#how to make circle
def circle(cx, cy, radius):
    draw.pensize(8)
    draw.pencolor("turquoise")
    draw.fillcolor("yellow")
    draw.penup()
    draw.goto(cx, cy)
    draw.pendown()
    draw.begin_fill()
    draw.circle(radius)
    draw.end_fill()

#how 2 make tragnle :>
def triangle(tx, ty):
    draw.pensize(5)
    draw.pencolor("lime")
    draw.penup()
    draw.goto(tx, ty)
    draw.pendown()
    for i in range(3): 
        draw.forward(100) 
        draw.right(120)

#how 2 make hexagon
def hexagon(tx, ty):
    draw.pensize(5)
    draw.pencolor("magenta")
    draw.penup()
    draw.goto(tx, ty)
    draw.pendown()
    for i in range(6): 
        draw.forward(130) 
        draw.right(60)

#how 2 make star
def star(tx, ty):
    draw.pensize(5)
    draw.pencolor("yellow")
    draw.penup()
    draw.goto(tx, ty)
    draw.pendown()
    for i in range(5): 
        draw.forward(100) 
        draw.left(72)
        draw.forward(100)
        draw.left(144)

#how 2 make cool
def cool():
    colors = ["red", "orange", "yellow", "lime", "blue", "magenta"]
    draw.penup()
    draw.goto(0, 0)
    draw.pendown()
    draw.pensize(10)
    for i in range(200): 
        draw.forward(i * 4)
        draw.left(92)
        draw.pencolor(colors[i%6])

#call functions
square(30, 40)
square(10, 50)
square (100, 200)
circle(-200, 200, 80)
triangle(200, -200)
hexagon(-200, -100)
star(-100, 100)
cool()

turtle.done() 