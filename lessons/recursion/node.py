"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Return the data attribute."""
        return self.data
    
    def tail(self) -> Node | None:
        """Return the non-data attribute."""
        return self.next
    
    def last(self) -> int:
        """Cycle through the linked list till the last item and return that item's data attribute."""
        while self.next is not None:
            self = self.next
        if self.next is None:
            return self.data
