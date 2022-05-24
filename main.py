# Pong Game
# Use "w" and "s" keys to move left paddle
# Use "Up" and "Down" keys to move right paddle


from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        print("contact")
        ball.bounce_x()

    # Detect Collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("contact")
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
