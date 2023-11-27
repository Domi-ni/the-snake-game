from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("The snake game")
my_screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

my_screen.listen()
my_screen.onkey(key="Up", fun=snake.up)
my_screen.onkey(key="Down", fun=snake.down)
my_screen.onkey(key="Right", fun=snake.right)
my_screen.onkey(key="Left", fun=snake.left)

game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.set_new_location()
        snake.new_segment()
        score_board.increase_score()

    if snake.head.xcor() > 285 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -285:
        game_is_on = False
        score_board.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
my_screen.exitonclick()
