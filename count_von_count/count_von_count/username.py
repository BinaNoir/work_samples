from .utils import typewriter


def validate_name_input(raw_input):

    name = raw_input.strip()

    if not name:
        return "", (
            "Don't be shy! Please tell me your name."
            "Your input can't be empty."
        )
    elif not name.isalpha():
        return "", (
            "I love numbers and symbols..."
            "But now I like to get some letters."
            "(Your input can only contain letters.)"
        )
    else:
        return name, (
            f"Would you like to play a game with me, {name.capitalize()}? "
            "(yes/no)"
        )


def get_username():
    """Getting the username through a dialogue."""
    name = ""
    while name == "":
        raw_input = input()
        name, response = validate_name_input(raw_input)
        typewriter(response)
    return name
