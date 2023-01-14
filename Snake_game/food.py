from turtle import Turtle
from random import randint

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("Red")
        self.speed("fastest")
        self.goto(randint(-280, 289), randint(-280, 280))
    

    def refresh(self):
        self.goto(randint(-280, 289), randint(-280, 280))
        