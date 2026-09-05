from typing import List, Union

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

    # Validate that arr is a list
    if not isinstance(arr, list):
        raise TypeError(f"Expected 'arr' to be a list, but received {type(arr).__name__}")

    # Validate that arr is not empty (per problem constraints: 1 <= len(arr))
    if len(arr) == 0:
        raise ValueError("Input array 'arr' must not be empty per constraints (1 <= len(arr) <= 100).")

    # Validate that k is an integer
    if not isinstance(k, int):
        raise TypeError(f"Expected 'k' to be an integer, but received {type(k).__name__}")

    # Validate that k is positive
    if k < 0:
        raise ValueError(f"Input 'k' must be a non-negative integer, but received {k}.")

    # Validate that k is not greater than the length of arr (per problem constraints)
    if k > len(arr):
        raise ValueError(f"Input 'k' ({k}) cannot be greater than the length of 'arr' ({len(arr)}).")

    # Helper function to check if a number has at most two digits
    def has_at_most_two_digits(number: int) -> bool:
        """
        Checks if the absolute value of an integer has at most two digits.
        This covers 0, 1-digit numbers (0-9, -9 to -1), and 2-digit numbers (10-99, -99 to -10).
        Numbers like 100, 0, -100 are excluded? Wait, 0 has one digit (0).
        100 has three digits. -5 has one digit.
        Logic: abs(number) must be in range [0, 99].
        """
        absolute_value = abs(number)
        return absolute_value <= 99

    # Initialize the sum accumulator
    total_sum = 0

    # Iterate exactly k times to process the first k elements
    for index in range(k):
        # Get the current element
        current_element = arr[index]

        # Validate the current element is an integer
        if not isinstance(current_element, int):
            raise TypeError(f"Expected all elements in 'arr' to be integers, but found {type(current_element).__name__} at index {index}.")

        # Check if the current element satisfies the "at most two digits" condition
        if has_at_most_two_digits(current_element):
            # Add the element to the running total
            total_sum += current_element

    return total_sum