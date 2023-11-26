from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("The snake game")

snake = Turtle("square")
snake.color("white")
snake.shapesize(stretch_len=3)








my_screen.exitonclick()