import sys
from .utils import typewriter


def process_replay_input(name, raw_input):
    user_input = raw_input.strip().lower()

    if user_input == "yes":
        return "break", ""
    elif user_input == "no":
        return "exit", (
            f"Thank you for playing! "
            f"I hope I can count on you again soon, "
            f"{name.capitalize()}. Goodbye! Ah-ah-ah!"
        )
    else:
        return None, "Sorry, I didn't get this. (Enter 'yes' or 'no'.)"


def replay(name):
    typewriter("Would you like to play another round? (yes/no)")
    user_input = None

    while user_input == None:
        raw_input = input()
        game_state, response = process_replay_input(name, raw_input)
        typewriter(response)

        if game_state == "break":
            break

        elif game_state == "exit":
            sys.exit()
