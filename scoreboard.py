from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 15, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_tracker = 0
        self.penup()
        self.color("White")
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score_tracker}", align=ALIGN, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score_tracker += 1
        self.clear()
        self.write(arg=f"Score: {self.score_tracker}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGN, font=FONT)

