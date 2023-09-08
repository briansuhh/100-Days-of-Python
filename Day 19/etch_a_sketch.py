from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def forward():
    timmy.forward(10)

def backward():
    timmy.backward(10)

def rotate_clockwise():
    timmy.right(10)

def rotate_counter():
    timmy.left(10)
    
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkeypress(fun=forward, key="w")
screen.onkeypress(fun=backward, key="s")
screen.onkeypress(fun=rotate_clockwise, key="d")
screen.onkeypress(fun=rotate_counter, key="a")
screen.onkey(fun=clear, key="c")
screen.exitonclick()