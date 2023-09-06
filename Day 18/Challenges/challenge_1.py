# make a square
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

for i in range(4):
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()