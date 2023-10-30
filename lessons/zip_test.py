"""Test my zip funciton."""
__author__ = "730648328"

from lessons.zip import zip


def test_empty_zip() -> None:
    """Zip with empty lists should return and empty dictionary."""
    key_list: list[str] = []
    val_list: list[int] = []
    assert zip(key_list, val_list) == dict()


def test_dict_length():
    """Length of the dictionary should match the length of the lists."""
    key_list: list[str] = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    val_list: list[int] = [1, 2, 3, 4, 5]
    assert len(zip(key_list, val_list)) == 5


def test_grocery_list():
    """A grocery list should return the item and how many are needed."""
    key_list: list[str] = ["apples", "bananas", "eggs"]
    val_list: list[int] = [8, 6, 36]
    assert zip(key_list, val_list) == {"apples": 8, "bananas": 6, "eggs": 36}