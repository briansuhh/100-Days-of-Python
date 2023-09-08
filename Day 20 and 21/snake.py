from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

class Snake():
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)
    
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].setposition(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)
        
    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

# to make a class inheritance
class Turtlee(Snake):
    def __init__(self) -> None:
        super().__init__() # this line inherits all the methods and attributes of the class snake

    # to modify and add something to a method
    def up(self):
        super().up() # this line inherits the method up of snake 
        print("I just want to add something from this method.")
    
    def hide(self):
        print("This method is only available to the Turtle class")