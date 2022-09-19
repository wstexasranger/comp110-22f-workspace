"""Examples of utilizing append, pop, index, etc. in lists."""
___author___ = "730601447"


def all(same: list[int], check: int) -> bool:
    "Returns a true or false if the whole list is repeated instances of the check int."
    i: int = 0
    while i < len(same):
        if same[i] == check:
            i = i + 1
        else:
            return False
    return True

def max(blist: list[int]) -> int:
    "Return the max value of the list, or returns an error if empty."
    if len(blist) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    big: int = blist[0]
    while i < len(blist):
        if big < blist[i]:
            big = blist[i]
        i = i + 1
    return big

def is_equal(list1: list[int], list2: list[int]) -> bool:
    "Returns a true or false while testing for deep equality."
    if len(list1) != len(list2):
        return False
    i: int = 0
    while i < len(list1):
        if list1[i] == list2[i]:
            i = i + 1
        else:
            return False
    return True