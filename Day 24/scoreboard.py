from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())

        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.scoreboard()
    
    def scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.scoreboard()

    def reset(self):
        if self.score > self.high_score: 
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.scoreboard()    