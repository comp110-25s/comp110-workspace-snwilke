"""Dictionary function skeletons and implementations"""

__author__: str = "730678385"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Swap the key and value of a given dictionary."""
    inverted: dict[str, str] = {}
    for key in dictionary:
        value = dictionary[key]
        if value in inverted:
            raise KeyError("Duplicate key found!")
        inverted[value] = key
    return inverted


def count(the_list: list[str]) -> dict[str, int]:
    """Count the number of times a str appears in a list."""
    idx: int = 0
    counted: dict[str, int] = {}
    while idx < len(the_list):
        if the_list[idx] in counted:
            counted[the_list[idx]] += 1
        else:
            counted[the_list[idx]] = 1
        idx += 1
    return counted


def favorite_color(favorites: dict[str, str]) -> str:
    """Returning the highest count favorite color."""
    counted: dict[str, int] = {}
    for key in favorites:
        temp: str = favorites[key]
        if temp in counted:
            counted[temp] += 1
        else:
            counted[temp] = 1
    highest_count: str = ""
    frequency: int = 0
    for key in favorites:
        temp: str = favorites[key]
        if counted[temp] > frequency:
            highest_count = temp
            frequency = counted[temp]
    return highest_count


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins various strings by their length."""
    the_bin: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length not in the_bin:
            the_bin[length] = set()
        the_bin[length].add(word)
    return the_bin
