"""File to define Fish class."""
__author__ = "730648328"


class Fish:
    """Create an object: Fish wiht the attribute age."""
    age: int

    def __init__(self, age_init: int = 0):
        """Initiate the age of the fish."""
        self.age = age_init
        return None
    
    def one_day(self):
        """After one day increase the age of the fish by one."""
        self.age += 1
        return None