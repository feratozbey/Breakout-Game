from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

# Constants
GAME_ON = True
BRICK_ROWS = 2
BRICK_PER_ROW = 14

# Screen configuration
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=700)
screen.title("Breakout")

# Objects on the screen
paddle = Paddle((0, -320))
ball = Ball()
scoreboard = Scoreboard()
# Creating bricks
bricks = []
brick_x = -260
brick_y = 250

# Creates and aligns bricks
for i in range(BRICK_ROWS):
    brick_y -= 30
    for j in range(BRICK_PER_ROW):
        brick_x += 35
        bricks.append(Brick((brick_x, brick_y)))
    brick_x = -260

# Assigns functions to 'right' and 'left' arrows.
screen.listen()
screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")


while GAME_ON:
    screen.update()
    ball.move()

    # Paddle and ball collision
    if ball.distance(paddle) <= 63.5 and -299 >= ball.ycor() > -301:
        ball.y_bounce()

    # Wall and paddle collision
    if -290 >= ball.xcor() or ball.xcor() >= 285:
        ball.x_bounce()
    elif ball.ycor() >= 340:
        ball.y_bounce()

    # Ball and bricks collision
    for brick in bricks:
        if ball.distance(brick) <= 20 and abs(ball.ycor() - brick.ycor()) <= 15:
            brick.hideturtle()

            # To move bricks to nearest out of screen location, need to figure out if the collided brick is on the left
            # or right of the screen. 'xcor_sign' Variable will help to figure out what side of screen the brick is. If
            # it is in the middle it will accept it as it is on the right side of screen.
            try:
                xcor_sign = (brick.xcor())/abs(brick.xcor())
            except ZeroDivisionError:
                xcor_sign = +1
            brick.goto(xcor_sign*320, brick.ycor())
            ball.y_bounce()
            scoreboard.point()
            scoreboard.update_score_lives()

    # Paddle misses ball
    if ball.ycor() <= -330:
        ball.reset_position()
        scoreboard.lives -= 1
        scoreboard.update_score_lives()

    # End of game
    # Win
    if scoreboard.score == len(bricks)*5:
        ball.hideturtle()
        scoreboard.clear()
        scoreboard.write('You Win!!!', align='left', font=("Courier-serif", 30, "bold"))
        time.sleep(2)
        screen.bye()

    # Lose
    if scoreboard.lives == 0:
        ball.hideturtle()
        scoreboard.clear()
        scoreboard.write('You Lost!!!', align='left', font=("Courier-serif", 30, "bold"))
        time.sleep(2)
        screen.bye()

screen.exitonclick()
