from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_tracker = 0
        self.penup()
        self.color("White")
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score_tracker}", align="center", font=('Arial', 15, 'normal'))
        self.hideturtle()

    def increase_score(self):
        self.score_tracker += 1
        self.clear()
        self.write(arg=f"Score: {self.score_tracker}", align="center", font=('Arial', 15, 'normal'))


