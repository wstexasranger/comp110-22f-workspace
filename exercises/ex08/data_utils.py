"""Dictionary related utility functions."""

__author__ = "730601447"

# Define your functions below
"""Some helpful utility functions for working with csv files."""

from csv import DictReader
from typing import Dict

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of the csv into a table."""
    result: list[dict[str, str]] = []
    
    #open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    #read that file

#prepare to read the data file as a csv instead of strings
    csv_reader = DictReader(file_handle)

# read each row of the csv line by line
    for row in csv_reader:
        result.append(row)

    #close the file when we're done, saves resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column"""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result

def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column oriented table"""
    result: dict[str, list[str]] = {} #could also use dict()
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result

def head(columndata: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Gets the top 5 rows of each column."""
    result: dict[str, list[str]] = {}
    for key in columndata:
        emptyList: list[str] = []
        testlist: list[str] = columndata[key] #I have no idea why this was required, but it's the only way I could get it to work
        i: int = 0
        J: int = N
        if(len(testlist) < N):
            J = len(testlist)
        while i < J:
            emptyList.append(testlist[i])
            i = i + 1
        result[key] = emptyList
        
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produces a new column based table with only a specific subset."""
    result: dict[str, list[str]] = {}
    for word in names:
        returnlist: list[str] = ""
        returnlist = table[word]
        result[word] = returnlist
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables."""
    result: dict[str, list[str]] = {}
    for key in table1:
        result[key] = table1[key]
    for key in table2:
        if key in result:
            result[key] = table1[key] + table2[key]
        else:
            result[key] = table2[key]
        
    return result


def count(freq: list[str]) -> dict[str, int]:
    """Counts the frequency of a word in a list."""
    result: dict[str, int] = {}
    for word in freq:
        if word in result:
            result[word] = result[word] + 1
        else:
            result[word] = 1
    return result