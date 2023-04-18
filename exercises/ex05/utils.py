"""'list' Utility Functions."""
__author__ = "730506662"


def only_evens(input_list: list[int]) -> list[int]:
    """Check for even values in a list."""
    result: list[int] = list()
    for item in input_list:
        if item % 2 == 0:
            result.append(item)
    return result


def concat(list1: int, list2: int) -> list[int]:
    """Combine list 1 and 2."""
    result: list[int] = list()
    for item in list1:
        result.append(item)
    for item in list2:
        result.append(item)
    return result


def sub(list1: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Determines the list inputs beginning at a start index and ending before the end index."""
    idx: int = start_idx
    result: list1[idx] = list()
    while idx < end_idx:
        if idx < 0:
            idx = 0
        if end_idx > len(list1):
            end_idx = len(list1)
        if len(list1) == 0:
            return list()
        if start_idx > len(list1):
            return list()
        if start_idx == len(list1):
            return list()
        if end_idx <= 0:
            return list()
        result.append(list1[idx])
        idx += 1
    return result
