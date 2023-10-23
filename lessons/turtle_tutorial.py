"""Practicing with turtle."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()


leo.penup()
leo.goto(-150,-130)
leo.pendown()
leo.color(250,250,250)
leo.speed(50)
leo.hideturtle()

leo.begin_fill()
i: int = 0
while (i<3):
    leo.forward(300)
    leo.left(120)   
    i += 1 
leo.end_fill()


bob: Turtle = Turtle()
bob.color(0,0,0)
bob.penup()
bob.goto(-150,-130)
bob.pendown()
bob.speed(50)
bob.hideturtle()

i: int = 0
while (i<3):
    bob.forward(300)
    bob.left(120)   
    i += 1 

side_len: int = 300
angle: int = 121

i = 0
while (i<33):
    bob.forward(side_len)
    bob.left(angle)   
    i += 1 
    side_len = side_len * 0.96
done()