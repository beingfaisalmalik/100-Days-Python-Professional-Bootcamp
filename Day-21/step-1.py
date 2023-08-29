from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
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
    if not snake.check():
        score.reset()
        snake.reset()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.snakesize()
        score.IncreaseScore()
    if not snake.checktail():
        score.reset()
        
    
        
        
        
screen.exitonclick()


    
