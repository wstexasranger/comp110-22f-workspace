"""The dictionary for the ex07 assignment."""
__author__ = "730601447"

from itertools import count


def invert(stuff: dict[str, str]) -> dict[str, str]:
    """Inverts an input dictionary and returns"""
    returnDict: dict[str, str]
    returnDict = dict()
    for first in stuff:
        if stuff[first] in returnDict:
            raise KeyError(f"Already an instance of {stuff[first]} in the dictionary Keys!")
        returnDict[stuff[first]] = first
    return returnDict

def favorite_color(stuff: dict[str, str]) -> str:
    """Returns most common color."""
    countDict: dict[str, str]
    countDict = dict()
    returnStr: str = ""
    for color in stuff:
        """Creates a numbered dict where Color : instances"""
        if stuff[color] in countDict:
            countDict[stuff[color]] = countDict[stuff[color]] + 1
        else: 
            countDict[stuff[color]] = 1
    for color in countDict:
        """Gets first instance of a color, needed for next for."""
        returnStr = color
        break
    for color in countDict:
        if (countDict[color] > countDict[returnStr]):
            if (countDict[color] == countDict[returnStr]):
                returnStr = returnStr
            else:
                returnStr = color
    return returnStr

def count_dict(stuff: dict[str, str]) -> dict[str, int]:
    """Returns most common color."""
    countDict: dict[str, str]
    countDict = dict()
    returnStr: str = ""
    for keys in stuff:
        """Creates a numbered dict where Key : instances"""
        if stuff[keys] in countDict:
            countDict[stuff[keys]] = countDict[stuff[keys]] + 1
        else: 
            countDict[stuff[keys]] = 1
    return(countDict)