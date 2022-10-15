from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#348feb")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(position)
        self.right(90)

    def move_right(self):
        x = self.xcor() + 60
        self.goto(x, self.ycor())

    def move_left(self):
        x = self.xcor() - 60
        self.goto(x, self.ycor())