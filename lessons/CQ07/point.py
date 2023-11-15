"""Practicing with class objects."""
from __future__ import annotations
__author__ = "730648328"


class Point:
    """Create an object: Point with x and y coordinates."""

    x: int | float
    y: int | float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """My constructors."""
        self.x = x_init
        self.y = y_init
        
    def scale_by(self, factor: int) -> None:
        """Change the original point by a scale."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """Create a new point at a scale of the original without changing the original."""
        new_x = self.x * factor
        new_y = self.y * factor
        new_point: Point = Point(new_x, new_y)
        return new_point
    
    def __mul__(self, factor: int | float) -> Point:
        """Overload the multiplication operator."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, increase: int | float) -> Point:
        """Overload the addition operator."""
        new_point: Point = Point(self.x + increase, self.y + increase)
        return new_point

    def __str__(self) -> str:
        """Print out points in a readable way."""
        return f"x: {self.x}; y: {self.y}"