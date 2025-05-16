import turtle as t
import line
import border
import paddle
import scoreboard
import time
from ball import Ball

WIDTH = 1280
HEIGHT = 720

screen = t.Screen()
screen.listen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("DHILIP'S PONG GAME")
screen.tracer(0)
l_paddle = paddle.Paddles((-350, 0))
r_paddle = paddle.Paddles((350, 0))

ball = Ball()
score = scoreboard.Scoreboard()

border_up = border.Border((0, 300))
border_down = border.Border((0, -300))

line = line.Line()

screen.onkeypress(r_paddle.move_play_up, "Up")
screen.onkeypress(r_paddle.move_play_down, "Down")

on = True
while on:
    time.sleep(0.01)
    screen.update()
    ball.movement()

    # Opponent Movement(Auto)
    if ball.ycor() > l_paddle.ycor():
        l_paddle.move_opp_up()
    elif ball.ycor() < l_paddle.ycor():
        l_paddle.move_opp_down()

    # Detect wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.speed("fastest")
        ball.setheading(360 - ball.heading())
        ball.speed("normal")

    # Detect paddle
    if 330 < ball.xcor() < r_paddle.xcor() and r_paddle.distance(ball) < 50 or \
            -330 > ball.xcor() > l_paddle.xcor() and l_paddle.distance(ball) < 50:
        ball.speed("fastest")
        ball.setheading(180 - ball.heading())
        ball.speed("normal")
        if ball.xcor() > 0:
            if ball.distance(r_paddle.paddle_edge_up()) < 20 and ball.ycor() >= r_paddle.paddle_edge_up()[1] or \
                    ball.distance(r_paddle.paddle_edge_down()) < 20 and ball.ycor() <= r_paddle.paddle_edge_down()[1]:
                ball.speed("fastest")
                ball.setheading(ball.heading() * -1)
                ball.speed("normal")
        elif ball.xcor() < 0:
            if ball.distance(l_paddle.paddle_edge_up()) < 20 and ball.ycor() >= l_paddle.paddle_edge_up()[1] or \
                     ball.distance(l_paddle.paddle_edge_down()) < 20 and ball.ycor() >= l_paddle.paddle_edge_down()[1]:
                ball.speed("fastest")
                ball.setheading(ball.heading() * -1)
                ball.speed("normal")

    # Track Scoreboard
    if score.player_score < 10 or score.opponent_score < 10:
        if ball.xcor() > 390:
            score.increase_score(False)
            ball.ball_reset()
            if score.player_score >= 3:
                on = False
        elif ball.xcor() < -390:
            score.increase_score(True)
            ball.ball_reset()
            if score.opponent_score >= 3:
                on = False
    else:
        break
screen.exitonclick()
