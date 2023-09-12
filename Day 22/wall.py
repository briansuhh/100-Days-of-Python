from turtle import Turtle

TOP_WALL = (-400, 280)
BOTTOM_WALL = (-400, -280)

class Wall(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.create_wall(TOP_WALL)
        self.create_wall(BOTTOM_WALL)
    
    def create_wall(self, position):
        self.penup()
        self.goto(position)
        self.pendown()
        self.forward(800)