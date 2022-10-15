from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#a3a3a3")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_score_lives()

    def update_score_lives(self):
        self.clear()
        self.goto(-250, 270)
        self.write('Score:' + str(self.score) + '    Lives:' + str(self.lives), align="left", font=("Courier-serif", 20, "bold"))

    def point(self):
        self.score += 5
        self.update_score_lives()