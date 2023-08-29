from turtle import Turtle,Screen
import random
timmy = Turtle()
screen = Screen()

timmy.pensize(10)
timmy.speed(100)

l = ['blue', 'red', 'green', 'yellow', 'cyan','brown','orange','deepskyblue','aqua','teal']
j = [0,90,180,270]
for i in range(100):
    timmy.pencolor(random.randint(0,256),random.randint(0,256),random.randint(0,256))
    steps = int(20)
    angle = random.choice(j)
    timmy.forward(steps)
    timmy.setheading(angle)
    
screen.exitonclick()