from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.speed(0)
        self.hideturtle()
        self.goto(-27, 270)
        self.r_score = 0
        self.l_score = 0
        self.write(f"{self.l_score} : {self.r_score}", align="left", font=("Arial", 15, "bold"))

    def update(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align="left", font=("Arial", 15, "bold"))

    def r_goal(self):
        self.r_score += 1
        self.update()

    def l_goal(self):
        self.l_score += 1
        self.update()
