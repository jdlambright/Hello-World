from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.left(90)
        self.penup()
        self.reset()


    def go_up(self):
        self.forward(MOVE_DISTANCE)


    def reset(self):
        self.goto(STARTING_POSITION)


    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
