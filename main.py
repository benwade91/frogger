from turtle import Screen
from frog import Frog
from car import Car
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.title("Frogger")
screen.tracer(0)


frog = Frog()
cars = []

# initial traffic
for _ in range(10):
    cars.append(Car())


screen.listen()
screen.onkey(frog.jump, "Up")

game_on = True

while game_on:
    screen.update()
    time.sleep(cars[0].car_speed)
    for car in cars:
        car.move_car()
        if car.distance(frog) < 20:
            game_on = False

    # detects successful crossing
    if frog.ycor() > 250:
        frog.restart()
        cars.append(Car())
        for car in cars:
            car.speed_up()



screen.exitonclick()