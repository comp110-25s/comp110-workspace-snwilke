"""Wordle for COMP110!"""

__author__: str = "730678385"


def contains_char(full_word: str, single_character: str) -> bool:
    """Checks to see if a single character is in the full secret word via indexing"""
    assert len(single_character) == 1, f"len('{full_word}') is not 1"
    x: int = 0
    while x < len(full_word):
        if full_word[x] == single_character:
            return True
        x += 1
    return False


def emojified(guess_word: str, full_word: str) -> str:
    """Presents matching index str characters as green, matching str characters as yellow, and extraneous characters as white"""
    assert len(guess_word) == len(full_word), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    x: int = 0
    colors: str = ""
    while x < len(guess_word):
        if guess_word[x] == full_word[x]:
            colors += GREEN_BOX
        elif contains_char(full_word, guess_word[x]):
            colors += YELLOW_BOX
        else:
            colors += WHITE_BOX
        x += 1
    return colors


def input_guess(expected_length: int) -> str:
    """Ask players to make a guess of the correct length"""
    guess: str = input(f"Enter a {expected_length} character word:")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    turn_max: int = 6
    while turn <= turn_max:
        print(f"=== Turn {turn}/{turn_max} ===")
        player_guess: str = input_guess(len(secret))
        print(emojified(player_guess, secret))
        if player_guess == secret:
            print(f"You won in {turn}/{turn_max} turns!")
            return
        turn += 1
    print(f"X/{turn_max} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
