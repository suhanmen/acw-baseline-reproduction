def check_distinct(tup: tuple) -> bool:
    """
    Checks if all elements in the given tuple are distinct.

    Args:
        tup (tuple): A tuple of elements.

    Returns:
        bool: True if all elements are distinct, False otherwise.
    """
    return len(tup) == len(set(tup))

if __name__ == "__main__":
    assert check_distinct((1, 4, 5, 6, 1, 4)) == False
    assert check_distinct((1, 4, 5, 6)) == True
    assert check_distinct((2, 3, 4, 5, 6)) == True