"""Ex07 Testing Code."""

__author__ = "730506662"

from exercises.ex07.dictionary import invert, count, favorite_color


def test_invert_use1() -> None:
    """Use Case 1."""
    input = {'apple': '1', 'orange': '2', 'pineapple': '3'}
    assert invert(input) == {'1': 'apple', '2': 'orange', '3': 'pineapple'}


def test_invert_use2() -> None:
    """Use Case 2."""
    input = {'Chris': 'Hemsworth', 'Leonardo': 'Dicaprio'}
    assert invert(input) == {'Hemsworth': 'Chris', 'Dicaprio': 'Leonardo'}


def test_invert_edge() -> None:
    """Edge Case 1."""
    input = {}
    assert invert(input) == {}


def test_count_use1() -> None:
    """Use Case 1."""
    input = ['yellow', 'yellow', 'blue', 'purple', 'purple', 'purple']
    assert count(input) == {'yellow': 2, 'blue': 1, 'purple': 3}


def test_count_use2() -> None:
    """Use Case 2."""
    input = ['green', 'green', 'green', 'green', 'green', 'purple']
    assert count(input) == {'green': 5, 'purple': 1}


def test_count_edge1() -> None:
    """Edge Case 1."""
    input = {}
    assert count(input) == {}


def test_favorite_color_use1() -> None:
    """Use Case 1."""
    input = {'Lindsey': 'purple', 'Lauren': 'green', 'Steve': 'green', 'Debi': 'blue'}
    assert favorite_color(input) == 'green'


def test_favorite_color_use2() -> None:
    """Use Case 2."""
    input = {'Booth': 'purple', 'Kiera': 'purple', 'Danny': 'yellow', 'Calvin': 'orange'}
    assert favorite_color(input) == 'purple'


def test_favorite_color_edge1() -> None:
    """Edge Case 1."""
    input = {'McKenzie': 'orange', 'Olivia': 'blue', 'Rose': 'green', 'Jackie': 'pink'}
    assert favorite_color(input) == 'orange'