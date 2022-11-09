from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.title("TURTLE RACE")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = ""
starting_y = -70
starting_x = -240
ending_x = 230
all_turtles = []


def get_user_bet():
    global user_bet
    user_bet = screen.textinput(title="Make your bet",
                                prompt=f"Which turtle will win the race? Enter a color: {', '.join(colors)}")


def create_racers():
    for i in range(len(colors)):
        racer_y = starting_y + (30 * i)
        racer = Turtle(shape="turtle")
        racer.penup()
        racer.color(colors[i])
        racer.goto(x=starting_x, y=racer_y)
        all_turtles.append(racer)


def race():
    global all_turtles
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            race_end_prompt = "Would you like to play again? 'y' or 'n': "
            race_end_title = ""
            if winner == user_bet:
                race_end_title = "YOU WON! 🏆"
            else:
                race_end_title = "You lost! 😭"
            race_again = screen.textinput(title=race_end_title, prompt=race_end_prompt).lower()
            if race_again == 'n':
                global race_on
                race_on = False
                return
            else:
                all_turtles = []
                screen.clearscreen()
                get_user_bet()
                create_racers()

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


get_user_bet()

if user_bet != "":
    race_on = True

create_racers()
while race_on:
    race()

screen.exitonclick()
