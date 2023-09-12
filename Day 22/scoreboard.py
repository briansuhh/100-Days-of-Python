from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        self.setposition(-180, 235)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.setposition(180, 235)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.show_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.show_score()

