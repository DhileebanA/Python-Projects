import turtle

BORDER_BOUNDARY = [(295, 295), (295, -295), (-295, -295), (-295, 295)]


class Border(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.border = turtle.Turtle(visible=False)
        self.border.speed("fastest")
        self.border.pensize(5)
        self.border.pencolor("black")
        self.border.penup()
        self.border.goto(-295, 295)
        self.border.pendown()
        for num in range(4):
            self.border.goto(BORDER_BOUNDARY[num])
