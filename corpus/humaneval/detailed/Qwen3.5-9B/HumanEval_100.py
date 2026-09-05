from typing import List, Optional
import math

def _is_non_negative_integer(value: object) -> bool:
    """
    Check if the value is a non-negative integer.
    Accepts int >= 0. Rejects negative numbers, floats, strings, None, etc.
    """
    if not isinstance(value, int):
        return False
    if value < 0:
        return False
    return True

def _is_odd(number: int) -> bool:
    """
    Check if a number is odd.
    Assumes the input is already an integer.
    """
    return number % 2 != 0

def _get_next_odd(current: int) -> int:
    """
    Given an odd integer `current`, return the next odd integer after it.
    Example: _get_next_odd(3) -> 5
    """
    return current + 2

def _get_next_even(current: int) -> int:
    """
    Given an even integer `current`, return the next even integer after it.
    Example: _get_next_even(2) -> 4
    """
    return current + 2

def _validate_input(n: object) -> Optional[str]:
    """
    Validate the input n against the problem constraints.
    - Must be an integer.
    - Must be positive (strictly greater than 0).
    Returns None if valid, or an error message string if invalid.
    """
    if not _is_non_negative_integer(n):
        return "Input must be a non-negative integer."
    if n <= 0:
        return "Input must be a positive integer (greater than 0)."
    return None

def _compute_stone_count_for_level(base: int, parity: bool) -> int:
    """
    Compute the number of stones for the next level based on the previous level.

    Parameters:
        base (int): The number of stones in the current level.
        parity (bool): True if 'n' (original input) was odd, False if even.

    Logic:
        - If 'n' was odd, the sequence of stones must be odd numbers.
          We take the next odd number after 'base'.
        - If 'n' was even, the sequence of stones must be even numbers.
          We take the next even number after 'base'.

    Note: The problem statement says "if n is odd/even", referring to the original input n.
    However, the examples and logical flow suggest the parity of the *sequence*
    matches the parity of the *input n*. 
    Since we start with n stones at level 1, and n has a specific parity,
    all subsequent levels must maintain that parity (next odd if odd, next even if even).

    But wait: The example make_a_pile(3) -> [3, 5, 7] confirms:
      - Input 3 (odd).
      - Level 1: 3 (odd).
      - Level 2: 5 (next odd after 3).
      - Level 3: 7 (next odd after 5).

    What if input is even? 
      - Input 4 (even).
      - Level 1: 4 (even).
      - Level 2: 6 (next even after 4).
      - Level 3: 8 (next even after 6).

    So we pass the parity of the original 'n' to determine the sequence type.
    """
    if parity:
        # n was odd, so we need the next odd number
        if base % 2 == 0:
            # This should theoretically not happen if logic is correct,
            # but as a defensive check: if base became even unexpectedly, 
            # we treat it as an error or force correction? 
            # Given the math (starting at odd and adding 2), it won't happen.
            # We will just return base + 1 to make it odd, or assume it's fine.
            # Actually, strictly following "next odd", if we are at 3, next is 5.
            return base + 1 if _is_odd(base + 1) else base + 2
        else:
            return _get_next_odd(base)
    else:
        # n was even, so we need the next even number
        if base % 2 != 0:
            return base + 1 if _is_even(base + 1) else base + 2
        else:
            return _get_next_even(base)

def _is_even(number: int) -> bool:
    """Helper to check evenness."""
    return number % 2 == 0

def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """

    # Step 1: Validate the input immediately.
    validation_error = _validate_input(n)
    if validation_error is not None:
        # Raise a descriptive error rather than returning silently or crashing with a stack trace of a bad type.
        raise ValueError(validation_error)

    # Step 2: Cast the validated input to int (redundant due to validation, but explicit for clarity).
    current_stones: int = int(n)

    # Step 3: Determine the parity of the original input n to dictate the sequence type.
    is_n_odd: bool = _is_odd(current_stones)

    # Step 4: Initialize the result list with the first level.
    stone_levels: List[int] = [current_stones]

    # Step 5: Initialize a variable to keep track of the number of stones in the current level.
    current_level_stones: int = current_stones

    # Step 6: Loop to generate the remaining (n - 1) levels.
    # We have already created the first level, so we need n-1 more.
    for level_index_in_remaining: int in range(1, n):
        # Step 7: Determine the number of stones for the next level based on the parity of the original input.
        next_level_stones: int

        if is_n_odd:
            # If original n was odd, the sequence must be odd numbers.
            # Find the next odd number after current_level_stones.
            # Since current_level_stones is odd, adding 2 gives the next odd.
            next_level_stones = _get_next_odd(current_level_stones)
        else:
            # If original n was even, the sequence must be even numbers.
            # Find the next even number after current_level_stones.
            # Since current_level_stones is even, adding 2 gives the next even.
            next_level_stones = _get_next_even(current_level_stones)

        # Step 8: Append the calculated number of stones to the result list.
        stone_levels.append(next_level_stones)

        # Step 9: Update the current level stones for the next iteration.
        current_level_stones = next_level_stones

    # Step 10: Return the completed list of stone counts.
    return stone_levels