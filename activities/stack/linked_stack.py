""""Implement a stack data collection that supports the `is_empty`, `push` and
`pop` methods.

This collection is iterable.
"""

class LinkedStack:

    class Node:
        def __init__(self, item, next):
            self._item = item
            self._next = next

    def __init__(self):
        """Initialize an empty stack."""
        self._top = None

    def __iter__(self):
        self._iter = self._top
        return self

    def __next__(self):
        if self._iter is None:
            raise StopIteration
        item = self._iter._item
        self._iter = self._iter._next
        return item

    def push(self, item):
        """Push the given item on the stack."""
        self._top = LinkedStack.Node(item, self._top)

    def pop(self):
        """Remove the last item that was pushed onto the stack."""
        item = self._top._item
        self._top = self._top._next
        return item

    def is_empty(self) -> bool:
        """Return True if the stack contains no item."""
        return self._top is None
