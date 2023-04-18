"""Zip File."""
__author__ = "730506662"

def zip(list_keys: list[str], values: list[int]) -> dict[str,int]:
    dict_return: dict[str,int] = {}
    if len(values) != len(list_keys):
        return dict_return
    if len(values) == 0 or len(list_keys) == 0:
        return dict_return
    for index in range(0, len(list_keys)):
        dict_return[list_keys[index]] = values[index]
    return dict_return
