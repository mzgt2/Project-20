from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
l_paddle = Paddle((-450, 0))
r_paddle = Paddle((450, 0))



ball = Ball()
screen = Screen()
screen.tracer(0)
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Pong Game")

screen.listen()

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.comp_up, "Up")
screen.onkey(r_paddle.comp_down, "Down")
game_time = True
scoreboard = Scoreboard()
scoreboard.divider()
scoreboard.set_score()
while game_time:
    screen.update()
    time.sleep(0.1)
    #r_paddle.comp_movement()

    ball.move()
    if ball.distance(l_paddle) < 45 and ball.xcor() > -450:
            ball.bounce_x()



    if ball.distance(r_paddle) < 45 and ball.xcor() < 435:
            ball.bounce_x()


    if ball.xcor() > 500:
        scoreboard.score_1()
        ball.reset_position()
        scoreboard.divider()
    if ball.xcor() < -500:
        scoreboard.score_2()
        ball.reset_position()
        scoreboard.divider()
screen.exitonclick()
