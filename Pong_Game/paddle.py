import turtle as t
SPEED_OF_PLAYER = 10
SPEED_OF_OPPONENT = 2


class Paddles(t.Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(position)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.edge_up = (0, 0)
        self.edge_down = (0, 0)

    def paddle_edge_up(self):
        self.edge_up = (self.xcor(), self.ycor() + 25)
        return self.edge_up

    def paddle_edge_down(self):
        self.edge_down = (self.xcor(), self.ycor() - 25)
        return self.edge_down

    def edge(self):
        self.paddle_edge_up()
        self.paddle_edge_down()

    def move_play_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + SPEED_OF_PLAYER)

    def move_opp_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + SPEED_OF_OPPONENT)

    def move_play_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - SPEED_OF_PLAYER)

    def move_opp_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - SPEED_OF_OPPONENT)
