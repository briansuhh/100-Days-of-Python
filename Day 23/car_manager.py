from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.move_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        min_distance = 50
        random_chance = random.randint(1, 3)

        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2, outline=10)
            new_car.color(random.choice(COLORS))
            new_car.goto(320, random.randint(-200, 220))

            for car in self.cars:
                if car.distance(new_car) < min_distance:
                    new_car.clear()
                    return

            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_speed)  

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
