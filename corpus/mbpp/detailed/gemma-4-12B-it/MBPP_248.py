import math
from typing import Union

def harmonic_sum(n: int) -> float:
    """
    Calculates the harmonic sum of n-1.
    The harmonic sum H_k is defined as the sum of 1/i for i from 1 to k.
    The problem asks for the harmonic sum of n-1, which is H_{n-1}.

    Args:
        n (int): The upper bound for the harmonic calculation (n-1).

    Returns:
        float: The calculated harmonic sum.

    Raises:
        ValueError: If n is less than 1, as n-1 must be at least 0.
                   If n=1, n-1=0, and the sum of an empty range is 0.0.
        TypeError: If n is not an integer.
    """
    # Input Validation: Ensure n is an integer.
    if not isinstance(n, int):
        raise TypeError(f"Input 'n' must be an integer. Received: {type(n).__name__}")

    # Input Validation: Harmonic sum is typically defined for non-negative integers.
    # If n < 1, then n-1 < 0, which is undefined for a standard harmonic sum.
    if n < 1:
        raise ValueError(f"Input 'n' must be at least 1. Received: {n}")

    # Calculate the upper limit of the summation.
    # The problem specifies the harmonic sum of n-1.
    limit = n - 1

    # Handle the degenerate case where n=1.
    # The sum of an empty range (from 1 to 0) is defined as 0.0.
    if limit <= 0:
        return 0.0

    # Initialize the accumulator.
    total_sum: float = 0.0

    # Perform the summation.
    # We iterate from 1 up to and including 'limit'.
    # We use float conversion to ensure floating point division.
    for i in range(1, limit + 1):
        # Defensive check: technically range() handles this, but we ensure 
        # we never divide by zero.
        if i == 0:
            raise ValueError("Division by zero encountered in harmonic sum calculation.")

        current_term: float = 1.0 / float(i)
        total_sum += current_term

    return total_sum

if __name__ == "__main__":
    # Verification against provided assertions
    # H_{7-1} = H_6 = 1/1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6
    # H_6 = 1 + 0.5 + 0.333... + 0.25 + 0.2 + 0.166... = 2.5928571428571425

    # The prompt asks for the sum of n-1.
    # For n=7, calculate H_6.
    # For n=4, calculate H_3.
    # For n=19, calculate H_18.

    res7 = harmonic_sum(7)
    assert math.isclose(res7, 2.5928571428571425), f"Expected 2.5928571428571425, got {res7}"

    res4 = harmonic_sum(4)
    assert math.isclose(res4, 2.083333333333333), f"Expected 2.083333333333333, got {res4}"

    res19 = harmonic_sum(19)
    assert math.isclose(res19, 3.547739657143682), f"Expected 3.547739657143682, got {res19}"