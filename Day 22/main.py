from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard

RIGHT_PADDLE = (370, 0)
LEFT_PADDLE = (-380, 0)

game_speed = ['easy', 'average', 'hard']

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

wall = Wall()
r_paddle = Paddle(RIGHT_PADDLE)
l_paddle = Paddle(LEFT_PADDLE)
ball = Ball()
scoreboard = Scoreboard()

userChoice = screen.textinput(title="Adjust the game speed", prompt="Type your choice (easy|average|hard)")

if userChoice in game_speed:
    game_is_on = True

if userChoice == 'easy':
    ball.move_speed(0.2)
elif userChoice == 'average':
    ball.move_speed(0.4)
elif userChoice == 'hard':
    ball.move_speed(0.6)

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

while game_is_on:
    screen.update()
    ball.move()

    # detect the colission of ball and wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
    
    # detect the colission of ball and right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350:
        ball.bounce_x() 
        # ball.move_speed += 0.1
        
    # detect the colission of ball and left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()
        # ball.move_speed += 0.1

    # detect if the ball goes out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
