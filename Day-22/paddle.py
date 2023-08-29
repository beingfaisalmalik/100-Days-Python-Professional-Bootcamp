from turtle import Turtle,Screen
class Paddle(Turtle):
    def __init__(self,xcordinate,ycordinate):
        super().__init__()
        self.shape("square")
        self.width(20)
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.color("white")
        self.goto(y=ycordinate,x=xcordinate)
 
    


    def go_up(self):
        new_y = self.ycor()+ 20
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    
        