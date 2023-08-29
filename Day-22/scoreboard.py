from turtle import Turtle,Screen
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.lcore = 0
        self.rsocre = 0
        self.updatescore()
    def updatescore(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lcore, align="center" , font=("Courier", 50, "normal"))
        self.goto(100,200)
        self.write(self.rsocre, align="center" , font=("Courier", 50, "normal"))
        
    def lscore(self):
        self.lcore +=1 
        self.updatescore()
    def rscore(self):
        self.rsocre +=1 
        self.updatescore()
        
        