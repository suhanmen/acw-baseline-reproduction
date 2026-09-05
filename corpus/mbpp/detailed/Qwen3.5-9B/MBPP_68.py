from typing import List, Union, Tuple

Number = Union[int, float]

def is_increasing_or_equal(sequence: List[Number]) -> bool:
    """
    Checks if a sequence is monotonically increasing (non-decreasing).

    For a sequence to be monotonically increasing or equal:
    - Every element must be less than or equal to the next element.
    - The sequence can contain equal adjacent elements.
    - The sequence cannot have any decrease.

    Args:
        sequence (List[Number]): The list of numbers to check.

    Returns:
        bool: True if the sequence is monotonically increasing or equal, False otherwise.
    """
    # Step 1: Handle the empty sequence case explicitly.
    # An empty list is technically monotonically increasing by definition (vacuous truth).
    if len(sequence) == 0:
        return True

    # Step 2: Handle the single element case explicitly.
    # A list with one element is trivially monotonically increasing.
    if len(sequence) == 1:
        return True

    # Step 3: Iterate through the sequence and check adjacent pairs.
    # We start from the second element (index 1) up to the last element.
    for current_index in range(1, len(sequence)):
        previous_value = sequence[current_index - 1]
        current_value = sequence[current_index]

        # Step 4: Check if the current value is strictly less than the previous value.
        # If sequence[i] < sequence[i-1], the sequence is not increasing.
        if current_value < previous_value:
            return False

    # Step 5: If no decreases were found, the sequence is monotonically increasing or equal.
    return True


def is_decreasing_or_equal(sequence: List[Number]) -> bool:
    """
    Checks if a sequence is monotonically decreasing (non-increasing).

    For a sequence to be monotonically decreasing or equal:
    - Every element must be greater than or equal to the next element.
    - The sequence can contain equal adjacent elements.
    - The sequence cannot have any increase.

    Args:
        sequence (List[Number]): The list of numbers to check.

    Returns:
        bool: True if the sequence is monotonically decreasing or equal, False otherwise.
    """
    # Step 1: Handle the empty sequence case explicitly.
    if len(sequence) == 0:
        return True

    # Step 2: Handle the single element case explicitly.
    if len(sequence) == 1:
        return True

    # Step 3: Iterate through the sequence and check adjacent pairs.
    for current_index in range(1, len(sequence)):
        previous_value = sequence[current_index - 1]
        current_value = sequence[current_index]

        # Step 4: Check if the current value is strictly greater than the previous value.
        # If sequence[i] > sequence[i-1], the sequence is not decreasing.
        if current_value > previous_value:
            return False

    # Step 5: If no increases were found, the sequence is monotonically decreasing or equal.
    return True


def is_Monotonic(sequence: List[Number]) -> bool:
    """
    Determines whether a given list of numbers is monotonic.

    A sequence is monotonic if it is either:
    1. Monotonically increasing (each element <= next element).
    2. Monotonically decreasing (each element >= next element).

    This function validates that the input is a list before proceeding.

    Args:
        sequence (List[Number]): The list of numbers to evaluate.

    Returns:
        bool: True if the sequence is monotonic (either increasing or decreasing), False otherwise.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
        ValueError: If the input is not a standard Python list (e.g., tuple, generator).
    """
    # Step 1: Validate input type strictly.
    # The problem specifies an "array", which we interpret as a Python list.
    if not isinstance(sequence, list):
        raise TypeError(
            f"Input must be a list, but got {type(sequence).__name__} instead."
        )

    # Step 2: Validate that all elements are numeric (int or float).
    for index, element in enumerate(sequence):
        if not isinstance(element, (int, float)):
            raise ValueError(
                f"Element at index {index} is not a number ({type(element).__name__})."
            )

    # Step 3: Check if the sequence is monotonically increasing or equal.
    is_increasing = is_increasing_or_equal(sequence)

    # Step 4: Check if the sequence is monotonically decreasing or equal.
    is_decreasing = is_decreasing_or_equal(sequence)

    # Step 5: The sequence is monotonic if it satisfies either condition.
    return is_increasing or is_decreasing