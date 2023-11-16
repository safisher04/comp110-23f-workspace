"""File to define Bear class."""
__author__ = "730648328"


class Bear:
    """Create an object: Bear with the attributes age and hunger_score."""
    age: int
    hunger_score: int

    def __init__(self, age_init: int = 0, hunger_score_init: int = 0):
        """Initiate the age and hunger score of the bear."""
        self.age = age_init
        self.hunger_score = hunger_score_init
        return None
    
    def one_day(self):
        """After one day increase the age of the bear by one and decrease the hunger score of the bear by one."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increase the bears hunger score by how many fish it ate."""
        self.hunger_score += num_fish
        return None