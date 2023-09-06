# import colorgram

# rgb_colors = []
# colors = colorgram.extract('Day 18/images.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

colors = [(196, 158, 124), (64, 95, 124), (140, 87, 63), (140, 162, 183), (217, 208, 127), (185, 147, 159), (23, 36, 52), (122, 78, 92), (46, 24, 17), (138, 179, 153), (67, 114, 83), (52, 22, 33), (132, 25, 39), (168, 157, 51), (21, 39, 30), (188, 99, 84), (219, 174, 186), (170, 102, 117), (226, 177, 168), (129, 32, 22), (78, 158, 107), (163, 210, 178), (45, 
58, 96), (112, 121, 156), (183, 187, 212), (36, 86, 56)]

import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
timmy.hideturtle()
colormode(255)

for num in range(50, 501, 50):
    timmy.penup()
    timmy.setposition(-250, -250 + num)
    for _ in range(10):
        timmy.pendown()
        print(timmy.position())
        timmy.dot(20, random.choice(colors))
        timmy.penup()
        timmy.forward(50)

screen = Screen()
screen.exitonclick()