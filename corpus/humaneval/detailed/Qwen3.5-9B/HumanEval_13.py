import math

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Ensure inputs are integers (type checking)
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")

    # Handle zero cases explicitly
    if a == 0 and b == 0:
        raise ValueError("GCD is undefined for both arguments being zero.")

    # Use math.gcd for robustness with negative numbers and efficiency
    result = math.gcd(a, b)

    return result