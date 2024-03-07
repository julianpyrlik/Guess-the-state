import turtle
import pandas

data = pandas.read_csv("50_states.csv")
FONT = ("Courier", 20, "bold")

# Setting up screen
screen = turtle.Screen()
screen.title("Guess the state")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Functions


def adding_state(state_name, xcor, ycor):
    new_state = turtle.Turtle()
    new_state.hideturtle()
    new_state.penup()
    new_state.goto(xcor, ycor)
    new_state.write(state_name)


def win():
    winning = turtle.Turtle()
    winning.hideturtle()
    winning.penup()
    winning.write(f"Congratulations, you guessed all the states! ", font=FONT, align="center")


#  Converting data into lists

state_list = data["state"].to_list()
state_list_delete = data["state"].to_list()
x_list = data["x"].to_list()
y_list = data["y"].to_list()

game_is_on = True  # True as long as the answers are correct
correct_answers = 0  # Starting value


while game_is_on:
    answer = screen.textinput(title=f"{correct_answers}/50 states guessed", prompt="Type in a state (type e to exit)").title()

    if answer in state_list:
        # Determine the coordinates of the correct answer
        row = data[data.state == answer]  # Row of the correct city
        xcor = int(row.x)
        ycor = int(row.y)

        # Creating the text turtle and move it to the new coordinates
        adding_state(answer, xcor, ycor)
        correct_answers += 1
        state_list_delete.remove(answer)

    # exit
    if answer == "E":
        missed_states_data = pandas.DataFrame(state_list_delete)
        missed_states_data.to_csv("missed_states.csv")
        break

    # win
    if correct_answers == 50:
        win()
        break
