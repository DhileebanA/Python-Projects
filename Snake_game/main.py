# Import Package
import time
import turtle as t
import snake as s
from food import Food
from scoreboard import ScoreBoard
import borderLine

# Object creating:
border = borderLine.Border()
snake = s.Snake()
food = Food()
score = ScoreBoard()

# Create a Window:
screen = t.Screen()
screen.setup(width=1920, height=1080, startx=0, starty=0)
screen.bgcolor("white")
screen.title("Dhilip's Snake Game")
screen.tracer(0)
screen.listen()

# Key aligner:
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Run the Game:
run_snake = True
while run_snake:
    # Movement
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Detect the food:
    if snake.head_of_snake.distance(food) < 16:
        food.refresh()
        snake.create_snake_body(snake.all_snake[-1].position())
        score.increase_score()

    # Detect the wall:
    if snake.head_of_snake.xcor() > 280 or snake.head_of_snake.xcor() < -280 or \
            snake.head_of_snake.ycor() > 280 or snake.head_of_snake.ycor() < -280:
        run_snake = False
        score.game_over()

    # Detect the tail:
    for body in snake.all_snake:
        if snake.head_of_snake.distance(body) < 10:
            if body == snake.head_of_snake:
                pass
            else:
                run_snake = False
                score.game_over()


screen.exitonclick()
