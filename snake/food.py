from turtle import Turtle
import random

LOWER_BOUNDARY = -260
UPPER_BOUNDARY = 260
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(LOWER_BOUNDARY, UPPER_BOUNDARY)
        random_y = random.randint(LOWER_BOUNDARY, UPPER_BOUNDARY)
        self.color(random.choice(COLORS))
        self.goto(random_x, random_y)
