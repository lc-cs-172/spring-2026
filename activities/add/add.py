def add(a : int, b : int) -> int:
    """Return the sum of two non-negative integers."""
    # Precondition: a >= 0 and b >= 0
    a0 = a
    b0 = b
    # Invariant: a0 + b0 = a + b
    # Ranking: b0
    while b0 > 0:
        a0 = a0 + 1
        b0 = b0 - 1
    # Postcondition: a0 = a + b
    return a0
