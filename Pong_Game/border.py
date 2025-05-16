import turtle


class Border(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(position)
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=40)
