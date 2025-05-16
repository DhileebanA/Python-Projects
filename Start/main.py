from turtle import Turtle, Screen

amai = Turtle()
screen = Screen()

amai.shape("turtle")
for _ in range(15):
    amai.forward(10)
    amai.penup()
    amai.forward(5)
    amai.pendown()


screen.exitonclick()
