import math

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Step 1: Validate input types.
    # The problem specification implies a and b must be integers.
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")

    # Step 2: Normalize the inputs.
    # The Greatest Common Divisor (GCD) is conventionally a non-negative integer.
    # GCD(a, b) is equivalent to GCD(|a|, |b|).
    abs_a = abs(a)
    abs_b = abs(b)

    # Step 3: Handle degenerate cases for zero.
    # By convention:
    # GCD(0, 0) = 0
    # GCD(x, 0) = |x|
    # GCD(0, x) = |x|
    if abs_a == 0 and abs_b == 0:
        return 0

    if abs_a == 0:
        return abs_b

    if abs_b == 0:
        return abs_a

    # Step 4: Implementation of the Euclidean Algorithm.
    # We use an iterative approach to avoid recursion depth limits.
    # The algorithm relies on the principle that GCD(a, b) = GCD(b, a % b).

    current_a = abs_a
    current_b = abs_b

    while current_b != 0:
        # Calculate the remainder of the division.
        remainder = current_a % current_b

        # Update current_a to the previous divisor.
        current_a = current_b

        # Update current_b to the remainder.
        current_b = remainder

    # After the loop, current_b is 0 and current_a holds the GCD.
    return current_a