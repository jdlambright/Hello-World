from turtle import Turtle

STARTING_POSITIONS = [(350, -40), (350, -20), (350,0), (350, 20), (350, 40)]

class Paddle:
    def __init__(self):
        self.segments = []


    def create_paddle(self):
        for position in STARTING_POSITIONS:
            paddle = Turtle("square")
            paddle.color("white")
            paddle.penup()
            paddle.goto(position)

