from turtle import Turtle, Screen
import random 
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.sccore =0
       
        with open(file='Day-21/data.txt') as file:
          n = file.read()
          self.highscore = int(n)
          
        self.penup()
        self.color("white")
        self.goto(0,250)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.sccore} HighScore: {self.highscore} ",align="center", font=("arial",24,"bold"))
        
    def reset (self):
        if self.sccore > self.highscore:
            self.highscore = self.sccore
            with open(file='Day-21/data.txt', mode="w") as file:
                file.write(str(self.sccore))
        self.sccore = 0
        self.update()
        
    def IncreaseScore(self):
        self.sccore += 1
        self.update()
        
        