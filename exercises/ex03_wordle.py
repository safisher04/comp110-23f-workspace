"""Ex03 - Wordle - Full Program!"""
__author__ = "730648328"


def contains_char(word: str, char: str) -> bool:
    """Search through a given word and return True if char is found and False if char isn't found."""
    assert len(char) == 1
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        else:
            i += 1
    return False


def emojified(user_guess: str, secret: str) -> str:
    """Determine the emoji representation of the users guess in comparison to the secret word."""
    """Define variables"""
    emoji_result: str = ""
    i: int = 0
    find_letter: bool = False
    green: str = "\U0001F7E9"
    yellow: str = "\U0001F7E8"
    white: str = "\U00002B1C"
    
    """Search through secret word for matching chars from the user guess"""
    assert len(user_guess) == len(secret)
    while i < len(secret):
        if user_guess[i] == secret[i]:
            emoji_result = emoji_result + green
        else:
            find_letter = contains_char(secret, user_guess[i])
            if find_letter:
                emoji_result = emoji_result + yellow
            else:
                emoji_result = emoji_result + white
        i += 1
    return emoji_result


def input_guess(length: int) -> str:
    """Prompt the user for a word until the user gives a word of the approriate length."""
    user_guess: str = input(f"Enter a { length } character word: ")
    while len(user_guess) != length:
        user_guess = input(f"That wasn't { length } chars! Try again: ")
    return user_guess


def main() -> None:
    """Give the user 6 tries to guess the secret word giving them hints in the form of an emoji string."""
    """Define variables"""
    attempts: int = 1
    secret: str = "codes"

    """Run the game"""
    while attempts <= 6:
        print(f"=== Turn { attempts }/6 ===")
        guess: str = input_guess(len(secret))
        emoji_guess: str = emojified(guess, secret)
        print(emoji_guess)
        if guess == secret:
            print(f"You won in { attempts }/6 turns!")
            quit()
        attempts += 1
    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    """Makes the main function usable on it's own"""
    main()

