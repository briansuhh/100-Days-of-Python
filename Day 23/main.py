import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from finish_line import Finishline

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")  
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
finish_line = Finishline()

screen.listen()
screen.onkeypress(player.move, "Up")
screen.onkeypress(player.starting_position, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_cars()
    car_manager.create_car()

    # if car collides with player
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False    
    
    # if player reaches finish line
    if player.is_at_finish_line():
        player.starting_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()

