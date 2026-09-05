def _compute_sum_of_divisors(n: int) -> int:
    """
    Computes the sum of all positive divisors of a given integer n.

    This function iterates from 1 up to the square root of n to find divisors.
    For every divisor i found, both i and n // i are added to the sum.
    Special care is taken to avoid double-counting perfect squares.

    Args:
        n: A positive integer greater than 0.

    Returns:
        The sum of all positive divisors of n.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError(f"Input must be a positive integer, got {n}")

    total_sum: int = 0
    limit: int = int(n ** 0.5)

    for candidate in range(1, limit + 1):
        if n % candidate == 0:
            divisor_1: int = candidate
            divisor_2: int = n // candidate

            # Add the first divisor
            total_sum += divisor_1

            # Add the second divisor if it's different from the first
            # (to handle perfect squares correctly)
            if divisor_1 != divisor_2:
                total_sum += divisor_2

    return total_sum

def areEquivalent(n1: int, n2: int) -> bool:
    """
    Checks whether the sum of divisors of two numbers are the same.

    This function calculates the sum of divisors for each number and compares them.
    It handles various edge cases including negative numbers, zero, and non-integers.

    Args:
        n1: The first number to check.
        n2: The second number to check.

    Returns:
        True if the sum of divisors of n1 and n2 are equal, False otherwise.

    Raises:
        ValueError: If either input is not a positive integer.
    """
    # Validate first input
    if not isinstance(n1, int):
        raise ValueError(f"First argument must be an integer, got {type(n1).__name__}")
    if n1 <= 0:
        raise ValueError(f"First argument must be a positive integer, got {n1}")

    # Validate second input
    if not isinstance(n2, int):
        raise ValueError(f"Second argument must be an integer, got {type(n2).__name__}")
    if n2 <= 0:
        raise ValueError(f"Second argument must be a positive integer, got {n2}")

    # Compute sums
    sum1: int = _compute_sum_of_divisors(n1)
    sum2: int = _compute_sum_of_divisors(n2)

    # Compare sums
    return sum1 == sum2