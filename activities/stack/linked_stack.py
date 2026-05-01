""""Implement a stack data collection that supports the `is_empty`, `push` and
`pop` methods.
"""

class LinkedStack:

    class Node:
        def __init__(self, item, next):
            self._item = item
            self._next = next

    def __init__(self):
        """Initialize an empty stack."""
        pass

    def push(self, item):
        """Push the given item on the stack."""
        pass

    def pop(self):
        """Remove the last item that was pushed onto the stack."""
        pass

    def is_empty(self) -> bool:
        """Return True if the stack contains no item."""
        pass
