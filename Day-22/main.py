from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
socre = Score()
screen = Screen()
screen.title("Ping Pong Game")
screen.setup(height=600,width=800)
screen.bgcolor("black")

screen.tracer(0)

screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_ready = True
while game_is_ready:
    time.sleep(0.1)
    screen.update() 
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    if ball.distance(r_paddle) > 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320  :
            ball.bounce_x()
    if ball.xcor() > 380:
        socre.lscore()
        ball.resert()
    if ball.xcor() < -380:
        socre.rscore()
        ball.resert()
screen.exitonclick()