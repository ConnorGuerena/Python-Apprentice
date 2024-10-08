"""Flaming Ninja Star

This program already works; run it to see what it does. 
Then change it to make it draw a different pattern. 
"""

import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]


def getNextColor(i):
    return colors[i % len(colors)]

turtle.setup (width=6000, height=6000) 
window = turtle.Screen()

baseSize = 20  # the size of the black part of the star
flameSize = 30  # the length of the flaming arms

t = turtle.Turtle() 

t.shape("turtle") 

t.width(2) 

t.speed(0) 

for i in range(25):
    t.pencolor(getRandomColor())

    t.fillcolor(getRandomColor()) 
   
    t.begin_fill()

    t.forward(34) 

    t.left(45) 

    t.forward(flameSize) 

    t.right(30) 

    t.forward(flameSize) 

    t.right(42) 
 
    t.forward(i)

    t.end_fill()

t.hideturtle() 

turtle.done() 
