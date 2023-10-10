"""Ex04 - Learning List Utility Functions!"""
__author__ = "730648328"

def all(int_list: list[int], num: int) -> bool:
    if len(int_list) == 0:
        return False
    i: int = 0
    same: bool = True
    while i < len(int_list):
        if int_list[i] == num:
            same = True
            i += 1
        else:
            same = False 
            return same
    if same is True:
        return True


def max(int_list: list[int]) -> int:
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = int_list[0]
    i: int = 0
    while i < len(int_list):
        if int_list[i] > max:
            max = int_list[i]
    return max


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    if len(list_one) != len(list_two):
        return False
    i: int = 0
    length: int = len(list_one)
    same: bool = True 
    while i < length:
        if list_one[i] == list_two[i]:
            same = True
            i += 1
        else:
            same = False
            return same
    return same