"""A program first asks user for the number of squares and then draws the sequence of rotated squares. The minimum number of squares is 1.
Move the turtle 200 pixels, The upper left corner of each square is at (0,0). The first square is drawn without any rotation. The second
and the subsequent squares are rotated to the right by the same number of degrees which is 360 divided the number of squares.
"""

import turtle

num_sqr = int(input("Enter the number of squares:"))

pen = turtle.Turtle()
pen.speed(300)

pen.hideturtle()

# for loop to draw the number of squares inputed by the user
for sqr in range(1, num_sqr+1):
    # loop to draw a square
    for i in range(4):
        pen.fd(200)
        pen.rt(90)
    
    # the angle that the next square moves from the previous square
    pen.rt(360/num_sqr)
    
turtle.exitonclick()