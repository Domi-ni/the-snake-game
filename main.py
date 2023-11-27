from turtle import Screen
from snake import Snake
from food import Food
import time


my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("The snake game")
my_screen.tracer(0)

snake = Snake()
food = Food()

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
    if snake.head.distance(food) < 13:
        food.set_new_location()
        snake.new_segment()


my_screen.exitonclick()
