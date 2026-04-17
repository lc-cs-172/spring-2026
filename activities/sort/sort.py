"""Sort a list."""

def one_pass(a : list[int], i : int):
    """Assume `a` is a list of integers with at least two elements and `i` is
    less than `len(a) - 1`.
    
    What does this function do?

    Try with `a = [5, 4, 3, 2, 1, 0]` and different values for `i` starting with
    `0`.
    
    What would be a better name for local variable `x` to reflect its role?
    """
    # Precondition: len(n) >= 2 and i >= 0 and i < len(n) - 1
    n = len(a)
    x = i
    j = i + 1
    while j < n:
        if a[j] < a[x]:
            x = j
        j += 1
    # Postcondition: x s.t. min(a[i:]) = a[x]
    a[i], a[x] = a[x], a[i]
    # Postcondition: min(a[i:]) = a[i]

def sort(a: list[int]):
    """Sort the elements in a in ascending order."""
    n = len(a)
    i = 0
    # Invariant: is_sorted(a[0:i+1])
    for i in range(n - 1):
        one_pass(a, i)
