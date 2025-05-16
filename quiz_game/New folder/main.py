import turtle as t
import random

player_turtle = object
no_of_front = 1
is_on = True
all_turty = []
colors = ["pink", "orange", "purple", "blue", "green", "red"]
y_positions = [-100, -60, -20, 20, 60, 100]
screen = t.Screen()
screen.setup(width=600, height=500)
user_input = screen.textinput(title="Turtle Race", prompt=f"Which color of turtle do you pick?\n{colors}")
is_spell_correct = True

for turtle_index in range(6):
    turty = t.Turtle(shape="turtle")
    turty.penup()
    turty.color(colors[turtle_index])
    if turty.color()[0] == user_input:
        player_turtle = turty
    turty.goto(x=-280, y=y_positions[turtle_index])
    all_turty.append(turty)

while is_spell_correct:
    if user_input in colors:
        while is_on:
            for turty in all_turty:
                turty.forward(random.randint(0, 10))
                if turty.xcor() > 275:
                    winner = turty
                    is_on = False
                    is_spell_correct = False
                    for pos_turty in all_turty:
                        if pos_turty.xcor() > player_turtle.xcor():
                            no_of_front += 1
                    if winner.color()[0] == user_input:
                        print(f"You've Won! The {winner.color()[0]} color turtle is the Winner!")
                    else:
                        print(f"You've got {no_of_front} place! The {winner.color()[0]} color turtle is the Winner!"
                              f"Better Luck next time")
                    break
    else:
        user_input = screen.textinput(title="Turtle Race", prompt=f"Please check the spelling and type:\n{colors}")

screen.exitonclick()
