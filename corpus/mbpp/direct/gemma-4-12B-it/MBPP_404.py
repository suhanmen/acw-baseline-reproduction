def minimum(a, b):
    """
    Finds the minimum of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The smaller of the two numbers.
    """
    if a < b:
        return a
    else:
        return b

if __name__ == "__main__":
    assert minimum(1, 2) == 1
    assert minimum(-5, -4) == -5
    assert minimum(0, 0) == 0