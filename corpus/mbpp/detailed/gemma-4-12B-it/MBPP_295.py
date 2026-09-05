import math
from typing import List

def sum_div(n: int) -> int:
    """
    Calculates the sum of all proper divisors of a given integer n.
    A proper divisor is a divisor of n excluding n itself.

    For example:
    - sum_div(8) -> 1 + 2 + 4 = 7
    - sum_div(12) -> 1 + 2 + 3 + 4 + 6 = 16
    - sum_div(7) -> 1
    - sum_div(1) -> 0 (1 has no proper divisors)
    """

    # Input Validation
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received: {type(n).__name__}")

    # Handle cases where divisor logic doesn't apply normally
    if n < 0:
        # The problem doesn't specify negative behavior, but standard 
        # practice for divisor sums is to use the absolute value.
        n = abs(n)

    # A number less than 2 has no proper divisors (as n itself is excluded)
    if n < 2:
        return 0

    # We will store divisors in a set to avoid duplicates (e.g., if n is a perfect square)
    # However, using a list and handling the square root logic correctly is more efficient.
    divisors_sum: int = 0

    # The largest possible proper divisor is n // 2.
    # We can find all divisors by iterating up to the square root of n.
    # If 'i' is a divisor, then 'n / i' is also a divisor.
    limit = int(math.isqrt(n))

    for i in range(1, limit + 1):
        # Check if i is a divisor
        if n % i == 0:
            # 'i' is a divisor
            divisors_sum += i

            # Find the paired divisor: n // i
            paired_divisor = n // i

            # We must ensure:
            # 1. The paired_divisor is not the same as i (prevents double-counting square roots)
            # 2. The paired_divisor is not the original number n (proper divisors exclude n)
            if paired_divisor != i and paired_divisor != n:
                divisors_sum += paired_divisor

    return divisors_sum

# Testing the logic against provided assertions
if __name__ == "__main__":
    # These assertions are provided in the prompt to verify correctness
    assert sum_div(8) == 7
    assert sum_div(12) == 16
    assert sum_div(7) == 1

    # Additional edge case testing
    assert sum_div(1) == 0
    assert sum_div(0) == 0
    assert sum_div(2) == 1
    assert sum_div(4) == 3  # 1 + 2
    assert sum_div(16) == 15 # 1 + 2 + 4 + 8