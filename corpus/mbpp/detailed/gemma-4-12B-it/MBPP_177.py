import math
from typing import Tuple, List

def get_lcm(a: int, b: int) -> int:
    """
    Calculates the Least Common Multiple (LCM) of two integers.
    Formula: lcm(a, b) = abs(a * b) // gcd(a, b)
    """
    if a == 0 or b == 0:
        return 0

    # Use math.gcd which is efficient and handles negative numbers
    gcd_value = math.gcd(a, b)

    # Perform multiplication before division, but use floor division
    product = abs(a * b)
    lcm_value = product // gcd_value
    return lcm_value

def is_in_range(value: int, lower: int, upper: int) -> bool:
    """
    Checks if a value is within the inclusive range [lower, upper].
    """
    return lower <= value <= upper

def find_two_numbers_with_lcm_in_range(lower_bound: int, upper_bound: int) -> Tuple[int, int]:
    """
    Finds two distinct positive integers (a, b) such that their 
    Least Common Multiple (LCM) falls within the range [lower_bound, upper_bound].

    The function prioritizes finding the smallest possible pair by iterating
    through potential integers.

    Args:
        lower_bound (int): The lower limit of the LCM range (inclusive).
        upper_bound (int): The upper limit of the LCM range (inclusive).

    Returns:
        Tuple[int, int]: A pair of distinct integers.

    Raises:
        ValueError: If the range is invalid or no pair is found.
    """
    # Input Validation
    if not isinstance(lower_bound, int) or not isinstance(upper_bound, int):
        raise ValueError("Bounds must be integers.")

    if lower_bound > upper_bound:
        raise ValueError("Lower bound cannot be greater than upper bound.")

    # Strategy:
    # We need to find two distinct positive integers a and b.
    # To ensure we find a pair efficiently, we can iterate through 
    # possible values of 'a' and 'b'.
    # Given the test cases:
    # (3, 8) -> (3, 6) | LCM(3, 6) = 6. 6 is in [3, 8].
    # (2, 6) -> (2, 4) | LCM(2, 4) = 4. 4 is in [2, 6].
    # (1, 3) -> (1, 2) | LCM(1, 2) = 2. 2 is in [1, 3].

    # The search space: 
    # Since we need LCM <= upper_bound, both a and b must be <= upper_bound.
    # We look for the smallest distinct positive integers.

    # We iterate through possible values for 'a' starting from 1.
    # We iterate through possible values for 'b' starting from a + 1.
    # This ensures 'a' and 'b' are distinct and we find the "first" smallest pair.

    # We set a reasonable upper limit for the search to prevent infinite loops,
    # though for these bounds, the answer will be found very quickly.
    max_search_limit = upper_bound + 1

    for a in range(1, max_search_limit):
        for b in range(a + 1, max_search_limit):
            current_lcm = get_lcm(a, b)

            if is_in_range(current_lcm, lower_bound, upper_bound):
                # Return the first pair found that satisfies the condition.
                # Based on test cases, we return them in ascending order.
                return (a, b)

    # If no pair is found after exhaustive search
    raise ValueError("No distinct pair found within the specified LCM range.")

def answer(lower_bound: int, upper_bound: int) -> Tuple[int, int]:
    """
    Wrapper function to match the required signature.
    """
    # Defensive check for negative bounds or zeros which might complicate LCM
    if lower_bound < 1:
        # If the problem implies positive integers, we treat range as starting from 1
        # Otherwise, we proceed with the logic.
        pass

    return find_two_numbers_with_lcm_in_range(lower_bound, upper_bound)