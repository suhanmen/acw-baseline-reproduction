import math

def count_Odd_Squares(low: int, high: int) -> int:
    """
    Count numbers in [low, high] that have an odd number of factors.
    A number has an odd number of factors if and only if it is a perfect square.
    """
    if low > high:
        return 0

    low = max(low, 1)  # Factors are defined for positive integers; ignore non-positive.
    high = min(high, 10**18)  # Cap to avoid overflow in sqrt if inputs are huge.

    start = math.isqrt(low - 1) + 1
    end = math.isqrt(high)

    return max(0, end - start + 1)