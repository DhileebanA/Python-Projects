import turtle as t
import random
BALL_SIZE = 1
BALL_SPEED = 5
BALL_TOWARDS_ANGLE = [45, 135, 225, 315]


class Ball(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(BALL_SIZE)
        self.penup()
        self.color("white")
        self.setheading(45)

    def movement(self):
        self.forward(BALL_SPEED)

    def ball_reset(self):
        self.home()
        self.setheading(BALL_TOWARDS_ANGLE[random.randint(0, 3)])


