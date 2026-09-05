def tuple_to_int(t: tuple) -> int:
    """
    Converts a tuple of positive integers into a single integer.
    Example: (1, 2, 3) -> 123
    """
    return int(''.join(map(str, t)))

if __name__ == "__main__":
    assert tuple_to_int((1,2,3))==123
    assert tuple_to_int((4,5,6))==456
    assert tuple_to_int((5,6,7))==567