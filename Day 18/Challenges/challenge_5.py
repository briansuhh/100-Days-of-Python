from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
colormode(255)
timmy.speed("fastest")
timmy.pensize(1)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(gap):
    for i in range(int(360/gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.right(gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()