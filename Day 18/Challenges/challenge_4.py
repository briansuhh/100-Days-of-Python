# random walk
from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
colormode(255)

colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Turquoise", "Gray"]
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
    
timmy.pensize(5)
timmy.speed("fastest")

for i in range(200):
    timmy.color(random_color())
    timmy.setheading(random.choice(directions))
    timmy.forward(20)

screen = Screen()
screen.exitonclick()