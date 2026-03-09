import turtle as t
import time
from paddle import Paddle
from ball import Ball
from score import ScoreBoard

#loading the screen
screen = t.Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.bgpic("court.gif")
screen.title("Pong!")
screen.tracer(0)
screen.listen()

# #creating a partition line
# brick = t.Turtle(shape ="square")
# brick.penup()
# brick.color("white")
# brick.shapesize(0.60)
# for i in range (-330,330,30):
#     brick.goto(0, i)
#     brick.stamp()

#showing the paddles, ball and scorecard
paddle_1 = Paddle((480,0))
paddle_2 = Paddle((-480,0))
ball = Ball()
scoreboard = ScoreBoard()

#controlling the paddles
screen.onkeypress(fun=paddle_1.up, key="Up")
screen.onkeypress(fun=paddle_1.down, key="Down")
screen.onkeypress(fun=paddle_2.up, key = "w")
screen.onkeypress(fun=paddle_2.down, key = "s")

we_play = True
while we_play:

    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #collisions with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_deflection()

    #collision with paddles
    if (ball.xcor() > 465 and ball.distance(paddle_1) < 50) or \
   (ball.xcor() < -465 and ball.distance(paddle_2) < 50):
        ball.paddle_hit()

    #updating the scoreboard
    if ball.xcor() > 500:
        ball.reset_pos()
        scoreboard.right_scores()
    if ball.xcor() < -500:
        ball.reset_pos()
        scoreboard.left_scores()

    #game ending
    if scoreboard.left_points == 10 or scoreboard.right_points == 10:
        we_play = False
        print("Game ended")

screen.exitonclick()
