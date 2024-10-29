"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 


forwards = [ 50,30,50,30 ]*50
lefts = [ 45,90,45,90 ]*50
colors = ['blue', 'red', 'orange', 'black', ]*50
tina.goto(0,200)
for  i in range(20):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.forward(forward)
    tina.left(left)
    tina.forward(i)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.left(i)
for  i in range(20):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.forward(forward-40)
    tina.left(left-4)
    tina.forward(i)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(20):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.forward(forward-40)
    tina.left(left-4)
    tina.forward(i)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(20):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.forward(forward-40)
    tina.left(left-4)
    tina.forward(i)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(20):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.forward(forward-40)
    tina.left(left-4)
    tina.forward(i)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(20):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.forward(forward-40)
    tina.left(left-4)
    tina.forward(i)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)
for  i in range(200):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.left(left)
    tina.back(forward)
    tina.forward(4)
    tina.left(i)
    tina.forward(4)

turtle.done()  

