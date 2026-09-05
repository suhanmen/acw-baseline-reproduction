def find(a, b):
    """
    Finds the remainder of the division of two numbers.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        int: The remainder of a divided by b.
    """
    return a % b

if __name__ == "__main__":
    assert find(3, 3) == 0
    assert find(10, 3) == 1
    assert find(16, 5) == 1