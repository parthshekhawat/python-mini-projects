import turtle as t

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
FACING = {'UP' : 90,
        'DOWN' : 270,
        'LEFT' : 180,
        'RIGHT' : 0}

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        square = t.Turtle(shape="square")
        square.color("white")
        square.penup()
        square.speed("fast")
        square.goto(position)
        self.segments.append(square)

    def extend(self):
        self.add_segment(self.segments[-1].position()) #adding the segment at the position of the last segment

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):  # (start at last of self.segments, end at 0, and this happens while taking a step of -1), can't use keyword args here
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != FACING["DOWN"]:
            self.head.setheading(FACING["UP"])

    def down(self):
        if self.head.heading() != FACING["UP"]:
            self.head.setheading(FACING["DOWN"])

    def right(self):
        if self.head.heading() != FACING["LEFT"]:
            self.head.setheading(FACING["RIGHT"])

    def left(self):
        if self.head.heading() != FACING["RIGHT"]:
            self.head.setheading(FACING["LEFT"])

