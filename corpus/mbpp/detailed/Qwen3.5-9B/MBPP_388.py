from typing import Union, Optional


def _is_valid_integer(value: Union[int, float], name: str = "value") -> bool:
    """
    Validate that the input is an integer and non-negative.

    This function checks two conditions:
    1. The value must be an integer type.
    2. The value must be greater than or equal to zero.

    It raises a ValueError with a descriptive message if either condition is violated.
    """
    if not isinstance(value, int):
        raise ValueError(
            f"Input '{name}' must be an integer, but got type {type(value).__name__}"
        )

    if value < 0:
        raise ValueError(
            f"Input '{name}' must be non-negative (>= 0), but got {value}"
        )

    return True


def _find_highest_power_of_two(n: int) -> int:
    """
    Find the highest power of 2 that is less than or equal to n.

    Algorithm:
    1. Start with a power variable set to 1 (2^0).
    2. While the next power of 2 (current * 2) is less than or equal to n:
       - Multiply the current power by 2.
    3. Return the final power.

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Examples:
    - highest_power_of_two(10) -> 8 (since 8 <= 10 and 16 > 10)
    - highest_power_of_two(32) -> 32
    - highest_power_of_two(0) -> 0 (special case handled before this function in main)
    - highest_power_of_two(1) -> 1
    """
    # Special case for 0: No power of 2 is less than or equal to 0 except if we consider 0 itself,
    # but mathematically 2^k = 0 has no solution. However, based on problem constraints 
    # and typical expectations for this type of problem, if n=0, we might expect 0 as the result
    # because 0 is not a power of 2, but it is the highest value <= 0 that could be returned 
    # if we strictly follow "less than or equal". However, usually this problem implies positive integers.
    # Given the assertions provided (10->8, 19->16, 32->32), n is always >= 1.
    # If n is 0, mathematically there is no power of 2 <= 0. 
    # But to provide a deterministic return value, we will return 0 for input 0.
    if n == 0:
        return 0

    # Initialize the current power of 2. 
    # We start at 1 because 2^0 = 1 is the smallest positive power of 2.
    current_power = 1

    # Loop condition: Check if doubling the current power exceeds n.
    # We continue as long as (current_power * 2) is less than or equal to n.
    while (current_power * 2) <= n:
        current_power = current_power * 2

    # Return the highest power of 2 found
    return current_power


def highest_Power_of_2(n: int) -> int:
    """
    Public interface to find the highest power of 2 less than or equal to n.

    This function wraps _is_valid_integer and _find_highest_power_of_two 
    to provide input validation and error handling.

    Args:
        n (int): The input integer. Must be non-negative.

    Returns:
        int: The highest power of 2 less than or equal to n.

    Raises:
        ValueError: If n is not an integer or is negative.
        TypeError: If n is None (handled by isinstance check).
    """
    # Step 1: Validate the input
    _is_valid_integer(n)

    # Step 2: Compute the result using the helper function
    result = _find_highest_power_of_two(n)

    # Step 3: Return the result
    return result