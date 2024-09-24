# drawing a square by using a turtle object and rotating an object 90 degrees to the right

import turtle

pen = turtle.Turtle()
pen.setposition(0,0)
for _ in range(4):
    pen.forward(100)  
    pen.right(90)    

turtle.exitonclick()


