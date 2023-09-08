from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        # 10x10 apple is created
        self.color('red')
        self.speed('fastest')
        self.Refresh_food()

    def Refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        # food spawns to a random place on 600x600 screen
        self.goto(random_x, random_y)
