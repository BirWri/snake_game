from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("MY SNAKE GAME")

snake_body = []
start_positions = [(-20, 0), (0, 0), (20, 0)]

for nr in range(0, 3):
    new_square = Turtle(shape="square")
    new_square.penup()
    new_square.color("white")
    new_square.setpos(start_positions[nr])
    snake_body.append(new_square)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(snake_body)-1, 0, -1):
        new_x = snake_body[seg_num - 1].xcor()
        new_y = snake_body[seg_num - 1].ycor()
        snake_body[seg_num].goto(new_x, new_y)
    snake_body[0].forward(10)
screen.exitonclick()

