import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=750, height=515)
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
game_on = True

data = pd.read_csv('50_states.csv')
states = data.state.to_list()
guessed_states = []
title = 'Guess the State'

while game_on:
    answer_state = screen.textinput(title, prompt='Type a name of the state').title()
    state_data = data[data['state'] == answer_state]
    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        title = f'{len(guessed_states)}/{len(states)}'
        print(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state, align='center', font=('Arial', 12, 'normal'))
        if len(guessed_states) == len(states):
            game_on = False
            game_over = turtle.Turtle()
            game_over.hideturtle()
            game_over.penup()
            game_over.write('Great, You know all the states!', align='center', font=('Arial', 30, 'bold'))

screen.mainloop()

