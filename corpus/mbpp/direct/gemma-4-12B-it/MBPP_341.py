def set_to_tuple(input_set: set) -> tuple:
    """
    Converts a set into a sorted tuple of its elements.
    """
    return tuple(sorted(list(input_set)))

if __name__ == "__main__":
    assert set_to_tuple({1, 2, 3, 4, 5}) == (1, 2, 3, 4, 5)
    assert set_to_tuple({6, 7, 8, 9, 10, 11}) == (6, 7, 8, 9, 10, 11)
    assert set_to_tuple({12, 13, 14, 15, 16}) == (12, 13, 14, 15, 16)