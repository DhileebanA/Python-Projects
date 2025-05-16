import turtle as t
SNAKE_SEG_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 20


class Snake:
    def __init__(self):
        self.all_snake = []
        self.create_snake()
        self.head_of_snake = self.all_snake[0]

    def create_snake(self):
        for num in range(3):
            self.create_snake_body(SNAKE_SEG_POS[num])

    def create_snake_body(self, position):
        snake = t.Turtle(shape="circle")
        snake.penup()
        snake.color("purple")
        snake.goto(position)
        self.all_snake.append(snake)

    def move(self):
        for i in range(len(self.all_snake)-1, 0, -1):
            self.all_snake[i].goto(self.all_snake[i - 1].position())
        self.head_of_snake.forward(MOVEMENT)

    def up(self):
        if self.head_of_snake.heading() != 270:
            self.head_of_snake.setheading(90)

    def down(self):
        if self.head_of_snake.heading() != 90:
            self.head_of_snake.setheading(270)

    def left(self):
        if self.head_of_snake.heading() != 0:
            self.head_of_snake.setheading(180)

    def right(self):
        if self.head_of_snake.heading() != 180:
            self.head_of_snake.setheading(0)
