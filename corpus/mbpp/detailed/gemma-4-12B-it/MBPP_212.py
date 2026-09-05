import math
from typing import List

def fourth_Power_Sum(n: int) -> int:
    """
    Calculates the sum of the fourth powers of the first n natural numbers.
    The sequence of natural numbers is considered to be 1, 2, 3, ..., n.

    The sum is defined as: 1^4 + 2^4 + 3^4 + ... + n^4.

    Args:
        n (int): The upper limit of the natural numbers to sum.

    Returns:
        int: The sum of the fourth powers of natural numbers from 1 to n.

    Raises:
        ValueError: If n is not a non-negative integer.
        TypeError: If n is not an integer.
    """
    # Step 1: Validate the input type
    if not isinstance(n, int):
        raise TypeError(f"Input 'n' must be an integer. Received: {type(n).__name__}")

    # Step 2: Validate the input value
    # Natural numbers in this context start from 1. 
    # If n is 0, the sum is mathematically defined as 0 (empty sum).
    # Negative numbers are not natural numbers.
    if n < 0:
        raise ValueError(f"Input 'n' must be a non-negative integer. Received: {n}")

    # Handle the degenerate case where n is 0
    if n == 0:
        return 0

    # Step 3: Calculate the sum
    # We can calculate this iteratively to ensure clarity and handle large n safely.
    # Alternatively, one could use the mathematical formula:
    # Sum = (n * (n + 1) * (2n + 1) * (3n^2 + 3n - 1)) / 30

    total_sum: int = 0

    for current_number in range(1, n + 1):
        # Calculate the fourth power: x^4
        # We use exponentiation operator ** or math.pow, 
        # but ** is preferred for returning an integer.
        fourth_power = current_number ** 4

        # Accumulate the result
        total_sum += fourth_power

    return total_sum

if __name__ == "__main__":
    # The following assertions verify the logic against the problem requirements.
    # 1^4 + 2^4 = 1 + 16 = 17
    assert fourth_Power_Sum(2) == 17

    # 1^4 + 2^4 + 3^4 + 4^4 = 1 + 16 + 81 + 256 = 354
    assert fourth_Power_Sum(4) == 354

    # 1^4 + 2^4 + 3^4 + 4^4 + 5^4 + 6^4 = 354 + 625 + 1296 = 2275
    assert fourth_Power_Sum(6) == 2275