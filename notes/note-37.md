# Note 37

## Data collection building blocks

### Primitive arrays

Using Python's convenient list syntax:

Operation                       | Syntax
-|-
Allocate an array of length $n$ | `a = [None] * n`
Access element $i$              | `a[i]`
Set element $i$ to $x$          | `a[i] = x`
Get the length of an array      | `len(a)`

### Linked lists

```python
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
```
