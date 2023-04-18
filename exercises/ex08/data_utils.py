"""Data Wrangling."""

__author__ = "730506662"

from csv import DictReader

def read_csv_rows (filename: str) -> list[dict[str,str]]:
    """Read data wrangling file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, 'r', encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values column under headers."""     
    result: list[str] = []
    for row in table:
        result.append(row[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    """Reformats data to have column headers as keys."""
    result: dict[str, list[str]] = {}
    first_row: dict[str,str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result


def head (input: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Returns the first N number of rows for each data set."""
    result: dict[str, list[str]] = {}
    for row in input:
        l: list[str] = []
        for i in range(min(n, len(input[row]))):
            l.append(input[row][i])
        result[row] = l
    return result


def select(table: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Create a new table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for row in name:
        result[row] = table[row]
    return result

def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Create a new table from the combination of two column-based tables."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            result[column].extend(table_2[column])
        else:
            result[column] = table_2[column]
    return result
    

def count(frequencies: list[str]) -> dict[str, int]:
    """Counts how many times a value appears in a list."""
    result: dict[str, int] = {}
    for item in frequencies:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result