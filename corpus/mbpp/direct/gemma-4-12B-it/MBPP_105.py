def count(lst):
    """
    Counts the number of True values in a list of booleans.
    """
    return sum(1 for x in lst if x is True)

if __name__ == "__main__":
    assert count([True, False, True]) == 2
    assert count([False, False]) == 0
    assert count([True, True, True]) == 3