from .utils import typewriter
from .constants import HOST_INTRODUCTION_TEXT
from .username import get_username
from .start_game import game_init
from .game_loop import guess_init, draw_random_number
from .replay_game import replay


def main():
    typewriter(HOST_INTRODUCTION_TEXT)
    name = get_username()
    game_init(name)
    while True:
        random_number = draw_random_number()
        guess_init(random_number)
        replay(name)


if __name__ == "__main__":
    main()
