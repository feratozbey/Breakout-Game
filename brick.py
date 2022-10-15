from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("#752206")
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=0.5)
        self.right(90)
        self.penup()
        self.goto(position)