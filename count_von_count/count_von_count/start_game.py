from .utils import typewriter


def game_init():
    """Start game or ending script depending on user input."""
    while True:
        user_input = input()
        if user_input.lower() == "yes":
            typewriter(
                "Alright! It's a guessing game: "
                "I will choose a number between 1 and 100 [1,100]."
                "You need to guess which number it is. Let's begin!"
            )
            break
        elif user_input.lower() == "no":
            typewriter(
                "I'm sorry that you missed out a chance to learn "
                "something about numbers."
                "Remember: If you dont ask, you won't know."
                f"Goodbye, {name.capitalize()} !"
            )
            exit()
        else:
            typewriter("Sorry, I didn't understand you. (Enter 'yes' or 'no'.)")
