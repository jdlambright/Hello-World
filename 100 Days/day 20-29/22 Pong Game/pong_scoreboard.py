from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier",80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 180)
        self.write(f" {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 180)
        self.write(f" {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

