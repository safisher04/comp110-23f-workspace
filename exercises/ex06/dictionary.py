"""Practicing with dictionary functions."""
__author__ = "730648328"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Switch the key and values of the given dictionary.
    
    First check to see if there are repeated values that will cause a key error when switched.
    """
    counter: dict[str, int] = {}
    for key in my_dict:
        val: str = my_dict[key]
        if val in counter:
            counter[val] += 1
        else:
            counter[val] = 1
    for key in counter:
        if counter[key] > 1:
            raise KeyError("There is a repeated value that prevents inversion.")
    """Create the new dictionary with swapped keys and values."""
    new_dict: dict[str, str] = dict()
    for key in my_dict:
        new_key: str = my_dict[key]
        new_val: str = key
        new_dict[new_key] = new_val
    return new_dict


def favorite_color(my_dict: dict[str, str]) -> str:
    """Find which favorite color is most common and return that value."""
    color_count: dict[str, int] = {}
    max_color: int = 0
    most_common: str = ""
    for key in my_dict:
        color: str = my_dict[key]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    for color in color_count:
        if color_count[color] > max_color:
            max_color = color_count[color]
            most_common = color
    return most_common


def count(my_list: list[str]) -> dict[str, int]:
    """Count how many times an item appears in a given list."""
    new_dict: dict[str, int] = {}
    for elem in my_list:
        if elem in new_dict:
            new_dict[elem] += 1
        else:
            new_dict[elem] = 1
    return new_dict


def alphabetizer(my_list: list[str]) -> dict[str, list[str]]:
    """Organize a list by strings that start with the same letter.
    
    First duplicate the given list in all lower case.
    """
    my_dict: dict[str, list[str]] = {}
    for elem in my_list:
        i: int = 0
        all_words: list[str] = []
        while i < len(my_list):
            word: str = elem.lower()
            letter: str = word[0]
            string: str = my_list[i]
            match: str = string.lower()
            if match[0] == letter:
                all_words.append(string)
            i += 1
        if letter not in my_dict:
            my_dict[letter] = all_words
    return my_dict


def update_attendance(my_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Add a student to the attendence based on the day they were there."""
    update_dict = my_dict
    if day in update_dict:
        if student in update_dict[day]:
            return update_dict
        else:
            attending: list[str] = update_dict[day]
            attending.append(student)
            update_dict[day] = attending
    else:
        alone: list[str] = [student]
        update_dict[day] = alone
    return update_dict