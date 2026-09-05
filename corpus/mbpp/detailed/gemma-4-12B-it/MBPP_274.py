import math
from typing import List

def get_binomial_coefficient(n: int, k: int) -> int:
    """
    Calculates the binomial coefficient (n choose k) using the 
    formula: n! / (k! * (n-k)!)

    Args:
        n: The total number of items.
        k: The number of items to choose.

    Returns:
        The number of ways to choose k items from n.

    Raises:
        ValueError: If n or k are negative.
    """
    if n < 0 or k < 0:
        raise ValueError("Input values n and k must be non-negative.")

    if k > n:
        return 0

    # Optimization: (n choose k) is the same as (n choose n-k)
    if k > n // 2:
        k = n - k

    # Use math.comb if available (Python 3.8+), 
    # otherwise implement a stable multiplicative formula.
    if hasattr(math, 'comb'):
        return math.comb(n, k)
    else:
        # Fallback for older Python versions
        numerator = 1
        denominator = 1
        for i in range(k):
            numerator *= (n - i)
            denominator *= (i + 1)
        return numerator // denominator

def even_binomial_Coeff_Sum(n: int) -> int:
    """
    Calculates the sum of binomial coefficients at even indices for a given n.
    The formula is: C(n, 0) + C(n, 2) + C(n, 4) + ...

    Mathematically, this sum is known to be 2^(n-1) for n > 0, 
    and 1 for n = 0.

    Args:
        n: A non-negative integer representing the row of Pascal's triangle.

    Returns:
        The sum of even-indexed binomial coefficients.

    Raises:
        ValueError: If n is a negative integer.
    """
    # 1. Validate Input
    if not isinstance(n, int):
        raise ValueError("Input 'n' must be an integer.")

    if n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")

    # 2. Handle Edge Case: n = 0
    # C(0, 0) is the only coefficient, and 0 is even.
    if n == 0:
        # C(0, 0) = 1
        return 1

    # 3. Calculate the sum iteratively to ensure accuracy and clarity
    # We want to sum C(n, k) where k is 0, 2, 4, ... up to n.
    total_sum = 0

    # We iterate through every index k from 0 to n.
    # If k is even, we add C(n, k) to our total_sum.
    for k in range(n + 1):
        is_even_index = (k % 2 == 0)

        if is_even_index:
            coefficient = get_binomial_coefficient(n, k)
            total_sum += coefficient

    return total_sum