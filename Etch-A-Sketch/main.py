import turtle as t


def move_forward():
    dhil.forward(10)


def move_backward():
    dhil.back(10)


def turn_left():
    dhil.left(10)


def turn_right():
    dhil.right(10)


def clear():
    dhil.reset()


dhil = t.Turtle()
screen = t.Screen()

screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()
