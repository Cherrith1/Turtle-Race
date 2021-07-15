from turtle import Turtle,Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Choose your Turtle", prompt="Which turtle do you think will win ?"
                                                               " Pick a colour from VBGYOR").lower()

colors = ["violet","blue","green","yellow","orange","red"]

turtles = []

for index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-230, y=-100 + index * 30)
    turtles.append(tim)

game_on = True
winner = "None"

while(game_on):

    for turtle in turtles:
        turtle.forward(randint(0,10))
        if turtle.xcor() >= 220:
            game_on = False
            winner = turtle.pencolor()
            break

if(winner == user_bet):
    print(f"You won. {winner} turtle is the winner")

else:
    print(f"You lose. {winner} turtle is the winner")

screen.exitonclick()