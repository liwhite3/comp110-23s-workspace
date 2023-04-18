"""Ex07 - Dictionary Functions."""

__author__ = "730506662"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary and inverts the keys and values to return a new dictionary."""
    inverted_dict: dict[str, str] = {}
    for key in input:
        if input[key] in inverted_dict:
            raise KeyError(f"KeyError: {input[key]} is already in the dictionary.")
        inverted_dict[input[key]] = key
    return inverted_dict


def count(input: list[str]) -> dict[str, int]:
    """Input is a list, output returns a dictionary with the list as keys and their frequency as the values."""
    new_dictionary: dict[str, int] = {}
    for keys in input:
        if keys in new_dictionary:
            new_dictionary[keys] += 1
        else:
            new_dictionary[keys] = 1
    return new_dictionary


def favorite_color(input: dict[str, str]) -> str:
    """Input is a dictionary of names with associated favorite colors, output returns the most frequent favorite color."""
    new_dictionary: dict[str, int] = {}
    color: str = ""
    greatest: int = 0
    for keys in input:
        if input[keys] in new_dictionary:
            new_dictionary[input[keys]] += 1
        else:
            new_dictionary[input[keys]] = 1
    for keys in new_dictionary:
        if new_dictionary[keys] > greatest:
            greatest = new_dictionary[keys]
            color = keys
    return color