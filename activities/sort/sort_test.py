import sort

def test_empty():
    a = []
    sort.sort(a)
    assert len(a) == 0

def test_sorted():
    a = [0, 1, 2, 3, 4, 5]
    sort.sort(a)
    assert a == [0, 1, 2, 3, 4, 5]

def test_descending():
    a = [5, 4, 3, 2, 1, 0]
    sort.sort(a)
    assert a == [0, 1, 2, 3, 4, 5]
