import turtle as t

quad_SIZE = 300

class Border:
    def __init__(self):
        super().__init__()
        self.stamp = t.Turtle("square")
        self.stamp.hideturtle()
        self.stamp.penup()
        self.stamp.color('grey')

        for i in range(-quad_SIZE + 10, quad_SIZE - 10, 22):
            self.draw(-quad_SIZE + 5, i)
            self.draw(quad_SIZE - 10, i)
            self.draw(i, quad_SIZE - 5)
            self.draw(i, -quad_SIZE + 10)

    def draw(self,x,y):
        self.stamp.goto(x,y)
        self.stamp.stamp()







