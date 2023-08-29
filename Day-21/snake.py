from turtle import Turtle
STARTTING_POSITION = [(0,0),(0,-20),(0,-40)]
class Snake:
    def __init__(self):
       
        self.segments=[]
        self.createsnake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
    def createsnake(self):
        for postion in STARTTING_POSITION:
            self.add_segment(postion)
            
            
            
    def move(self):
        for segment in range((len(self.segments)-1),0,-1):
            x_cor = self.segments[segment-1].xcor()
            y_cor = self.segments[segment-1].ycor()
            self.segments[segment].goto(x_cor,y_cor)
        self.head.fd(20)
   
        
    def check(self):
        if self.head.xcor() > 280 or self.head.ycor() > 280 or self.head.xcor() < -280 or self.head.ycor() < -280:
            print("you Lost")
            return False
        else : return True
    def add_segment(self,position):
            turtle = Turtle()
            turtle.shape('square')
            turtle.color("white")
            turtle.penup()
            turtle.goto(position)
            self.segments.append(turtle)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createsnake()
        self.head = self.segments[0]
    def snakesize(self):
        self.add_segment(self.segments[-1].position())
            
    def checktail(self):
        for segment in self.segments:
            if segment == self.head:
                pass
        if self.head.distance(segment) < 10:
            return False
        else:
            return True      
        
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
         if self.head.heading() != 180:
            self.head.setheading(0)