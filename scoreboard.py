from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 15, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_tracker = 0
        with open("high_score.txt") as high_score:
            self.new_high_score = int(high_score.read())
        self.penup()
        self.color("White")
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score_tracker} High Score:{self.new_high_score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score_tracker} High Score:{self.new_high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score_tracker += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score_tracker > self.new_high_score:
            self.new_high_score = self.score_tracker
            with open("high_score.txt", mode="w") as high_score:
                high_score.write(str(self.new_high_score))
        self.score_tracker = 0
        self.update_scoreboard()

    def game_over(self):
        self.update_scoreboard()
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGN, font=FONT)
