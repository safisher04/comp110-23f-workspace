"""Combining two lists into a dictionary."""

__author__ = "730648328"


def zip(keys: list[str], vals: list[int]) -> dict[str, int]:
    """Take two lists and create a dictionary with the first as the keys and the second as the values."""
    my_dict: dict[str, int] = dict()
    if (len(keys) == 0) or (len(vals) == 0) or (len(keys) != len(vals)):
        return my_dict
    i: int = 0
    for idx in range(0, len(keys)):
        my_dict[keys[i]] = vals[i]
        i += 1
    return my_dict


print(zip(["Happy", "Tuesday"], [1, 2]))