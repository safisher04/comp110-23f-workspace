"""Ex01 - Chardle - First step towards Wordle!"""
__author__ = "730648328"

"""Get the users input"""
user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
user_char: str = input("Enter a single character: ")
if len(str(user_char)) != 1:
    print("Error: Charcter must be a single character")
    exit()
print("Searching for " + user_char + " in " + user_word)

"""Check and count indices"""
num_indices: int = 0
if user_word[0] == user_char:
    print(user_char + " found at index 0")
    num_indices += 1
if user_word[1] == user_char:
    print(user_char + " found at index 1")
    num_indices += 1
if user_word[2] == user_char:
    print(user_char + " found at index 2")
    num_indices += 1
if user_word[3] == user_char:
    print(user_char + " found at index 3")
    num_indices += 1
if user_word[4] == user_char:
    print(user_char + " found at index 4")
    num_indices += 1
if num_indices > 1:
    print(str(num_indices) + " instances of " + user_char + " found in " + user_word)
if num_indices == 1:
    print(str(num_indices) + " instance of " + user_char + " found in " + user_word)
if num_indices == 0:
    print("No instances of " + user_char + " found in " + user_word)