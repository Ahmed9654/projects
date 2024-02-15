from turtle import Turtle,Screen
import time

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVING_SPEED = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def add_segment(self,position):
        snake = Turtle('square')
        snake.color('white')
        snake.up()
        snake.setposition(position)
        self.segments.append(snake)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())
    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

    def move(self):

        for seg in range(len(self.segments) - 1, 0, -1):
                self.segments[seg].goto(self.segments[seg - 1].xcor(), self.segments[seg - 1].ycor())
        self.head.forward(MOVING_SPEED)