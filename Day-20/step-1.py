from turtle import Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
flag =True
while flag:
    screen.update()
    time.sleep(0.5)
    snake.move()
    snake.size()
    flag = snake.check()
    
    
        
        
        
screen.exitonclick()


    
