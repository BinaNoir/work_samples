import sys
import random
from .utils import typewriter
from .constants import GUESS_PROMPT


def process_init_input(name, raw_input):
    user_input = raw_input.strip().lower()
    if user_input == "yes":
        return "break", (
            "Alright! It's a guessing game: "
            "I will choose a number between 1 and 100 [1,100]."
            "You need to guess which number it is. "
        )
    elif user_input == "no":
        return "exit", (
            "I'm sorry that you missed out a chance to learn "
            "something about numbers."
            "Remember: If you dont ask, you won't know. "
            f"Goodbye, {name.capitalize()} !"
        )
    else:
        return "", ("Sorry, I didn't understand you. (Enter 'yes' or 'no'.)")


def game_init(name):
    """Start game or end script depending on user input."""
    user_input = ""
    while user_input == "":
        raw_input = input()
        game_state, response = process_init_input(name, raw_input)
        typewriter(response)

        if game_state == "break":
            break
        if game_state == "exit":
            sys.exit()
