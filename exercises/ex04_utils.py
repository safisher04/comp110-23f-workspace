"""Ex04 - Learning List Utility Functions!"""
__author__ = "730648328"


def all(int_list: list[int], num: int) -> bool:
    """Determines is all of the integers in a list are the same as a given integer."""
    """Return False if given an empty list."""
    if len(int_list) == 0:
        return False
    """Establish variables for function."""
    i: int = 0
    same: bool = True
    """Determine if every int in the list matches the given int and return True or False depending."""
    while i < len(int_list):
        if int_list[i] == num:
            same = True
            i += 1
        else:
            return same
    if same is True:
        return True


def max(int_list: list[int]) -> int:
    """Find and return the largest value in a given list of integers."""
    """Raise an error if the given list is empty."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    """Establish needed variables for the function"""
    max: int = int_list[0]
    i: int = 0
    """Search through the list and find the greatest value."""
    while i < len(int_list):
        if int_list[i] > max:
            max = int_list[i]
            i += 1
    return max


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Determine is two given lists are identical."""
    """Return false automatically if the two lists aren't the same length."""
    if len(list_one) != len(list_two):
        return False
    """Establish needed variables for the function."""
    i: int = 0
    length: int = len(list_one)
    same: bool = True 
    """Scan through list and check if the values in the two lists at matching indexes are identical."""
    while i < length:
        if list_one[i] == list_two[i]:
            same = True
            i += 1
        else:
            same = False
            return same
    return same