from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.left_points = 0
        self.right_points = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-125,250)
        self.write(self.left_points, align=ALIGNMENT, font=FONT)

        self.goto(125,250)
        self.write(self.right_points, align=ALIGNMENT, font=FONT)

    def left_scores(self):
        self.left_points += 1
        self.update_score()
        
    def right_scores(self):
        self.right_points += 1
        self.update_score()







