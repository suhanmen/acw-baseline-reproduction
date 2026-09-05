def opposite_Signs(x: int, y: int) -> bool:
    """
    Checks whether the given two integers have opposite signs.

    Args:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        bool: True if the signs are opposite, False otherwise.
    """
    # Two numbers have opposite signs if their product is negative.
    # However, multiplication can overflow in some languages, 
    # so checking the XOR of the sign bits is more robust.
    # In Python, we can simply check if one is non-negative and one is negative,
    # or more simply, if their product is less than zero.
    return (x < 0) != (y < 0)

if __name__ == "__main__":
    assert opposite_Signs(1, -2) == True
    assert opposite_Signs(3, 2) == False
    assert opposite_Signs(-10, -10) == False