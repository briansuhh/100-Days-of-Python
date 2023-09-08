import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Dash Betting Showdown")
screen.bgcolor("black")

turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-125, -75, -25, 25, 75, 125]

for i in range(6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[i])
    timmy.setposition(-230, y_position[i])
    turtles.append(timmy)

userChoice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if userChoice in colors:
    is_race_on = True

winner = ''
while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor() 

            text_turtle = Turtle()
            text_turtle.hideturtle()
            text_turtle.color("white")

            text_content = f"The winner is {winner}."
            text_font = ("Arial", 15, "normal") 

            if userChoice == winner:
                text_turtle.write("You win!" + text_content, align="center", font=text_font)
            else:
                text_turtle.write("You lose." + text_content, align="center", font=text_font)

screen.mainloop()






