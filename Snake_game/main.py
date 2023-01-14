from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)


temp = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()

screen.onkey(temp.turn_left, "Left")
screen.onkey(temp.turn_right, "Right")
screen.onkey(temp.turn_down, "Down")
screen.onkey(temp.turn_up, "Up")

score = 0

a = True
while a:
    screen.update()
    sleep(0.1)
    temp.move()
    k = temp.pos()
    if temp.turtle_list[0].distance(food) < 15:
        food.refresh()
        temp.new_element()
        score += 1
        scoreboard.increase_score()
    if -290 <= k[1] <= 290 and -290 <= k[0] <= 290:
        a = True
    else:
        temp.game_over()
        a = False
    for i in range(1, len(temp.turtle_list)):
        if temp.turtle_list[0].distance(temp.turtle_list[i]) < 10:
            a = False
            temp.game_over()

screen.exitonclick()


# screen = Screen()
# screen.title("Snake Game")
# screen.bgcolor("black")
# # screen.tracer(0)
# screen.listen()

# color_list = ["red", "blue", "pink", "green", "purple", "yellow", "violet", "crimson"]


# turtle_list = []

# def new_snake():
#     for i in range(0, 3):
#         temp = Turtle("square")
#         temp.speed(1)
#         temp.penup()
#         temp.color(color_list[i])
#         temp.goto(x = (20 * (-i)), y = 0)
#         turtle_list.append(temp)

# def continous_forward_movement():
#     a = True
#     while a:
#         for i in range(len(turtle_list) - 1, 0, -1):
#             x = turtle_list[i - 1].xcor()
#             y = turtle_list[i - 1].ycor()
#             turtle_list[i].goto(x, y)
#         turtle_list[0].forward(20)
#         screen.update()
#         sleep(0.1)

# def turn_right():
#     turtle_list[0].left(90)

    



# new_snake()
# screen.onkey(turn_right, "d")
# continous_forward_movement() 

# screen.exitonclick()