from turtle import Screen, Turtle
from user_paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

user_paddle = Paddle()

dotted_line = Turtle()
dotted_line.hideturtle()
dotted_line.color("white")
dotted_line.speed("fastest")
dotted_line.width(5)
dotted_line.penup()
dotted_line.goto(x=0, y=290)
dotted_line.rt(90)



for _ in range(18):
    dotted_line.pendown()
    dotted_line.forward(15)
    dotted_line.penup()
    dotted_line.forward(20)















screen.exitonclick()