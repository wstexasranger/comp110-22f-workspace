"""Testing file for dictionary file for ex07."""
__author__ = "730601447"
import pytest
from dictionary import invert

def test_invert_empty() -> None:
    """Tests inversion of empty dict."""
    testDict: dict[str, str]
    testDict = dict()
    assert invert(testDict) == {}

def test_invert_example() -> None:
    """Tests normal inversion example."""
    testDict: dict[str, str]
    testDict = dict({"a": "b", "c": "d"})
    assert invert(testDict) == {"b": "a", "d": "c"}

with pytest.raises(KeyError):
    """Tests multiple instances of a value."""
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)

from dictionary import favorite_color

def test_favorite_color() -> None:
    """Tests for multiple instances of a color"""
    testDict: dict[str, str]
    testDict = dict({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"})
    assert favorite_color(testDict) == "blue"

def test_favorite_color_singles() -> None:
    """Tests for first instance of color when number of colors is equal"""
    testDict: dict[str, str]
    testDict = dict({"Marc": "yellow", "Ezri": "blue", "Kris": "green"})
    assert favorite_color(testDict) == "yellow"

def test_favorite_color_empty() -> None:
    """Tests empty dict."""
    testDict: dict[str, str]
    testDict = dict()
    assert favorite_color(testDict) == ""

def test_favorite_color_doubles() -> None:
    """Tests for first instance of color when number of colors is equal"""
    testDict: dict[str, str]
    testDict = dict({"Marc": "yellow", "Ezri": "yellow", "Kris": "green", "connor": "green"})
    assert favorite_color(testDict) == "yellow"

from dictionary import count_dict

def test_count_dict_singles() -> None:
    """Tests for single instances of values"""
    testDict: dict[str, str]
    testDict = dict({"Marc": "yellow", "Ezri": "blue", "Kris": "green"})
    assert count_dict(testDict) == {"yellow": 1, "blue": 1, "green": 1}

def test_count_dict_doubles() -> None:
    """Tests for double instances of values"""
    testDict: dict[str, str]
    testDict = dict({"Marc": "yellow", "Ezri": "yellow", "Kris": "green"})
    assert count_dict(testDict) == {"yellow": 2, "green": 1}

def test_count_dict_empty() -> None:
    """Tests for no  instances of values"""
    testDict: dict[str, str]
    testDict = dict({})
    assert count_dict(testDict) == {}