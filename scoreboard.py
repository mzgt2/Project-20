from turtle import Turtle

FONT = ("Arial", 80, "bold")
ALIGN = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.player_1_score = 0
        self.player_2_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.setheading(270)


    def divider(self):
        self.goto(0, 300)
        for item in range(50):

            self.pensize(3)
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
    def set_score(self):
        self.color("white")
        self.penup()
        self.goto(-60,160)
        self.write(f"{self.player_1_score}", align=ALIGN, font=FONT)
        self.goto(60, 160)
        self.write(f"{self.player_2_score}", align=ALIGN, font=FONT)

    def score_1(self):
        self.clear()
        self.player_1_score += 1
        self.penup()
        self.goto(-60, 160)
        self.write(f"{self.player_1_score}", align=ALIGN, font=FONT)
        self.goto(60,160)
        self.write(f"{self.player_2_score}", align=ALIGN, font=FONT)

    def score_2(self):
        self.clear()
        self.player_2_score += 1
        self.penup()
        self.goto(-60,160)
        self.write(f"{self.player_1_score}", align=ALIGN, font=FONT)
        self.goto(60, 160)
        self.write(f"{self.player_2_score}", align=ALIGN, font=FONT)
