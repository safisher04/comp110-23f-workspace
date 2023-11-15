"""Test for correctness and functionality of my dictionary functions."""
__author__ = "730648328"

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance
import pytest

"""Tests for invert function."""


def test_key_error() -> None:
    """Dictionary with duplicate values should raise a key error."""
    with pytest.raises(KeyError):
        my_dictionary = {"kyle": "banana", "betty": "apple", "josie": "banana"}
        invert(my_dictionary)


def test_swap() -> None:
    """Invert should take a dictionary and swap the keys and values."""
    my_dict = {"kyle": "banana", "betty": "apple"}
    assert invert(my_dict) == {"banana": "kyle", "apple": "betty"}


def test_len() -> None:
    """The inverted dictionary should be the same length as the given dictionary."""
    my_dict = {"luke": "skywalker", "han": "solo", "leia": "organa"}
    assert len(invert(my_dict)) == 3


"""Tests for favorite_color function."""


def test_all_different() -> None:
    """If every key has a different favorite color, the first color should be returned."""
    my_dict = {"jo": "blue", "rachel": "green", "bobby": "red"}
    assert favorite_color(my_dict) == "blue"


def test_empty() -> None:
    """If given an empty dictionary, return an empty string."""
    my_dict = {}
    assert favorite_color(my_dict) == ""


def test_favorite_red() -> None:
    """If red is the most common color, it should be returned."""
    my_dict = {"jo": "red", "beth": "red", "amy": "blue", "meg": "pink", "marmee": "red"}
    assert favorite_color(my_dict) == "red"


"""Tests for count function."""


def test_single_occurence() -> None:
    """If the given list has no repeat values, the dictionary returned should have 1 as the value for each item."""
    my_list = ["apple", "banana"]
    assert count(my_list) == {"apple": 1, "banana": 1}


def test_all_same() -> None:
    """If all the items in the given list are the same, there should only be one key and the val should be the length of the list."""
    my_list = ["happy", "happy", "happy"]
    assert count(my_list) == {"happy": len(my_list)}


def test_names() -> None:
    """Given a list of names, see how many repeats of certain names there are."""
    name_list = ["abby", "joe", "bob", "abby", "jessica", "abby", "bob"]
    assert count(name_list) == {"abby": 3, "joe": 1, "bob": 2, "jessica": 1}


"""Tests for alphabetizer function."""


def test_all_lower() -> None:
    """Test a list with all items entirely lowercase."""
    my_list = ["cat", "candy", "box", "sand", "jump", "belt"]
    assert alphabetizer(my_list) == {"c": ["cat", "candy"], "b": ["box", "belt"], "s": ["sand"], "j": ["jump"]}


def test_all_upper() -> None:
    """Test a list with all items capitalized."""
    my_list = ["Cat", "Dog", "Bunny", "Cake", "Brownie", "Pie"]
    assert alphabetizer(my_list) == {"c": ["Cat", "Cake"], "d": ["Dog"], "b": ["Bunny", "Brownie"], "p": ["Pie"]}


def test_no_groups() -> None:
    """Test a list with no words starting with the same letter to be grouped."""
    my_list = ["cat", "dog", "parrot", "lizard"]
    assert alphabetizer(my_list) == {"c": ["cat"], "d": ["dog"], "p": ["parrot"], "l": ["lizard"]}


"""Tests for update attendance function."""


def test_missing_student() -> None:
    """Update the attendance when there was a student incorrectly marked absent."""
    my_dict = {"Monday": ["Jo", "Beth"]}
    assert update_attendance(my_dict, "Monday", "Sarah") == {"Monday": ["Jo", "Beth", "Sarah"]}


def test_student_alone() -> None:
    """Test updating the attendance on a day that was initially empty."""
    my_dict = {"Monday": ["Jo", "Beth"]}
    assert update_attendance(my_dict, "Tuesday", "Sarah") == {"Monday": ["Jo", "Beth"], "Tuesday": ["Sarah"]}


def test_no_change() -> None:
    """Trying to update the attendance but the student is already marked for that day."""
    my_dict = {"Monday": ["Jo", "Beth"]}
    assert update_attendance(my_dict, "Monday", "Jo") == {"Monday": ["Jo", "Beth"]}