import sys
import textwrap
import time


def typewriter(str):
    """Gives outputs a tywriter effect."""
    str = textwrap.dedent(str).strip()
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
