from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from pong_scoreboard import Scoreboard
import time

#set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("grey")
screen.title("PONG")
screen.tracer(0)

# #make dotted line
# dotted_line = Turtle()
# dotted_line.hideturtle()
# dotted_line.color("white")
# dotted_line.speed("fastest")
# dotted_line.width(5)
# dotted_line.penup()
# dotted_line.goto(x=0, y=290)
# dotted_line.rt(90)
#
#
# for _ in range(18):
#     dotted_line.pendown()
#     dotted_line.forward(15)
#     dotted_line.penup()
#     dotted_line.forward(20)



#place paddles and ball on screen
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Right")
screen.onkey(r_paddle.go_down, "Left")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()








screen.exitonclick()