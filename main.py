from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(600, 600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameison = True
while gameison:
    screen.update()
    time.sleep(0.1)
    snake.movesnake()
    if snake.head.distance(food) < 15:
        food.foodchange()
        snake.extend1()
        scoreboard.incscore()

    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        gameison = False
        scoreboard.gameover()

    for seg in snake.addturtle:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            gameison = False
            scoreboard.gameover()

screen.exitonclick()
