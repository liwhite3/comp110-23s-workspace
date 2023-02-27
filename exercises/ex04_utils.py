"""Utility Functions"""
__author__ = "730506662"


def all(list: list[int], int: int) -> bool:
    """Determines if the list matches the given integer"""
    indx: int = 0
    if len(input) == 0:
            return[False]
    while indx < len(list):
        if list[indx] == int[indx]:
            indx += 1
        else:
            return(False)
    return(True)

def max(list: list[int]) -> int:
    """Determine max value from list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    my_max: int = 0
    indx: int = 0
    while indx < len(list):
        if list[indx] > my_max:
            my_max = list[indx]
        indx += 1
    return(my_max)

def is_equal(list1: list[int], list2: list[int]) -> bool:
    indx: int = 0
    while indx < len(list1) and len(list2):
        if list1[indx] == list2[indx]:
            indx += 1
        else:
            return(False)
    return(True)
