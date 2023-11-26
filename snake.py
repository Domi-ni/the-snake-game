from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move_snake(self):

        for index in range(len(self.segments)-1, 0, -1):
            new_y = self.segments[index - 1].ycor()
            new_x = self.segments[index - 1].xcor()
            self.segments[index].goto(x=new_x, y=new_y)
        self.segments[0].forward(20)
