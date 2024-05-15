# States Game

This Python script creates an interactive game using Turtle graphics and a dataset of states in the United States. The game displays an image of the U.S. map with all the states' outlines. The objective is to guess the names of the states. As the player correctly guesses each state, its name is displayed on the map.

## Setup

1. **Install Python**: Make sure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone this repository to your local machine

3. **Install Required Libraries**: This project requires the `turtle` and `pandas` libraries. You can install them via pip:

## Usage

Run the Python script `states_game.py`. The game window will appear, displaying the U.S. map with the outlines of all the states.

To play the game:
- Enter the name of a state when prompted.
- If the state name is correct, it will be displayed on the map, and you can proceed to guess the next state.
- If you want to exit the game, type "Exit". The game will save a list of states you haven't guessed yet to a file named `state_to_learn.csv`.
- The game continues until you guess all the states or choose to exit.

## Files

- `states_game.py`: Python script containing the game logic.
- `50_states.csv`: Dataset containing the names and coordinates of states in the United States.
- `blank_states_img.gif`: Image file displaying the U.S. map with blank outlines of states.
- `state_to_learn.csv`: Output file containing the list of states that the player hasn't guessed yet.

## Requirements

- Python 3.x
- turtle
- pandas


