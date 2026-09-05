from typing import List, Union

Number = Union[int, float]

def _validate_input_list(numbers: List[Number]) -> None:
    """
    Validates that the input is a list and contains only numeric values.
    Raises a ValueError if validation fails.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list, but received {type(numbers).__name__}.")

    if len(numbers) == 0:
        raise ValueError("The input list cannot be empty.")

    for index, value in enumerate(numbers):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError(
                f"Element at index {index} is not a valid number. "
                f"Received {type(value).__name__}: {value!r}"
            )

def _validate_indices(
    start_index: int, 
    end_index: int, 
    list_length: int
) -> None:
    """
    Validates that the provided start and end indices are within the valid range
    for the given list length.
    Raises a ValueError if validation fails.

    Logic: The problem implies 0-based indexing where the range includes both endpoints.
    Thus, valid start_index is 0 to list_length-1, and valid end_index is 0 to list_length-1.
    Additionally, typically start_index should be less than or equal to end_index.
    """
    if not isinstance(start_index, int) or isinstance(start_index, bool):
        raise TypeError(f"start_index must be an integer, received {type(start_index).__name__}.")

    if not isinstance(end_index, int) or isinstance(end_index, bool):
        raise TypeError(f"end_index must be an integer, received {type(end_index).__name__}.")

    if start_index < 0:
        raise ValueError(f"start_index must be non-negative, received {start_index}.")

    if end_index < 0:
        raise ValueError(f"end_index must be non-negative, received {end_index}.")

    if start_index > end_index:
        raise ValueError(f"start_index ({start_index}) must be less than or equal to end_index ({end_index}).")

    if start_index >= list_length:
        raise ValueError(
            f"start_index ({start_index}) is out of bounds for a list of length {list_length}."
        )

    if end_index >= list_length:
        raise ValueError(
            f"end_index ({end_index}) is out of bounds for a list of length {list_length}."
        )

def sum_range_list(numbers: List[Number], start_index: int, end_index: int) -> Number:
    """
    Calculates the sum of numbers in a list between specified indices (inclusive).

    Args:
        numbers: A list of numeric values.
        start_index: The starting index (inclusive).
        end_index: The ending index (inclusive).

    Returns:
        The sum of the elements in the specified range.

    Raises:
        TypeError: If inputs are not of the expected type.
        ValueError: If inputs are out of bounds or invalid (e.g., negative indices, start > end).
    """
    # Step 1: Validate the list structure and contents
    _validate_input_list(numbers)

    # Capture the length early for use in index validation
    list_length = len(numbers)

    # Step 2: Validate the indices against the list boundaries and relative order
    _validate_indices(start_index, end_index, list_length)

    # Step 3: Extract the sub-list within the specified range
    # This creates a new list containing elements from start_index to end_index (inclusive)
    sub_list = []
    current_index = start_index

    while current_index <= end_index:
        sub_list.append(numbers[current_index])
        current_index += 1

    # Step 4: Calculate the sum of the extracted sub-list
    running_total = 0

    for value in sub_list:
        running_total = running_total + value

    return running_total