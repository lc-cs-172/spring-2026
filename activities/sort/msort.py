"""Merge sort.

Inspired by https://introcs.cs.princeton.edu/java/42sort/Merge.java.html.
"""

import random
import time

def merge(a : list[int], aux : list[int], lo : int, mid : int, hi : int):
    """Merge the sublists a[lo:mid] and a[mid:hi] in a[lo:hi] using the
    auxiliary list.
    Precondition: elements in sublists a[lo:mid] and a[mid:hi] are in ascending
                  order.
    Postcondition: elements in sublist a[lo:hi] are in ascending order.
    """
    i = lo
    j = mid
    for k in range(lo, hi):
        if   i == mid:    aux[k] = a[j]; j += 1
        elif j == hi:     aux[k] = a[i]; i += 1
        elif a[i] < a[j]: aux[k] = a[i]; i += 1
        else:             aux[k] = a[j]; j += 1

    # Copy back
    for k in range(lo, hi):
        a[k] = aux[k]

def sort_helper(a : list[int], aux : list[int], lo : int, hi : int):
    """Sort the sublist a[lo:hi] in ascending order using merge sort."""
    # Base case
    if hi - lo <= 1: return

    # Sort each half, recursively
    mid = (lo + hi)//2
    sort_helper(a, aux, lo, mid)
    sort_helper(a, aux, mid, hi)

    # Merge each half back together
    merge(a, aux, lo, mid, hi)

def sort(a : list[int]):
    """Sort the list in ascending order."""
    n = len(a)
    aux = [0]*n
    sort_helper(a, aux, 0, n)

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
