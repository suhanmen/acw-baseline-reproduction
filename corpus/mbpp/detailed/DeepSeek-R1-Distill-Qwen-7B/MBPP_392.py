import sys
from functools import lru_cache

sys.setrecursionlimit(100000)

def get_max_sum(n):
    """
    Calculate the maximum sum possible using the given equation.

    Args:
        n (int): The input number.

    Returns:
        int: The maximum sum.

    Raises:
        ValueError: If the input is invalid.
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n == 0:
        return 0

    @lru_cache(maxsize=None)
    def helper(x):
        if x == 0:
            return 0
        elif x in (1, 2):
            return x
        else:
            return max(x, helper(x // 2) + helper(x // 3) + helper(x // 4) + helper(x // 5))

    return helper(n)