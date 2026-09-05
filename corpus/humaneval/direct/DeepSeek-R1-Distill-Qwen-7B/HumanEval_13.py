def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers a and b.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)