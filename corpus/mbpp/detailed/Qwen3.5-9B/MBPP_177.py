import math
from typing import Optional, Tuple, Union

Number = Union[int, float]

def gcd(a: Number, b: Number) -> Number:
    """
    Compute the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.

    Handles negative numbers by taking the absolute value before computation.
    Returns 0 if both inputs are 0.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float).")

    # Convert to integers if they are floats, assuming they represent integers.
    # If non-integer floats are passed, we convert them to int for GCD logic, 
    # though strictly GCD is defined for integers. 
    # For the sake of the problem (which implies integers), we proceed with int conversion.
    int_a = int(a)
    int_b = int(b)

    a_val = abs(int_a)
    b_val = abs(int_b)

    while b_val != 0:
        temp = b_val
        b_val = a_val % b_val
        a_val = temp

    return int(a_val)


def lcm(a: Number, b: Number) -> Number:
    """
    Compute the Least Common Multiple (LCM) of two numbers.
    LCM(a, b) = |a * b| / GCD(a, b)
    Returns 0 if both inputs are 0.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float).")

    int_a = int(a)
    int_b = int(b)

    # If both are zero, LCM is undefined or 0 depending on context, but mathematically 0.
    if int_a == 0 and int_b == 0:
        return 0

    common_divisor = gcd(int_a, int_b)

    # Calculate product first, then divide by GCD to avoid floating point issues if possible.
    # Since inputs are integers, the result will be an integer.
    product = int_a * int_b
    result = product // common_divisor

    # Ensure the result is non-negative if inputs were mixed signs, 
    # though LCM is typically defined for positive integers in this context.
    return abs(result)


def find_pair_in_range(min_val: Number, max_val: Number) -> Optional[Tuple[int, int]]:
    """
    Finds two distinct integers within the range [min_val, max_val] (inclusive)
    such that their LCM is also within the range [min_val, max_val].

    Returns the tuple (n, m) where n < m.
    If no such pair exists, returns None.

    Constraints:
    1. n and m must be distinct.
    2. min_val <= n < m <= max_val.
    3. min_val <= lcm(n, m) <= max_val.
    """
    # Input Validation
    if not isinstance(min_val, (int, float)) or not isinstance(max_val, (int, float)):
        raise TypeError("Range boundaries must be numbers (int or float).")

    lower_bound = int(min_val)
    upper_bound = int(max_val)

    # Ensure bounds make sense
    if lower_bound > upper_bound:
        raise ValueError("Lower bound must be less than or equal to upper bound.")

    # Normalize to integers. If the input allows non-integers, we assume the 
    # numbers sought are integers within this inclusive range.
    # We work with integers for the search space.

    # Edge Case: If the range contains fewer than 2 integers, no distinct pair exists.
    if lower_bound == upper_bound:
        return None

    # Convert to inclusive integer list range if necessary, 
    # but iterating is better than creating a list for large ranges.

    # Search Strategy:
    # We need n and m such that lcm(n, m) <= max_val.
    # Since lcm(n, m) >= max(n, m), we must have max(n, m) <= max_val.
    # Also, lcm(n, m) >= min_val (usually true if n, m >= min_val and not 0/1 edge cases where lcm=1 < min_val).

    # Special handling for 0 or negative numbers:
    # LCM is typically defined for positive integers. 
    # If min_val <= 0, we need to decide behavior. 
    # Given the problem examples (positive integers), we assume positive integers.
    # If negative numbers are allowed, lcm is usually positive.
    # Let's assume the search space for n and m is the intersection of [min_val, max_val] and [1, infinity).

    search_start = max(1, lower_bound)
    search_end = upper_bound

    if search_start > search_end:
        # No positive integers in the range
        return None

    # Iterate through possible values for n
    for n in range(search_start, search_end + 1):
        # Iterate through possible values for m where m > n
        for m in range(n + 1, search_end + 1):
            current_lcm = lcm(n, m)

            # Check if LCM is within the range [min_val, max_val]
            if current_lcm >= lower_bound and current_lcm <= upper_bound:
                # We found a valid pair
                return (n, m)

    # If no pair is found after checking all combinations
    return None


def answer(min_val: Number, max_val: Number) -> Tuple[int, int]:
    """
    Wrapper function to find two distinct numbers such that their lcm lies within the given range.

    This function calls find_pair_in_range and asserts that a solution is found as per 
    the problem description implying a solution always exists for valid inputs.

    Args:
        min_val: The lower bound of the range (inclusive).
        max_val: The upper bound of the range (inclusive).

    Returns:
        A tuple (n, m) of distinct integers within [min_val, max_val] 
        such that lcm(n, m) is also within [min_val, max_val].

    Raises:
        AssertionError: If no solution is found for the given inputs (should not happen per problem constraints).
    """
    result = find_pair_in_range(min_val, max_val)

    if result is None:
        raise AssertionError(f"No distinct pair found with LCM in range [{min_val}, {max_val}].")

    return result