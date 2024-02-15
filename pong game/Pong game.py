from turtle import Screen
from Paddle import Paddle
from ball import Ball
from score import Score
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)

screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)


game_is_on = True
while game_is_on:
    time.sleep(.03)
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_wall()
    if ball.xcor() > 320 and ball.distance(right_paddle) < 60 or ball.xcor() < -320 and ball.distance(left_paddle) < 60:
        ball.bounce_paddle()
    # right miss
    if ball.xcor() > 380:
        ball.reset()
        score.l_goal()

    if ball.xcor() < -380:
        ball.reset()
        score.r_goal()

    screen.update()

screen.exitonclick()
