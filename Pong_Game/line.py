import turtle


class Line(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.new_y_up = 5
        self.new_y_down = -5
        self.pencolor("white")
        self.pensize(5)
        self.penup()
        self.hideturtle()
        self.goto(0, 5)
        while self.ycor() < 300:
            self.pendown()
            self.new_y_up += 20
            self.goto(0, self.new_y_up)
            self.penup()
            self.new_y_up += 10
            self.goto(0, self.new_y_up)
        self.goto(0, -5)
        while self.ycor() > -300:
            self.pendown()
            self.new_y_down -= 20
            self.goto(0, self.new_y_down)
            self.penup()
            self.new_y_down -= 10
            self.goto(0, self.new_y_down)
