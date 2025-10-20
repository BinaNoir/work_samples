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
    random_number = random.randint(1, 100)
    return random_number


def validate_guess_input(raw_input):
    guess = raw_input.strip()
    if not guess.isdigit():
        return None, (
            "Sorry, but your answer doesn't make sense "
            "(Please enter a number (between 1 and 100).)"
        )
    guess = int(guess)
    if not 1 <= guess <= 100:
        return None, "Please enter a number between 1 and 100."
    return guess, None


def right_guess(guess, random_number, guesses_taken):
    """Detect winning guess"""
    if guess == random_number and guesses_taken == 1:
        return f"Well done! You guessed my number in {guesses_taken} guess!"
    elif guess == random_number and guesses_taken > 1:
        return f"Well done! You guessed my number in {guesses_taken} guesses!"


def out_of_guesses(random_number):
    """Reveal number if out of tries"""
    return f"Sorry, you're out of guesses. My number is {random_number}."


def feedback_guess(
    random_number,
    guess,
    TOO_LOW_FEEDBACK,
    TOO_HIGH_FEEDBACK,
    GUESS_AGAIN_PROMPT,
):
    """Feedback on too high/low guess"""
    if guess < random_number:
        return random.choice(TOO_LOW_FEEDBACK) + random.choice(
            GUESS_AGAIN_PROMPT
        )
    elif guess > random_number:
        return random.choice(TOO_HIGH_FEEDBACK) + random.choice(
            GUESS_AGAIN_PROMPT
        )


def guess_init(random_number):
    """Main loop"""
    typewriter(random.choice(GUESS_PROMPT))
    guesses_taken = 0
    guesses_max = 10

    while guesses_taken < guesses_max:
        raw_input = input()
        guess, error = validate_guess_input(raw_input)
        if error:
            typewriter(error)
            continue

        guesses_taken += 1

        response = right_guess(guess, random_number, guesses_taken)
        if response:
            typewriter(response)
            return

        if guesses_taken < guesses_max:
            response = feedback_guess(
                random_number,
                guess,
                TOO_LOW_FEEDBACK,
                TOO_HIGH_FEEDBACK,
                GUESS_AGAIN_PROMPT,
            )
            typewriter(response)
        else:
            typewriter(out_of_guesses(random_number))
