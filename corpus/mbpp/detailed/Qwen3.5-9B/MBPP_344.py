from math import sqrt, floor
from typing import Tuple

def validate_and_adjust_bounds(start: int, end: int) -> Tuple[int, int]:
    """
    Validates the input integers and ensures that the valid range [min_val, max_val]
    is computed. If inputs are invalid (non-integers, or out of reasonable bounds for this problem logic),
    we raise a ValueError. We also normalize so that min <= max.

    Edge cases handled:
      - Empty range (start > end): returns (start, end) but loop will be empty.
      - Single element: start == end.
      - Negative numbers: allowed, but logic must hold.
      - Large numbers: Python handles arbitrary precision, but we must be efficient.
      - Non-integer inputs: will be caught by type check if strict, but here we assume int input per problem context.
      - If start or end are not ints, we raise TypeError.

    For the purpose of this function, we assume start and end are integers.
    We adjust so that lower_bound <= upper_bound.
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Both start and end must be integers.")

    # Determine the effective range boundaries
    if start > end:
        lower_bound, upper_bound = start, end
    else:
        lower_bound, upper_bound = start, end

    return lower_bound, upper_bound


def count_odd_factors(n: int) -> int:
    """
    Counts the number of odd factors (divisors) for a given integer n.

    Mathematical Insight:
      Any integer n can be written as n = 2^k * m, where m is odd.
      The factors of n are of the form 2^a * d, where 0 <= a <= k and d is a divisor of m.
      For a factor to be odd, we must have a = 0. Therefore, the odd factors of n are exactly the divisors of m.

      So, the number of odd factors of n is equal to the number of divisors of m (the odd part of n).

    Steps:
      1. Remove all factors of 2 from n to get m.
      2. Count the divisors of m.

    Edge cases:
      - n = 0: By definition, 0 has infinite divisors, but in this context (counting odd factors), 
        it is undefined or infinite. However, typical programming problems avoid 0 or define it as 0.
        Given the problem constraints (small ranges in examples), we assume n != 0.
        We will handle n=0 by returning 0 to avoid infinity, as it has no finite odd factors in practical terms.
      - n < 0: The number of odd factors is the same as for |n| because -1 does not affect divisor count (divisors are usually considered positive).
        We will use absolute value.
    """
    if n == 0:
        return 0

    # Work with absolute value to handle negative numbers
    n = abs(n)

    # Step 1: Remove all factors of 2 to get the odd part m
    while n % 2 == 0:
        n //= 2

    # Step 2: Count divisors of the odd part m
    # We iterate from 1 up to sqrt(m).
    count = 0
    limit = floor(sqrt(n))

    i = 1
    while i <= limit:
        if n % i == 0:
            # i is a divisor
            count += 1
            # Check if the corresponding pair (n // i) is different from i
            pair = n // i
            if pair != i:
                count += 1
        i += 1

    return count


def is_odd_square(x: int) -> bool:
    """
    Checks if a number is an odd perfect square.

    Conditions:
      1. The number must be a perfect square.
      2. The square root must be an odd integer.

    Edge cases:
      - Negative numbers: cannot be perfect squares in real integers -> False.
      - Zero: 0 is a perfect square (0^2=0), but 0 is even -> False.
      - Non-perfect squares: False.
    """
    if x < 0:
        return False

    root = sqrt(x)

    # Check if root is an integer
    if root != floor(root):
        return False

    root_int = int(round(root))

    # Check if the root is odd
    return (root_int % 2) == 1


def count_odd_squares_in_range(start: int, end: int) -> int:
    """
    Counts the number of perfect squares in the inclusive range [start, end] 
    that have an odd number of odd factors.

    Problem Clarification based on assertions:
      The problem asks for "number of elements with odd factors" in a range, but the function name and assertions 
      suggest it might be "number of perfect squares that have an odd number of factors (total or odd?)".

      Let's analyze the assertions:
        count_Odd_Squares(5, 100) == 8
        count_Odd_Squares(8, 65) == 6
        count_Odd_Squares(2, 5) == 1

      Hypothesis 1: Count numbers in [start, end] that are PERFECT SQUARES and have an ODD number of TOTAL FACTORS.
        - A perfect square always has an ODD number of total factors (mathematical property).
          So every perfect square has an odd number of total factors.
          Then we just count perfect squares in the range.

        Let's test Hypothesis 1:
          Range [2, 5]: Perfect squares are 4 (since 2^2=4). Count = 1. Matches assertion.
          Range [5, 100]: Perfect squares are 9, 16, 25, 36, 49, 64, 81, 100. 
                     Note: 4 is less than 5, so excluded. 
                     List: 9, 16, 25, 36, 49, 64, 81, 100 -> 8 squares. Matches assertion.
          Range [8, 65]: Perfect squares: 9, 16, 25, 36, 49, 64. (81 is >65). Count = 6. Matches assertion.

      Conclusion: The problem likely means "Count the number of perfect squares in the range [start, end]".
      Why the name "count_Odd_Squares" and the mention of "odd factors"?
        Because every perfect square has an odd number of total factors.
        The problem statement says "number of elements with odd factors", which in the context of perfect squares 
        uniquely identifies perfect squares (since only perfect squares have an odd number of total factors).

      However, the problem statement says "find number of elements with odd factors", which technically applies to ANY number 
      that has an odd number of factors (which is exactly the set of perfect squares).

      Therefore, the task is: Count integers x in [start, end] such that x is a perfect square.

      We do NOT need to count the number of odd factors for each number. We just need to identify if the number 
      is a perfect square.

      Algorithm:
        Iterate through integers k such that k*k is in [start, end].
        Count how many such k exist.

    Edge cases:
      - start > end: return 0.
      - No perfect squares in range: return 0.
      - start or end negative: perfect squares are non-negative, so negative numbers are ignored.
    """
    # Validate and adjust bounds
    lower_bound, upper_bound = validate_and_adjust_bounds(start, end)

    count = 0

    # We need to find integers k such that:
    #   lower_bound <= k*k <= upper_bound
    # So, k >= sqrt(lower_bound) and k <= sqrt(upper_bound)
    # Also, k must be an integer and k >= 0 (since k*k is the same for -k and k, but we count the number k once for the square value? 
    # Actually, we are counting the ELEMENTS (the squares) in the range, not the roots.
    # But each square corresponds to exactly one non-negative root k.

    # Calculate the smallest integer k such that k*k >= lower_bound
    # We can compute min_k = ceil(sqrt(lower_bound))
    # And max_k = floor(sqrt(upper_bound))

    # Helper to compute ceil sqrt
    def ceil_sqrt(val: int) -> int:
        if val < 0:
            return 0 # No solution for negative
        s = floor(sqrt(val))
        if s * s >= val:
            return s
        return s + 1

    def floor_sqrt(val: int) -> int:
        if val < 0:
            return -1 # No solution
        return floor(sqrt(val))

    min_k = ceil_sqrt(lower_bound)
    max_k = floor_sqrt(upper_bound)

    # Ensure we only consider non-negative k (since k*k for negative k is same as positive, 
    # and we want unique squares in the range, so we only count k >= 0)
    if min_k < 0:
        min_k = 0

    if min_k > max_k:
        return 0

    # Count integers from min_k to max_k (inclusive)
    # This gives the count of unique perfect squares in [lower_bound, upper_bound]
    return max_k - min_k + 1


def count_Odd_Squares(start: int, end: int) -> int:
    """
    Wrapper function to satisfy the exact signature requirement: count_Odd_Squares(start, end).

    Logic:
      This function counts the number of perfect squares in the inclusive range [start, end].
      Rationale: Only perfect squares have an odd number of total factors (divisors).
      Therefore, counting elements with an odd number of factors is equivalent to counting perfect squares.

    Parameters:
      start (int): The lower bound of the range (inclusive).
      end (int): The upper bound of the range (inclusive).

    Returns:
      int: The count of perfect squares in the range [start, end].
    """
    return count_odd_squares_in_range(start, end)