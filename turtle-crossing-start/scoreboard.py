from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.penup()
        self.goto(-200, 250)
        self.write(arg=f"LEVEL: {self.score}", move=False, align="center", font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)

    def next_lvl(self):
        self.penup()
        self.goto(-200, 250)
        self.clear()
        self.write(arg=f"LEVEL: {self.score}", move=False, align="center", font=FONT)

