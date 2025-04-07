"""This file simulates the river at values 10 and 2, for 1 day and 1 week."""

from exercises.EX04.river import River

__author__: str = "730678385"
my_river: River = River(10, 2)
"""Assigns river values 10 and 2."""
my_river.view_river()
"""Views river after 1 day."""
my_river.one_river_week()
"""Views river after 1 week."""
