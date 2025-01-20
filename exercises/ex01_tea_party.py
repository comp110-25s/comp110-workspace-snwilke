"""Calculating tea party guests, tea bags, treats, and cost."""

__author__: str = "730678385"


def main_planner(guests: int) -> None:
    """Summarize number of tea bags, treats, and cost."""
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(guests)}")
    print(f"Treats: {treats(guests)}")
    print(f"Cost: ${cost(tea_bags(guests), treats(guests))}")


def tea_bags(people: int) -> int:
    """Number of tea bags per guest"""
    return 2 * people


def treats(people: int) -> int:
    """Number of treats per guest"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate cost of tea bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
