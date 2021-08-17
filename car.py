from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 2)
        self.penup()
        self.color_options = ['red', 'blue', 'yellow', 'orange', 'pink', 'green', 'brown', 'purple']
        self.car_speed = .01
        self.paint_car()
        self.place_car()

    def paint_car(self):
        i = random.choice(self.color_options)
        self.color('black', i)

    def place_car(self):
        random_y = random.randint(-10, 10) * 23
        random_x = random.randint(350, 1200)
        self.goto(random_x, random_y)

    def move_car(self):
        current_x = self.xcor()
        current_y = self.ycor()
        if current_x < -400:
            current_x += 800
        self.goto(current_x - 1, current_y)

    def speed_up(self):
        self.car_speed *= 0.7
