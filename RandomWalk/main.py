from random import choice, randint
import turtle as t


dhil = t.Turtle()
angle = [0, 90, 180, 270]
color = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen',]
dhil.pensize(10)
dhil.speed('fastest')
t.colormode(255)
screen = t.Screen()
screen.bgcolor("black")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


for i in range(501):
    dhil.forward(20)
    dhil.setheading(choice(angle))
    dhil.color(random_color())


screen.exitonclick()
