import turtle as t
import random

t.colormode(255)

hirst = t.Turtle()

rgb_colors = [(9, 48, 97), (202, 105, 138), (233, 88, 37), (56, 70, 37), (155, 39, 52),
              (240, 130, 60), (63, 42, 35), (0, 74, 106), (249, 157, 48), (108, 65, 112),
              (163, 163, 64), (255, 190, 54), (236, 136, 196), (157, 54, 157), (25, 125, 25),
              (175, 188, 75), (3, 122, 154), (25, 50, 100), (150, 200, 200), (220, 175, 30),
              (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205)]

x = -325
y = -300
total_dots = 100


def make_dot():
    hirst.dot(20, random.choice(rgb_colors))


def move_forward():
    hirst.forward(50)


def next_row():
    hirst.speed("fastest")
    hirst.setheading(90)
    hirst.forward(50)
    hirst.setheading(180)
    hirst.forward(500)
    hirst.setheading(0)
    hirst.speed("slowest")


def make_painting():
    hirst.speed("fastest")
    hirst.hideturtle()
    hirst.penup()
    hirst.setheading(225)
    hirst.forward(300)
    hirst.setheading(0)
    hirst.speed("slowest")
    for i in range(total_dots):
        if i % 10 == 0 and i > 0:
            next_row()
        make_dot()
        move_forward()


make_painting()

screen = t.Screen()
screen.exitonclick()
