def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    This function handles edge cases explicitly and uses the Euclidean algorithm for efficient computation.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Handle edge cases where either number is zero
    if a == 0:
        if b == 0:
            raise ValueError("Both a and b cannot be zero.")
        return abs(b)
    if b == 0:
        return abs(a)

    # Use Euclidean algorithm to compute GCD
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a