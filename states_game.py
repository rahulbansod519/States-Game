import turtle
import pandas


def main():
    screen = turtle.Screen()
    screen.title("States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    total_state = len(all_states)
    guessed_state = []

    while len(guessed_state) < total_state:
        answer_state = screen.textinput(title=f"{len(guessed_state)}/{total_state} states name",
                                        prompt="What is another state name?").title()
        if answer_state == "Exit":
            save_remaining_state(all_states, guessed_state)
            break
        if answer_state in all_states:
            guessed_state.append(answer_state)
            display_state_name(data, answer_state)
    turtle.mainloop()


def save_remaining_state(all_states, guessed_state):
    new_list = list(set(all_states).difference(guessed_state))
    new_df = pandas.DataFrame(new_list)
    new_df.to_csv("state_to_learn.csv")


def display_state_name(data, answer_state):
    tk = turtle.Turtle()
    tk.hideturtle()
    tk.penup()
    state_data = data[data["state"] == answer_state]
    tk.goto(int(state_data.x), int(state_data.y))
    tk.write(state_data.state.item(), font=("Arial", 10, "normal"))


if __name__ == "__main__":
    main()
