"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730648328"


class River:
    """Create an object: River with attributes days, bears, and fish."""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check the age of the bear and remove it if it's older than 5."""
        checking_bears: list[Bear] = self.bears
        for bear in self.bears:
            if bear.age > 5:
                checking_bears.pop(checking_bears.index(bear))
        self.bears = checking_bears
        """Check the age of the fish and remove it if it's older than 3."""
        checking_fish: list[Fish] = self.fish
        for fish in self.fish:
            if fish.age > 3:
                checking_fish.pop(checking_fish.index(fish))
        self.fish = checking_fish
        return None
    
    def remove_fish(self, amount: int):
        """Remove a certain number of fish from the beginning of the fish list."""
        fish_list = self.fish
        for val in range(0, amount):
            fish_list.pop(0)
        return None

    def bears_eating(self):
        """Whenever a bear eats, remove the number of fish it eats and increase it's hunger score."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Check the bear's hunger score and remove it if it's less than zero."""
        checking_bears: list[Bear] = self.bears
        for bear in self.bears:
            if bear.hunger_score < 0:
                checking_bears.pop(checking_bears.index(bear))
        self.bears = checking_bears
        return None
        
    def repopulate_fish(self):
        """Account for fish reproduction."""
        n: int = len(self.fish)
        babies: int = (n // 2) * 4
        for x in range(0, babies):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Account for bear reproduction."""
        n: int = len(self.bears)
        babies: int = n // 2
        for x in range(0, babies):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Print the day, fish population, and bear population of the river."""
        output: str = f"~~~ Day {self.day}: ~~~\n"
        output += f"Fish population: {len(self.fish)}\n"
        output += f"Bear population: {len(self.bears)}\n"
        print(output)
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        while self.day < 7:
            self.one_river_day()
        return None
            
