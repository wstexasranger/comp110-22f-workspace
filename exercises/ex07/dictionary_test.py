"""Testing file for dictionary file for ex07."""
import pytest
from dictionary import invert
from dictionary import count
from dictionary import favorite_color
__author__ = "730601447"


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


def test_favorite_color() -> None:
    """Tests for multiple instances of a color."""
    testDict: dict[str, str]
    testDict = dict({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"})
    assert favorite_color(testDict) == "blue"


def test_favorite_color_singles() -> None:
    """Tests for first instance of color when number of colors is equal."""
    testDict: dict[str, str]
    testDict = dict({"Marc": "yellow", "Ezri": "blue", "Kris": "green"})
    assert favorite_color(testDict) == "yellow"


def test_favorite_color_empty() -> None:
    """Tests empty dict."""
    testDict: dict[str, str]
    testDict = dict()
    assert favorite_color(testDict) == ""


def test_favorite_color_doubles() -> None:
    """Tests for first instance of color when number of colors is equal."""
    testDict: dict[str, str]
    testDict = dict({"Marc": "yellow", "Ezri": "yellow", "Kris": "green", "connor": "green"})
    assert favorite_color(testDict) == "yellow"


def test_count_list_singles() -> None:
    """Tests for single instances of values."""
    testList: list[str] = ["yellow", "blue", "green"]
    assert count(testList) == {"yellow": 1, "blue": 1, "green": 1}


def test_count_list_doubles() -> None:
    """Tests for double instances of values."""
    testList: list[str] = ["yellow", "yellow", "green"]
    assert count(testList) == {"yellow": 2, "green": 1}


def test_count_list_empty() -> None:
    """Tests for no  instances of values."""
    testList: list[str] = []
    assert count(testList) == {}