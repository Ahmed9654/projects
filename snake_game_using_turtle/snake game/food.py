from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.speed(0)
        self.shapesize(stretch_wid=.5,stretch_len=.5) # make it half width and length
        self.color('blue')
        self.up()
        self.refresh()

    def refresh(self):

        self.setposition(random.randint(-280,280), random.randint(-280,280))
