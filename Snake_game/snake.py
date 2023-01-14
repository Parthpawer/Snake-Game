from turtle import Turtle, Screen
from time import sleep

class Snake:


    def __init__(self):
        self.turtle_list = []

        self.new_snake()


    def new_snake(self):
        for i in range(0, 3):
            temp = Turtle("square")
            temp.speed(1)
            temp.penup()
            temp.color("white")
            temp.goto(x = (20 * (-i)), y = 0)
            self.turtle_list.append(temp)
            
    def move(self):
            for i in range(len(self.turtle_list) - 1, 0, -1):
                x = self.turtle_list[i - 1].xcor()
                y = self.turtle_list[i - 1].ycor()
                self.turtle_list[i].goto(x, y)
            self.turtle_list[0].forward(20)

    def turn_left(self):
        if self.turtle_list[0].heading() != 0:
            self.turtle_list[0].setheading(180)

    def turn_right(self):
        if self.turtle_list[0].heading() != 180:
            self.turtle_list[0].setheading(0)

    def turn_down(self):
        if self.turtle_list[0].heading() != 90:
            self.turtle_list[0].setheading(270)

    def turn_up(self):
        if self.turtle_list[0].heading() != 270:
            self.turtle_list[0].setheading(90)

    def game_over(self):
        temp = Turtle()
        temp.color("white")
        temp.write(f"Game Over", align = "center", font=("Ariel", 24, "normal"))
        temp.penup()
        temp.hideturtle()

    def new_element(self):
        temp = Turtle("square")
        temp.speed("fastest")
        temp.penup()
        temp.color("white")
        self.turtle_list.append(temp)



    def pos(self):
        a = self.turtle_list[0].xcor()    
        b = self.turtle_list[0].ycor()
        return (a, b)
