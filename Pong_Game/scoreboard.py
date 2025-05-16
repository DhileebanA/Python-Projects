import turtle


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.opponent_score = 0
        self.goto(0, 200)
        self.hideturtle()
        self.color("white")
        self.write(f"{self.opponent_score}  {self.player_score}", align="center", font=("Arial", 40, "normal"))
        self.display = turtle.Turtle()
        self.penup()
        self.display.hideturtle()
        self.display.goto(-20, 255)
        self.display.color("white")
        self.display.write("Computer    Player", align="center", font=("Arial", 20, "normal"))

    def increase_score(self, player):
        if player:
            self.clear()
            self.player_score += 1
            self.write(f"{self.opponent_score}  {self.player_score}", align="center", font=("arial", 40, "normal"))
            self.winner()
        else:
            self.clear()
            self.opponent_score += 1
            self.write(f"{self.opponent_score}  {self.player_score}", align="center", font=("arial", 40, "normal"))
            self.winner()

    def winner(self):
        if self.player_score == 10:
            self.goto(0, 0)
            print(self.write(f"YOU WIN!", align="center", font=("arial", 50, "normal")))
        elif self.opponent_score == 10:
            self.goto(0, 0)
            print(self.write(f"YOU LOSE!", align="center", font=("arial", 50, "normal")))
