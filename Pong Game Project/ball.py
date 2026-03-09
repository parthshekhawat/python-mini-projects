from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()

        self.move_x = 10
        self.move_y = 10
        self.ball_speed = 0.036

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def wall_deflection(self):
        self.move_y *= -1

    def paddle_hit(self):
        self.move_x *= -1
        self.ball_speed *= 0.98

    def reset_pos(self):
        self.goto(0,0)

        self.ball_speed = 0.036
        self.move_x *= -1