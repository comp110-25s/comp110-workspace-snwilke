"""Test file for dictionary.py"""

__author__: str = "730678385"

import pytest
from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


def test_invert_empty_case():
    """Test empty dictionary edge case."""
    assert invert({}) == {}


def test_invert_use_case():
    """Test use case swapping numbers"""
    assert invert({"1": "2", "3": "4", "5": "6"}) == {"2": "1", "4": "3", "6": "5"}


def test_invert_second_use_case():
    """Test use case with KeyError."""
    with pytest.raises(KeyError):
        invert({"1": "2", "3": "2"})


def test_count_empty():
    """Test edge case using empty list."""
    assert count([]) == {}


def test_count_use():
    """Test a regular countable list."""
    assert count(["apple", "mango", "pear"]) == {"apple": 1, "mango": 1, "pear": 1}


def test_count_use_2():
    """Test countable list with repeat."""
    assert count(["apple", "apple", "apple"]) == {"apple": 3}


def test_fav_color_empty():
    """Test empty edge case."""
    assert favorite_color({}) == ""


def test_fav_color_use():
    """Test regular list of fav colors"""
    assert (
        favorite_color({"Sara": "Blue", "Zander": "Green", "Susan": "Blue"}) == "Blue"
    )


def test_fav_color_use_2():
    """Test fav color with equal votes"""
    assert (
        favorite_color({"Sara": "Blue", "Zander": "Green", "Susan": "Purple"}) == "Blue"
    )


def test_bin_empty():
    """Test edge case of empty list."""
    assert bin_len([]) == {}


def test_bin_use():
    """Test regular varied word lengths."""
    assert bin_len(["hi", "hello", "hey"]) == {2: {"hi"}, 3: ["hey"], 5: {"hello"}}


def test_bin_use_2():
    """Test use case with only 1 length of word."""
    assert bin_len(["comp", "womp", "romp"]) == {4: {"comp", "womp", "romp"}}
