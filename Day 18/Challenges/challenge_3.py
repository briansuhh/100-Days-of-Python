# draw triangle up to decagon that changes color every shape
from turtle import Turtle, Screen
import random

timmy = Turtle()

colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Turquoise", "Gray"]

def shapes(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy.right(angle)
        timmy.forward(100)

for sides in range(3, 11):
    timmy.color(random.choice(colors))
    shapes(sides)

screen = Screen()
screen.exitonclick()
