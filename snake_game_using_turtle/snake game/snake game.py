from turtle import Screen
from score import Score
from food import Food
from snake import Snake
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(600, 600)
screen.title('My snake game')
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key='Up',fun=snake.up)
screen.onkey(key='Down',fun=snake.down)
screen.onkey(key='Left',fun=snake.left)
screen.onkey(key='Right',fun=snake.right)

game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    snake.move()

    # detect eating the food
    if snake.head.distance(food) < 20:
        food.refresh()
        score.increase_score()
        snake.extend_snake()
    if snake.head.xcor() > 280 or snake.head.ycor() > 290 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.game_over()
        snake.reset()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            snake.reset()





screen.exitonclick()