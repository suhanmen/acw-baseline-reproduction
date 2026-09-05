from typing import Tuple, Union

def _validate_binary_string(input_string: str) -> None:
    """
    Validates that the input string is a non-empty binary string containing
    only '0' and '1' characters.

    Raises:
        ValueError: If the string is empty or contains invalid characters.
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, got {type(input_string).__name__}")

    if len(input_string) == 0:
        raise ValueError("Input string cannot be empty.")

    for char in input_string:
        if char not in ('0', '1'):
            raise ValueError(f"Input string must contain only '0' and '1', found invalid character: '{char}'")

def _convert_to_score_list(binary_string: str) -> list[int]:
    """
    Converts a binary string into a list of integers representing the contribution
    of each character to the running score.

    Logic:
    - '0' contributes +1 to the score (since we want max(0s - 1s)).
    - '1' contributes -1 to the score.

    This transforms the problem of finding the maximum difference of 0s and 1s
    into finding the maximum subarray sum (Kadane's algorithm context).

    Args:
        binary_string: A validated non-empty string of '0's and '1's.

    Returns:
        A list of integers where each element is 1 if the character is '0',
        and -1 if the character is '1'.
    """
    score_list = []

    for character in binary_string:
        if character == '0':
            score_list.append(1)
        elif character == '1':
            score_list.append(-1)
        else:
            # This should theoretically be caught by validation, but added for safety
            raise ValueError(f"Unexpected character encountered during conversion: '{character}'")

    return score_list

def _find_maximum_subarray_sum(score_list: list[int]) -> int:
    """
    Finds the maximum sum of a contiguous subarray within the provided list of integers.
    Uses Kadane's algorithm logic adapted for explicit step-by-step readability.

    The algorithm tracks:
    - current_sum: The sum of the current subarray being considered.
    - max_sum: The maximum sum found so far.

    Args:
        score_list: A list of integers (1s and -1s).

    Returns:
        The maximum subarray sum found.

    Note:
        If all numbers are negative, the algorithm returns 0 (representing an empty subarray),
        because a sub-string could technically be empty (difference 0). 
        However, the problem context implies non-empty sub-strings might be expected in some interpretations,
        but standard "maximum difference" problems usually allow 0 as the baseline if no positive difference exists.
        Looking at the problem constraints and typical algorithmic interpretations:
        If we pick an empty sub-string, the count of 0s is 0 and count of 1s is 0, difference is 0.
        If all '1' contributes negative, max diff is 0.
    """
    if len(score_list) == 0:
        return 0

    current_sum = 0
    max_sum = 0  # Initialize with 0 to handle cases where all diffs are negative (resulting in 0 difference)

    for score in score_list:
        # Update current_sum: either extend the existing subarray or start new with current score
        current_sum += score

        # If current_sum drops below zero, it's better to reset it to zero
        # because a negative prefix only reduces the potential of future subarrays.
        if current_sum < 0:
            current_sum = 0

        # Update max_sum if current_sum is greater
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

def find_length(binary_string: str) -> int:
    """
    Finds the maximum difference between the number of 0s and number of 1s 
    in any sub-string of the given binary string.

    The difference is calculated as: (count of '0's) - (count of '1's).

    Args:
        binary_string: A string consisting only of '0' and '1' characters.

    Returns:
        The maximum integer difference found in any contiguous sub-string.

    Raises:
        TypeError: If input is not a string.
        ValueError: If input is empty or contains non-binary characters.
    """
    # Step 1: Validate Input
    _validate_binary_string(binary_string)

    # Step 2: Convert binary string to score list (0 -> 1, 1 -> -1)
    score_list = _convert_to_score_list(binary_string)

    # Step 3: Find the maximum subarray sum using Kadane's algorithm
    max_difference = _find_maximum_subarray_sum(score_list)

    return max_difference