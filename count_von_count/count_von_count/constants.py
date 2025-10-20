HOST_INTRODUCTION_TEXT = """\
Greetings! It is I, the Count!
I guess you've heard from me before. 
I'm well known for my mathematical teaching skills.
I love to count.
What's your name?"""

# Possible outputs to ask for a guess returned by draw_random_number().
GUESS_PROMPT = [
    "Take a guess!",
    "Give me a number!",
    "What's your tip?",
    "Make a guess!",
    "Take a shot!",
    "Give it a try!",
    "Make a guess!",
    "Tell me a number!",
    "What number do you have in mind?",
    "Please share your number!",
]

# Possible outputs to ask for another guess returned by feedback_guess().
GUESS_AGAIN_PROMPT = [
    " Try again!",
    " Give it another shot!",
    " Take another guess!",
    " Have another go!",
    " Give it another try!",
    " Try once more!",
    " Take a swing at it again!",
    " Give it one more attempt!",
    " Let’s see another guess!",
    " You can do better, try again!",
]

# Possible outputs if guess is too low returned by feedback_guess().
TOO_LOW_FEEDBACK = [
    "Your guess is too low.",
    "That guess is below the target.",
    "Too low!",
    "You're below the correct number.",
    "That’s not high enough.",
    "You need to guess a larger number.",
    "You're below the mark.",
    "That number is too small.",
    "You might want to go higher.",
    "Try a number that's more than that.",
]

# Possible outputs if guess is too high returned by feedback_guess().
TOO_HIGH_FEEDBACK = [
    "Your guess is too high.",
    "That guess is above the target.",
    "You're too high.",
    "Too high; aim a bit lower!",
    "You're over the correct number.",
    "That’s not low enough.",
    "You need to guess a smaller number.",
    "You're above the mark.",
    "That number is too large.",
    "You might want to go lower.",
    "Try a number that's less than that.",
]
