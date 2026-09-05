def gcd(a, b):
    """
    Compute the greatest common divisor of two positive integers.

    Args:
        a (int): First positive integer.
        b (int): Second positive integer.

    Returns:
        int: The greatest common divisor of a and b.

    Raises:
        ValueError: If either a or b is not a positive integer.
    """
    # Input validation
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both a and b must be integers.")
    if a <= 0 or b <= 0:
        raise ValueError("Both a and b must be positive integers.")

    # Ensure that a is the larger number
    if a < b:
        a, b = b, a

    # Euclidean algorithm
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a

# Test cases
assert gcd(12, 17) == 1, "Test case 1 failed"
assert gcd(4, 6) == 2, "Test case 2 failed"
assert gcd(2, 9) == 1, "Test case 3 failed"
print("All test cases passed successfully")