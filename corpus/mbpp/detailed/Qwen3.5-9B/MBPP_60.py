from typing import List, Optional, Tuple

def validate_input_elements(array: List[int]) -> None:
    """
    Validates that all elements in the array are integers.
    Raises a ValueError if any element is not an integer.
    """
    if not isinstance(array, list):
        raise TypeError("The first argument must be a list.")

    for index, value in enumerate(array):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"Element at index {index} is not an integer: {value} ({type(value).__name__})")

def calculate_difference(previous_value: int, current_value: int) -> int:
    """
    Calculates the absolute difference between two integer values.
    """
    return abs(current_value - previous_value)

def is_valid_transition(
    difference: int,
    target_difference: int,
    tolerance: int = 0
) -> bool:
    """
    Checks if the calculated difference is within a valid range relative to the target.
    In this specific problem context, we are looking for an exact match of the target difference.
    However, for robustness, this function allows for a small tolerance if needed, 
    though the standard interpretation of "difference" usually implies exact match.

    Args:
        difference: The actual calculated difference.
        target_difference: The required difference.
        tolerance: Allowable deviation (default 0 for exact match).

    Returns:
        True if the difference matches the target within tolerance, False otherwise.
    """
    return (difference - target_difference) == 0

def build_subsequence_lengths(
    array: List[int],
    target_difference: int
) -> List[int]:
    """
    Dynamic programming function to calculate the length of the longest valid subsequence
    ending at each index.

    A subsequence here refers to a contiguous subarray (slice) where every adjacent 
    pair of elements has a difference equal to the target_difference.
    Based on the problem examples, "subsequence" implies a contiguous subarray 
    (often called a subarray in competitive programming contexts).

    Returns:
        A list where index i contains the length of the longest valid contiguous subsequence
        ending at index i.
    """
    n = len(array)

    if n == 0:
        return []

    # dp[i] will store the length of the longest valid contiguous subsequence ending at index i
    dp: List[int] = [1] * n

    for current_index in range(1, n):
        previous_index = current_index - 1

        # Calculate the difference between the current element and the previous element
        actual_diff = calculate_difference(array[previous_index], array[current_index])

        # Check if the current pair satisfies the condition
        if is_valid_transition(actual_diff, target_difference):
            # Extend the sequence from the previous element
            dp[current_index] = dp[previous_index] + 1

    return dp

def find_maximum_length(
    array: List[int],
    target_difference: int
) -> int:
    """
    Finds the maximum length of a contiguous subsequence where the difference 
    between adjacent elements is exactly equal to target_difference.

    Args:
        array: A list of integers.
        target_difference: The required difference between adjacent elements.

    Returns:
        The maximum length of such a subsequence.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If input types are incorrect.
    """
    # Handle empty input explicitly
    if len(array) == 0:
        raise ValueError("Input array cannot be empty.")

    # Validate the array elements
    validate_input_elements(array)

    # Validate the target difference type
    if not isinstance(target_difference, int) or isinstance(target_difference, bool):
        raise TypeError("Target difference must be an integer.")

    # Compute the lengths of valid subsequences ending at each position
    dp_values = build_subsequence_lengths(array, target_difference)

    # Find the maximum value in the dp list
    max_length = dp_values[0]  # Initialize with at least the first element (length 1)

    for length_value in dp_values:
        if length_value > max_length:
            max_length = length_value

    return max_length

def max_len_sub(arr: List[int], diff: int) -> int:
    """
    Wrapper function to find the maximum length of the subsequence with difference
    between adjacent elements for the given array.

    Args:
        arr: The input list of integers.
        diff: The target difference between adjacent elements.

    Returns:
        The maximum length of the valid subsequence.
    """
    result = find_maximum_length(arr, diff)
    return result