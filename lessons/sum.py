"""Summing the elements of a list using different loops."""
__author__ = "730648328"


def w_sum(vals: list[float]) -> float:
    """Sum the elements of a list with a while loop."""
    i: int = 0
    sum: float = 0.0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sum the elements of a list with a for/in loop."""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sum the elements of a list with a for/in loop using range."""
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum