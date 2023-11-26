import time
from turtle import Turtle, Screen


def turn_lef():
    snake_segments[0].left(90)


my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("The snake game")
my_screen.listen()
my_screen.tracer(0)

initial_position = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []
for position in initial_position:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    snake_segments.append(segment)

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    for index in range(len(snake_segments)-1, 0, -1):
        new_y = snake_segments[index - 1].ycor()
        new_x = snake_segments[index - 1].xcor()
        snake_segments[index].goto(x=new_x, y=new_y)
    snake_segments[0].forward(20)
    my_screen.onkey(key="w", fun=turn_lef)

my_screen.exitonclick()
