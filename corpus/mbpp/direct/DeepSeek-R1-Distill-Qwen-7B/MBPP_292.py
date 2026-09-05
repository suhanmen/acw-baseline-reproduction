def find(a, b):
    """
    Return the quotient of two numbers, truncating towards zero.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        int: The quotient of a divided by b, truncated towards zero.
    """
    if b == 0:
        raise ValueError("Divisor cannot be zero.")
    return a // b