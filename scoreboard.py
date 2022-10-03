from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def declare_winner(self):
        if self.r_score > self.l_score:
            winner = "Right Player"
        else:
            winner = "Left Player"
        self.color("red")
        self.goto(0, 0)
        self.write(f"The Winner Is {winner}", align="center", font=("Courier", 30, "bold"))