import turtle

import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()

# Move the turtle to a specific position

guessed_states = []
user_score = 0

df = pandas.read_csv("50_states.csv")

all_states = df["state"].to_list()
while len(guessed_states)<=50:
    answer_state = screen.textinput(title=f"{user_score}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        user_score +=1
        answer_state_row = df[df.state==answer_state]
        t.hideturtle()
        t.penup()  # Lift the pen to avoid drawing lines
        t.goto(answer_state_row.x.item(), answer_state_row.y.item())
        t.pendown()  # Lower the pen to write text

        # Write the user input at the turtle's current position
        t.write(answer_state, move=False, align="center", font=("Arial", 8, "normal"))

missing_states = [state for state in all_states if state not in guessed_states ]
data = pandas.DataFrame(missing_states)
data.to_csv("states_to_learn.csv")
# print(missed_states)
