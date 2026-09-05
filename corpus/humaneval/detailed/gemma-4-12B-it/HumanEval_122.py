from typing import List


def has_at_most_two_digits(n: int) -> bool:
    """
    Helper function to determine if an integer has at most two digits.

    An integer has at most two digits if its absolute value is 
    between 0 and 99 inclusive.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if the number has 1 or 2 digits, False otherwise.
    """
    # Use absolute value to handle negative numbers correctly (e.g., -9 is one digit)
    absolute_value = abs(n)

    # Numbers from 0 to 99 have at most two digits
    if 0 <= absolute_value <= 99:
        return True

    return False


def add_elements(arr: List[int], k: int) -> int:
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:
        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # --- Input Validation ---
    # Check if arr is None or not a list
    if arr is None or not isinstance(arr, list):
        raise ValueError("Input 'arr' must be a non-empty list of integers.")

    # Check if the list is empty
    list_length = len(arr)
    if list_length == 0:
        raise ValueError("Input 'arr' must contain at least one element.")

    # Check if k is an integer
    if not isinstance(k, int):
        raise ValueError("Input 'k' must be an integer.")

    # Check if k is within the valid range [1, len(arr)]
    if k < 1 or k > list_length:
        raise ValueError(f"Input 'k' must be between 1 and {list_length} inclusive.")

    # --- Processing ---
    # Identify the subset of elements to consider (the first k elements)
    # Using slicing ensures we don't modify the original list.
    subset_to_examine = arr[:k]

    total_sum = 0

    # Iterate through each number in the subset
    for element in subset_to_examine:
        # Ensure the element is an integer
        if not isinstance(element, int):
            # In a production environment, we might skip or raise an error.
            # Given the prompt, we assume integers based on problem description.
            continue

        # Check if the number satisfies the condition (at most two digits)
        is_valid_count = has_at_most_two_digits(element)

        if is_valid_count:
            # Add to running total if condition is met
            total_sum += element

    return total_sum