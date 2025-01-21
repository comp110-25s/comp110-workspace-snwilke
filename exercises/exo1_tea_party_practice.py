"""Tea Party Calculations Practice"""

__author__: str = "730678385"


def main_planner(guests: int) -> None:
    """Summarizes tea party plans"""
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(guests)}")
    print(f"Treats: {treats(guests)}")
    print(f"Cost: ${cost(tea_bags(guests), treats(guests))}")


def tea_bags(people: int) -> int:
    """Calculates tea bags per person"""
    return 2 * people


def treats(people: int) -> int:
    """Calculates treats per tea bag"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates cost of tea and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
