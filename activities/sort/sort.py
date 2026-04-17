"""Sort a list."""

import random
import time

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

def time_sort(n : int) -> float:
    """Return the number of seconds that it takes to count the number of triples
    in an array of `n` integers.
    """
    a = gen_array_of_random_ints(n)
    start = time.time()
    sort(a)
    end = time.time()
    return end - start

def gen_array_of_random_ints(n : int) -> list[int]:
    xs = []
    for _ in range(n):
        xs.append(random.randint(-100_000, +100_000))
    return xs

def main():
    """Display the impact on a function's running time when doubling the input
    size.
    """
    n = 16
    prev = time_sort(n)
    print('{:>9} {:>6}'.format('n', 'ratio'))
    while True:
        n *= 2
        next = time_sort(n)
        print('{:-9} {:-6.1f}'.format(n, next/prev))
        prev = next

if __name__ == '__main__':
    main()
