from turtle import Turtle
import random


class Food(Turtle):
    x_position = random.randint(-275, 275)
    y_position = random.randint(-275, 275)
    random_location = (x_position, y_position)
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        x_position = random.randint(-275, 275)
        y_position = random.randint(-275, 275)
        random_location = (x_position, y_position)
        self.goto(random_location)

    def set_new_location(self):
        x_position = random.randint(-275, 275)
        y_position = random.randint(-275, 275)
        random_location = (x_position, y_position)
        self.goto(random_location)