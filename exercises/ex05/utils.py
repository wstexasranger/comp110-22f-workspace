"""Examples of running tests."""
___author___: str = "730601447"

def only_evens(randList: list[int]) -> list[int]:
    "Take in a list with random number, output a list with only the even numbers."
    evenList: list[int] = []
    i: int = 0
    while i < len(randList):
        if(randList[i] % 2 ==0):
            evenList.append(randList[i])
        i = i + 1
    return evenList

def concat(listOne: list[int], listTwo: list[int]) -> list[int]:
    "Append the first list with all the items of the second list."
    i: int = 0
    returnList: list[int] = listOne
    while i < len(listTwo):
        returnList.append(listTwo[i])
        i = i + 1
    return returnList

def sub(aList: list[int], idx1: int, idx2: int) -> list[int]:
    i: int = idx1
    returnList: list[int] = []
    while i < idx2:
        returnList.append(aList[i])
        i = i + 1
    return returnList