# make a dashed line
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("arrow")
timmy.color("red")

for _ in range(30):
    timmy.down()
    timmy.forward(5)
    timmy.up()
    timmy.forward(5)

screen = Screen()
screen.exitonclick()