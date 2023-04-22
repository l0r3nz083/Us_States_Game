import turtle
import pandas as pd
from poster import Poster

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.setup(width=800, height=550)

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")

correct_guesses = []
num_correct = 0

game_is_on = True
while game_is_on:

    answer_state = screen.textinput(title=f"{num_correct}/{len(df)} Guess The State",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    for state in df["state"]:
        if answer_state == state:
            x_cor = int(df[df["state"] == state]["x"])
            y_cor = int(df[df["state"] == state]["y"])
            Poster(state, x_cor, y_cor)
            correct_guesses.append(state)
            num_correct += 1
    if len(correct_guesses) == len(df):
        game_is_on = False

miss_states = []

for state in df["state"]:
    if state not in correct_guesses:
        miss_states.append(state)

states_to_learn = pd.DataFrame(miss_states)
states_to_learn.to_csv("states_to_learn.csv")
