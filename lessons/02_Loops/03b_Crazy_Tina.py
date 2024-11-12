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
turtle.setup (width=700, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(1)                           # Make the turtle move as fast, but not too fast. 


forwards = [ 50,30,50,30 ]*50
lefts = [ 45,90,45,90 ]*50

tina.write('Tina was not the Imposter')
for c in range(50):
    tina.forward(c/10)
    tina.tilt(10)




turtle.done()  

