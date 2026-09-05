def count_X(tup, x):
    """
    Counts the occurrences of an element x in a tuple tup.
    """
    count = 0
    for item in tup:
        if item == x:
            count += 1
    return count

if __name__ == "__main__":
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4) == 0
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 10) == 3
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 8) == 4