import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


dhil = t.Turtle()
screen = t.Screen()
t.colormode(255)
i = 0
dhil.speed("fastest")


def draw(size_of_gap):
    for _ in range(int(700 / size_of_gap)):
        dhil.color(random_color())
        dhil.circle(100)
        dhil.setheading(dhil.heading() + size_of_gap)


draw(5)

screen.exitonclick()
