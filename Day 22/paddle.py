from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(position)

    def go_up(self):
        if self.ycor() < 220:
            self.goto(self.xcor(), self.ycor() + 23)

    def go_down(self):
        if self.ycor() > -220: 
            self.goto(self.xcor(), self.ycor() - 23)