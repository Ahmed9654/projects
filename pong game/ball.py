from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.speed(0)
        self.goto(0,0)
        self.x_direction = 10
        self.y_direction = 10
        self.ball_speed = .1

    def move(self):

        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x,new_y)

    def bounce_wall(self):
        self.y_direction *= -1

    def bounce_paddle(self):
        self.x_direction *= -1
        self.ball_speed *= 0.9
    def reset(self):
        self.goto(0,0)
        self.bounce_paddle()
        self.ball_speed = 0.1