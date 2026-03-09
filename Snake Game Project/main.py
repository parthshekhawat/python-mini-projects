import turtle as t
import time
from snake import Snake
from food import Food
from score import ScoreBoard

#setting up the screen
screen = t.Screen()
screen.bgpic("grass.gif")
screen.setup(width = 620, height = 620)
screen.title("Snake")
screen.tracer(0)
screen.bgcolor("black")


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

playing_game = True


while playing_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #catching the food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    #touching the walls
    if snake.head.xcor() > 256 or snake.head.xcor() < -256 or snake.head.ycor() > 256 or snake.head.ycor() < -256:
        scoreboard.reset_score()
        playing_game = False
        scoreboard.game_over()

    #collision with tail
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            scoreboard.reset_score()
            playing_game = False
            scoreboard.game_over()

screen.exitonclick()

