"""Ex02 - Wordle -One try Wordle!"""
__author__ = "730648328"

"""Establishing variables used in the rest of my program"""
secret: str = "python"
len_secret: int = len(secret)
user_guess: str = input("What is your 6 letter guess? ")
i: int = 0
emoji_result: str = ""
same: bool = False
find_match: int = 0
while len(user_guess) != len_secret:
    user_guess = input(f"That was not { len_secret } letters! Try again? ")
while i < len_secret:
    if user_guess[i] == secret[i]:
        emoji_result = emoji_result + "\U0001F7E9"
    else:
        while (not same) and (find_match < len_secret):
            if user_guess[i] == secret[find_match]:
                same = True
            else:
                find_match += 1
        if same:
            emoji_result = emoji_result + "\U0001F7E8"
        else:
            emoji_result = emoji_result + "\U00002B1C"
        same = False
        find_match = 0
    i += 1
print(emoji_result)
if user_guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")