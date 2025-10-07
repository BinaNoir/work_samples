import random
from .utils import typewriter
from .constants import (
    HOST_INTRODUCTION_TEXT,
    GUESS_PROMPT,
    GUESS_AGAIN_PROMPT,
    TOO_LOW_FEEDBACK,
    TOO_HIGH_FEEDBACK,
)


def draw_random_number():
    my_number = random.randint(1, 100)
    typewriter(random.choice(GUESS_PROMPT))
    return my_number


def feedback_guess(my_number):
    guesses_taken = 0
    guesses_max = 10
    while guesses_taken < guesses_max:
        try:
            guess = int(input())
            if 1 <= guess <= 100:
                guesses_taken += 1
                if guesses_taken < guesses_max and guess < my_number:
                    typewriter(
                        random.choice(TOO_LOW_FEEDBACK)
                        + random.choice(GUESS_AGAIN_PROMPT)
                    )
                elif guesses_taken < guesses_max and guess > my_number:
                    typewriter(
                        random.choice(TOO_HIGH_FEEDBACK)
                        + random.choice(GUESS_AGAIN_PROMPT)
                    )
                else:
                    break
            else:
                typewriter("Please enter a number between 1 and 100.")
        except ValueError:
            typewriter(
                "Sorry, but your answer doesn't make sense "
                "(Please enter a number between 1 and 100.)"
            )
    return guesses_taken, my_number, guess


def end_of_game(guesses_taken, my_number, guess):
    if guess == my_number:
        if guesses_taken > 1:
            typewriter(f"Well done! You guessed my number in {guesses_taken} guesses!")
        else:
            typewriter(f"Well done! You guessed my number in {guesses_taken} guess!")
    else:
        typewriter(f"Sorry, you're out of guesses. My number is {my_number}.")
