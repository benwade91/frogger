from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = -1
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write( f"Score: {self.score}", move=False, align="center", font=('courier', 20, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=('courier', 30, 'bold'))