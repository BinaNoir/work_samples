from .utils import typewriter
from .constants import HOST_INTRODUCTION_TEXT
from .username import (
    get_username,
)

from .start_game import game_init
from .game_loop import (
    draw_random_number,
    feedback_guess,
    end_of_game,
)
from .replay_game import replay


def main():
    typewriter(HOST_INTRODUCTION_TEXT)
    name = get_username()
    game_init()
    while True:
        my_number = draw_random_number()
        guesses_taken, my_number, guess = feedback_guess(my_number)
        end_of_game(guesses_taken, my_number, guess)
        replay(name)


if __name__ == "__main__":
    main()
