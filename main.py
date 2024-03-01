import turtle
import pandas

screen = turtle.Screen()
screen.setup(720, 500)
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")

author = turtle.Turtle()
author.penup()
author.hideturtle()
scorekeeper = turtle.Turtle()
scorekeeper.penup()
scorekeeper.hideturtle()


def update_score(score):
    scorekeeper.clear()
    scorekeeper.goto(-100, 210)
    scorekeeper.write(f"Score: {score}/50", False, "center", ("Arial Black", 16, 'normal'))


# Asks the user for input and checks to see if the state exists
def guess_loop(data):
    states_guessed = []
    correct_guesses = len(states_guessed)
    while correct_guesses < 50:
        answer_state = screen.textinput(title="Guess a state", prompt="What's another state's name?")
        title_state = answer_state.title()
        selected_state = data[data.state == title_state]
        if not selected_state.empty:
            if title_state not in states_guessed:
                author.goto(int(selected_state.iloc[0].x), int(selected_state.iloc[0].y))
                author.write(f"{selected_state.iloc[0].state}")
                states_guessed.append(selected_state.iloc[0].state)
                print(states_guessed)
                correct_guesses += 1
                update_score(correct_guesses)


guess_loop(states_data)
turtle.mainloop()
