from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.speed(0)
        self.shapesize(stretch_len=5)
        self.color('white')
        self.left(90)
        self.goto(position)

    def move_up(self):
        self.forward(25)

    def move_down(self):
        self.back(25)
