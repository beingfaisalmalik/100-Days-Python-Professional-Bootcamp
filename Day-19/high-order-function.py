from turtle import Turtle,Screen

timmy = Turtle()
screen = Screen()


def forward():
    timmy.fd(10)
    
def backwar():
    timmy.backward(10)
    
def anticlockwise():
        timmy.left(10)
    
def clockwise():
    timmy.right(10)
    
def clr():
    timmy.clear()
    timmy.penup()
    timmy.home()
screen.listen()
screen.onkey(key='w',fun=forward)
screen.onkey(key='s',fun=backwar)
screen.onkey(key='a',fun=anticlockwise)
screen.onkey(key='d',fun=clockwise)
screen.onkey(key='c',fun=clr)
screen.exitonclick()