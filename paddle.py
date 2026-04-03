from turtle import Turtle
import random

UP = 90
DOWN = 270
MOVE_DISTANCE = 40

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)
        self.comp = [self.comp_up, self.comp_down]
    def up(self):
        current_y = self.ycor()
        new_y = current_y + MOVE_DISTANCE
        if current_y < 240:
            self.goto(self.xcor(), new_y)

    def down(self):
        current_y2 = self.ycor()
        new_y2 = current_y2 - MOVE_DISTANCE
        if current_y2 > -240:
            self.goto(self.xcor(), new_y2)

    def comp_up(self):
        comp_y = self.ycor()
        new_comp_y = comp_y + MOVE_DISTANCE
        if new_comp_y < 280:
            self.goto(self.xcor(), new_comp_y)


    def comp_down(self):
        comp_y2 = self.ycor()
        new_comp_y2 = comp_y2 - MOVE_DISTANCE
        if new_comp_y2 > -280:
            self.goto(self.xcor(), new_comp_y2)
    def comp_movement(self):
        choice = random.choice(self.comp)
        return choice()
