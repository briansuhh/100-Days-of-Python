import turtle
import pandas

# make a function to put the name of the state on the map
def write_state(input, data):
    if input in data.state.values:
        state = data[data.state == input] # get the row of the state
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state.x.iloc[0]), int(state.y.iloc[0])) # use iloc because x and y is a series with only one value
        t.write(input, align="center", font=("Arial", 8, "normal"))
        guessed_states.append(input)


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.bgpic("Day 25/blank_states_img.gif")

# get the data from the csv file
data = pandas.read_csv("Day 25/50_states.csv")

guessed_states = []

while len(guessed_states) < 50:
    input = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if input == "Exit":
        missing_states = [state for state in data.state.values if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day 25/missing_states.csv")
        break

    write_state(input, data)

