from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def change_color(self):
        r = random.randrange(0, 255, 10)
        g = random.randrange(0, 255, 10)
        b = random.randrange(0, 255, 10)
        self.color(r, g, b)

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()