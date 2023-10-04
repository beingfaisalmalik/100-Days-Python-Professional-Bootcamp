from turtle import Turtle,Screen
import random

screen = Screen()
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
flag = False
user_bet = screen.textinput(title='Make your bet', prompt='Which Turtle will win')
screen.setup(width=500,height=400)
y = -70
turtles = []
for i in range(0,6):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[i])
    timmy.penup()
    timmy.goto(x=-250,y=y)
    turtles.append(timmy)
    y +=30

if user_bet:
    flag = True
i =0

while flag:
    for t in turtles:
        if t.xcor() > 230:
            flag = False
            winiingcolor = t.pencolor()
            if winiingcolor == user_bet:
                print("userWon")
            else :
                print("userloss")
            
        r_distance = random.randint(0,10)
        t.forward(r_distance)
    


screen.exitonclick()