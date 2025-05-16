from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
i = 3
colour = ["red", "green", "blue", "yellow", "pink", "violet", "orange"]

while i < 10:
    tim.color(colour[i-3])
    angle = 360 / i
    j = 0
    while j < i:
        tim.right(angle)
        tim.forward(100)
        j += 1
    i += 1

screen.exitonclick()
