"""File to define Fish class."""

__author__: str = "730678385"


class Fish:
    """Creates new fish."""

    age: int

    def __init__(self):
        """New list of fish."""
        self.age = 0
        return None

    def one_day(self):
        """Ages the fish."""
        self.age += 1
        return None
