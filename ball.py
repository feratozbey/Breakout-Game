from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#7d7f82")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.x_move = -3
        self.y_move = -5
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def x_bounce(self):
        self.x_move *= -1

    def y_bounce(self):
        self.y_move *= -1

    def reset_position(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.move_speed = 0.1
        self.x_bounce()