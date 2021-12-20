from tim import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scores import Score
import time

screen = Screen()
scores = Score()


screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("white")
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scores.left_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scores.right_point()



screen.exitonclick()
