"""File to define River class."""

__author__: str = "730678385"

from exercises.EX04.bear import Bear
from exercises.EX04.fish import Fish


class River:
    """River class created."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages of animals to kill them off."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]
        return None

    def bears_eating(self):
        """Makes bears eat 3 fish for 5 existing."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Checks bears hunger then kills it if below 0."""
        surviving: list[Bear] = [bear for bear in self.bears if bear.hunger_score >= 0]
        self.bears = surviving
        return None

    def repopulate_fish(self):
        """Births 4 fish to 2 parents."""
        new_fish: int = (len(self.fish) // 2) * 4
        for _ in range(new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Births 1 bear to 2 parents."""
        new_bears: int = len(self.bears) // 2
        for _ in range(new_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Views the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates 1 week in river."""
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Removes fish for another fn."""
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)
