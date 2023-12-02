from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title(titlestring="Pong Game")
screen.listen()

screen.tracer(0)

ball = Ball()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
score = ScoreBoard()

screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

game_is_on = True
count = 0
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with y-axis screen edge
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right and left paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320 or
            ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reverse_position()
        score.left_player_point()

    if ball.xcor() < -380:
        ball.reverse_position()
        score.right_player_point()

screen.exitonclick()
