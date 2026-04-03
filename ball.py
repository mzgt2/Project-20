from turtle import Turtle

base_speed = 15
multiplier = 1.2
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(0,0)
        self.dx = base_speed
        self.dy = base_speed
        self.speed("normal")

    def move(self):
        new_x = (self.xcor() + self.dx)

        new_y = (self.ycor() + self.dy)
        if new_y >= 280 or new_y <= -280:
            self.dy = -self.dy
        new_position = (new_x, new_y)

        self.goto(new_position)
    def bounce_x(self):

        self.dx = -self.dx * multiplier

    def reset_position(self):
        self.penup()
        self.dx = base_speed
        self.dy = base_speed
        self.dx *= -1
        self.goto(0,0)
