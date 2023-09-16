from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        x_pos = random.randint(-270, 270)
        y_pos = random.randint(-270, 270)
        self.setposition(x_pos, y_pos)
      