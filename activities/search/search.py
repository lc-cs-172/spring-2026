def search(haystack : list[int], needle : int) -> int:
    """Search the array haystack for the value needle. Return -1 if needle is
    not found otherwise the index of an occurrence of needle in haystack. This
    function is O(n)."""
    n = len(haystack)
    for i in range(n):
        if haystack[i] == needle:
            return i
    return -1

def bsearch(haystack : list[int], needle : int) -> int:
    """Search the array haystack for the value needle. haystack is sorted
    (ascending). Return -1 if needle is not found otherwise the index of an
    occurrence of needle in haystack. This function is O(log(n))."""
    n = len(haystack)
    return bsearch_helper(haystack, needle, 0, n)

def bsearch_helper(haystack : list[int], needle : int, lo : int, hi : int) -> int:
    """Search for needle in haystack[lo : hi). haystack is sorted (ascending).
    Return -1 if needle is not found otherwise the index of an occurrence of
    needle in haystack."""
    # Invariant: if the needle is anywhere, it is in haystack[lo : hi)
    if hi <= lo:
        return -1
    mid = (lo + hi) // 2
    if haystack[mid] < needle:
        return bsearch_helper(haystack, needle, mid + 1, hi)
    elif haystack[mid] > needle:
        return bsearch_helper(haystack, needle, 0, mid)
    else:
        return mid
