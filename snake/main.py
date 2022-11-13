from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# FUNCTIONALITY TO ADD???
#   store history of high scores????

SCREEN_W_H = 600
QUADRANT_W_H = int(SCREEN_W_H/2)
WALL_LOWER_BOUNDARY = QUADRANT_W_H * -1
WALL_UPPER_BOUNDARY = QUADRANT_W_H


screen = Screen()
screen.setup(width=SCREEN_W_H, height=SCREEN_W_H)
screen.bgcolor("black")
screen.title("i'm a snaaaaaake")
screen.tracer(0)
play_game = True
is_game_over = False

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.movement_control, "space")


def play_snake():
    global is_game_over
    speed = 0.1
    screen.update()
    time.sleep(speed)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        if scoreboard.score >= 10 and scoreboard.score % 10 == 0:
            speed -= 0.01

    # detect collision with wall
    if snake.head.xcor() > WALL_UPPER_BOUNDARY or snake.head.xcor() < WALL_LOWER_BOUNDARY or snake.head.ycor() > \
            WALL_UPPER_BOUNDARY or snake.head.ycor() < WALL_LOWER_BOUNDARY:
        is_game_over = True
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_over = True
            scoreboard.game_over()


def snake_it_up():
    global play_game
    while not is_game_over:
        play_snake()
    play_again = screen.textinput(title="", prompt="Would you like to play again? 'y' or 'n': ").lower()
    if play_again == 'n':
        play_game = False


while play_game:
    snake_it_up()


screen.exitonclick()
