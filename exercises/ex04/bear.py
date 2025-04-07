"""File to define Bear class."""

___author___: str = "730678385"


class Bear:
    """Creates new bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """New list of bears with age and hunger."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Ages and tracks bears hunger per day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Feeds bears fish."""
        self.hunger_score += num_fish
