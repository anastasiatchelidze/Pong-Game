from turtle import Screen, colormode
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

colormode(255)

game_is_on = True

while game_is_on:

    time.sleep(0.08)
    ball.move()
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()
        ball.change_color()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.change_color()

    # Detect the ball missing the paddles
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_score += 1
        scoreboard.update_scores()
    elif ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_score += 1
        scoreboard.update_scores()

    # Determining the winner
    if scoreboard.r_score >= 3 or scoreboard.l_score >= 3:
        game_is_on = False
        scoreboard.declare_winner()

screen.exitonclick()