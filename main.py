from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtke will win the race")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-220, y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            race_on = False
            winning = turtle.pencolor()
            if winning == user_bet:
                print("You won")
            else:
                print(f"You lost. The winner is {winning} turtle")
        distance = random.randint(0, 10)
        turtle.forward(distance)




screen.exitonclick()
