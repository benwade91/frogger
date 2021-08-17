from turtle import Turtle


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.goto(0, -280)

    def jump(self):
        self.forward(20)

    def restart(self):
        self.goto(0, -280)