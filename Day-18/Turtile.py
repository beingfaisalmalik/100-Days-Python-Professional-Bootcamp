from turtle import Turtle,Screen
import random
timmy = Turtle()
screen = Screen()
timmy.shape('arrow')

timmy.color('greenyellow')
timmy.fillcolor('springgreen')
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)
        
def sides(side):
    angle = 360/side
   
    for i in range(side):
        timmy.forward(100)
        timmy.right(angle)
l = ['blue', 'red', 'green', 'yellow', 'cyan','brown','orange','deepskyblue','aqua','teal']

for i in range(3,11):
    timmy.color(random.choice(l))
    sides(i)
    
    
screen.exitonclick()
