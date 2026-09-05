from typing import List

def _is_odd(number: int) -> bool:
    """
    Determines if an integer is odd.

    Args:
        number: The integer to check.

    Returns:
        True if the number is odd, False otherwise.
    """
    # Using modulo operator: an odd number divided by 2 leaves a remainder of 1 or -1.
    # In Python, % 2 returns 1 for odd positive and odd negative numbers.
    return number % 2 != 0

def _is_even_position(index: int) -> bool:
    """
    Determines if an index is even.
    In the context of the problem (0-based indexing),
    even positions are 0, 2, 4, etc.

    Args:
        index: The index to check.

    Returns:
        True if the index is even, False otherwise.
    """
    return index % 2 == 0

def solution(lst: List[int]) -> int:
    """Given a non-empty list of integers, return the sum of all of the odd elements 
    that are in even positions (0, 2, 4, ...).

    Examples:
    solution([5, 8, 7, 1]) ==> 5 + 7 = 12
    solution([3, 3, 3, 3, 3]) ==> 3 + 3 + 3 = 9
    solution([30, 13, 24, 321]) ==> 0 (none of the even positions contain odd numbers)
    """
    # --- Input Validation ---
    if lst is None:
        raise ValueError("Input list cannot be None.")

    if len(lst) == 0:
        # The problem states a non-empty list, but we handle empty for robustness.
        return 0

    # Verify all elements are integers
    for item in lst:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers. Found: {type(item)}")

    total_sum = 0

    # --- Processing ---
    # We iterate through the list using index-based access to clearly identify positions.
    for current_index in range(len(lst)):
        current_element = lst[current_index]

        # Check if the current position (index) is even.
        # Note: Problem defines "even positions" usually as 0, 2, 4... in 0-indexed logic.
        # Based on examples: 
        # [5, 8, 7, 1] -> index 0 (val 5) is odd, index 2 (val 7) is odd. Sum = 12.
        # This confirms 0-indexed even positions are intended.
        is_position_even = _is_even_position(current_index)

        if is_position_even:
            # Check if the value at this even position is an odd number.
            is_value_odd = _is_odd(current_element)

            if is_value_odd:
                # Accumulate the sum.
                total_sum += current_element

    return total_sum