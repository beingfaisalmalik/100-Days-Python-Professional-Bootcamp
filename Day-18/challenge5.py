from turtle import Turtle,Screen
import random
timmy = Turtle()
screen = Screen()

F = 10
tup = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
while True:
    timmy.color(0,0,0)
    timmy.circle(50)
    timmy.tiltangle(360)
    timmy.left(10)
    F +=1
    
    