from turtle import Turtle,Screen
import random
timmy = Turtle()
screen = Screen()

timmy.shape('arrow')
l = ['blue', 'red', 'green', 'yellow', 'cyan','brown','orange','deepskyblue','aqua','teal']
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.fd(300)
timmy.setheading(0)
numberofdtos = 100
for dot in range(1,numberofdtos+1):
    timmy.dot(20,"red")
    timmy.fd(50)
    if dot %10 == 0:
        timmy.setheading(90)
        timmy.fd(50)
        timmy.penup()
        timmy.setheading(180)
        timmy.color(random.choice(l))
        
        timmy.fd(500)
        timmy.setheading(0)
