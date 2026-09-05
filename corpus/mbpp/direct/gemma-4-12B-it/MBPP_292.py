def find(a, b):
    """
    Finds the quotient of two numbers.

    Args:
        a (int/float): The dividend.
        b (int/float): The divisor.

    Returns:
        int: The integer quotient of a divided by b.
    """
    return a // b

if __name__ == "__main__":
    assert find(10, 3) == 3
    assert find(4, 2) == 2
    assert find(20, 5) == 4