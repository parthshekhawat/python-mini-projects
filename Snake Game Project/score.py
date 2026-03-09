from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Comic Sans MS', 14, 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-10,275)
        self.show_score()
        

    def show_score(self):
        self.write(f"SCORE : {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align = ALIGNMENT, font = FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(f"{str(self.high_score)}")
        self.score = 0
        self.clear()
        self.show_score()
        
