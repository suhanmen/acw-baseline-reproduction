def power(a, b):
    """
    Calculates the value of 'a' to the power 'b'.

    Args:
        a (int/float): The base.
        b (int): The exponent.

    Returns:
        int/float: The result of a raised to the power b.
    """
    return a ** b

if __name__ == "__main__":
    assert power(3, 4) == 81
    assert power(2, 3) == 8
    assert power(5, 5) == 3125