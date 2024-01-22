from tkinter import messagebox as tm
from collections import OrderedDict
from random import randint
from turtle import Turtle, Screen
from custom_turtle import CustomTurtle
from my_screen import MyScreen

START_POINT = 230
all_turtles = []


def display_turtles(turtles: OrderedDict):
    for i, (colour, y_position) in enumerate(turtles.items()):
        my_turtle = Turtle(shape='turtle')
        my_turtle.penup()
        my_turtle.color(colour)
        my_turtle.goto(x=-abs(START_POINT), y=y_position)
        all_turtles.append(my_turtle)


def main():
    turtles = CustomTurtle.get_turtles()
    if __name__ == '__main__':

        screen = MyScreen.screen('turtle racing game'.title())
        user_bet = screen.textinput(title="Make your bet",
                                    prompt=f'which tutle will win the race {[k for k in turtles.keys()]}').lower()
        if user_bet not in turtles.keys():
            raise Exception("Please choose a turtle colour from the specified list!")

        display_turtles(turtles=turtles)

        is_playing = True if user_bet else False
        while is_playing:
            for turtle in all_turtles:
                turtle.forward(randint(0, 10))
                if turtle.xcor() > abs(START_POINT):
                    is_playing = False
                    win_color = str(turtle.pencolor()).capitalize()
                    status = 'won' if win_color.lower() == user_bet else 'lost'
                    tm.showinfo(title='',
                                message=f"You've {status.capitalize()}! The {win_color} turtle is the winner!")
                    screen.bye()


if __name__ == '__main__':
    main()
