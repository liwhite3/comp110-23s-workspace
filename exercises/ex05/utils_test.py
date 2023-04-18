"""Test for List Unitility Functions."""
__author__ = "730506662"

from exercises.ex05.utils import only_evens, sub, concat


def test_some_evens() -> None:
    """Test a list with some even values and sum odd."""
    list_int_var: list[int] = only_evens([1, 2, 3])
    assert list_int_var == [2]

def test_only_odds() -> None:
    """Test a list with only odd values."""
    list_int_var: list[int] = only_evens([1, 3, 5])
    assert list_int_var == []


def test_only_evens() -> None:
    """Test a list with only even values."""
    list_int_var: list[int] = only_evens([2, 2, 2])
    assert list_int_var == [2, 2, 2]


def test_empty_list() -> None:
    """Test an empty list."""
    assert concat([], []) == []


def test_use_case_1() -> None:
    """Test identical lists."""
    assert concat([1, 2, 3], [1, 2, 3]) == [1, 2, 3, 1, 2, 3]


def test_use_case_2() -> None:
    """Test even lists."""
    assert concat([2, 4, 6, 8, 10], [2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10, 2, 4, 6, 8, 10]


def test_use_case1() -> None:
    """Test list with values 1, 3."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_edge_case1() -> None:
    """Test list beyond range."""
    assert sub([1, 2], 2, 3) == []


def test_use_case2() -> None:
    """Test list with a negative and increased index values."""
    assert sub([-1, 0, 1, 2, 3, 4], 1, 4) == [0, 1, 2]