from turtle import Turtle, Screen
from snake import Snake
import time
screen = Screen()
turtle = Turtle()

turtle.penup()
turtle.shape("circle")


turtle.setpos(x=100,y=0)
turtle2 = Turtle()

turtle2.penup()
turtle2.shape("arrow")


turtle2.setpos(x=100,y=0)
if turtle2.xcor() == turtle.xcor():
    print("attack")
screen.tracer(0)
screen.update()
screen.exitonclick()