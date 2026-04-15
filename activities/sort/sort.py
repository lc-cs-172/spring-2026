def one_pass(a : list[int], i : int):
    """Assume `a` is a list of integers with at least two elements and `i` is
    less than `len(a) - 1`.
    
    What does this function do?

    Try with `a = [5, 4, 3, 2, 1, 0]` and different values for `i` starting with
    `0`.
    
    What would be a better name for local variable `x` to reflect its role?
    """
    n = len(a)
    x = i
    j = i + 1
    while j < n:
        if a[j] < a[x]:
            x = j
        j += 1
    a[i], a[x] = a[x], a[i]
