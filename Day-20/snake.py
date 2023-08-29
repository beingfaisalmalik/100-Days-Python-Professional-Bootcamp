from turtle import Turtle
STARTTING_POSITION = [0,-20,-40]
class Snake:
    def __init__(self):
       
        self.segments=[]
        self.createsnake()
        
    def createsnake(self):
        for i in range(3):
            turtle = Turtle()
            turtle.shape('square')
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=STARTTING_POSITION[i],y=0)
            self.segments.append(turtle)
            
            
    def move(self):
        for segment in range((len(self.segments)-1),0,-1):
            x_cor = self.segments[segment-1].xcor()
            y_cor = self.segments[segment-1].ycor()
            self.segments[segment].goto(x_cor,y_cor)
        self.segments[0].fd(20)
    def size(self):
        turtle = Turtle()
        turtle.shape('square')
        turtle.color("white")
        turtle.penup()
        t = self.segments[-1].xcor()
        turtle.goto(x=t-20,y=0)
        self.segments.append(turtle)
        
    def check(self):
        if self.segments[0].xcor() > 280 or self.segments[0].ycor() > 280 or self.segments[0].xcor() < -280 or self.segments[0].ycor() < -280:
            print("you Lost")
            return False
        else : return True
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
         if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)