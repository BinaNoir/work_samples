from .utils import typewriter


def replay(name):
    typewriter("Would you like to play another round? (yes/no)")
    user_input = input().lower()
    while True:
        if user_input == "yes":
            break
        elif user_input == "no":
            typewriter(
                f"Thank your for playing!"
                f"I hope I can count on you again soon, "
                f"{name.capitalize()}. Goodbye! Ah-ah-ah!"
            )
            quit()
        else:
            typewriter("Sorry, I didn't get this. (Enter 'yes' or 'no'.)")
            user_input = input().lower()
