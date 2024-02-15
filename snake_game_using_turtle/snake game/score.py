from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('score.txt') as file:
            self.highest_score = int(file.read())
        self.up()
        self.hideturtle()
        self.goto(-90, 270)
        self.color('white')
        self.update()
    def game_over(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('score.txt',mode='w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update()
    def increase_score(self):
        self.score+=1
        self.update()
    def update(self):
        self.clear()
        self.write(f'score: {self.score} Highest score:{self.highest_score}', align="left", font=("Sans serif", 15, "bold"))