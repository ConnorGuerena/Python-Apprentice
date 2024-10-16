"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.color('orange')
tina.speed(0)
for i in range(999):
    tina.forward(50)
    tina.left(90)
    tina.forward(50)
    tina.back(i/5)

turtle.done()