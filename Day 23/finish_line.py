from turtle import Turtle


class Finishline(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.finish_line()
        self.flag()
        
    def finish_line(self):
        self.goto(-300, 240)
        self.pensize(5)
        self.setheading(0)
        self.pendown()
        self.forward(600)

    def flag(self):
        self.goto(0, 240)
        self.write("🏁       🏁", align="center", font=("Arial", 24, "normal"))
