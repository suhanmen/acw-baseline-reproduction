from typing import List, Union, Optional

Number = Union[int, float]

def validate_numeric_sequence(sequence: List[Number]) -> None:
    """
    Validates that the input is a list and contains only numeric values.

    This function raises specific exceptions if:
    1. The input is not a list (e.g., None, tuple, dict).
    2. The input list contains any non-numeric elements.

    If validation passes, no exception is raised and the function returns normally.
    """
    if not isinstance(sequence, list):
        raise TypeError(
            f"Expected a list of numbers, but received type: {type(sequence).__name__}"
        )

    for index, item in enumerate(sequence):
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise ValueError(
                f"Element at index {index} is not a valid number (int or float). "
                f"Found value: {item!r} (type: {type(item).__name__})"
            )

def compute_difference(list_item_a: Number, list_item_b: Number) -> Number:
    """
    Computes the difference between two consecutive numbers.

    Formula: result = list_item_b - list_item_a

    Args:
        list_item_a: The preceding number in the sequence.
        list_item_b: The following number in the sequence.

    Returns:
        The result of the subtraction.

    Raises:
        TypeError: If inputs are not numbers (though validated externally).
    """
    result = list_item_b - list_item_a
    return result

def diff_consecutivenums(sequence: List[Number]) -> List[Number]:
    """
    Finds the difference between two consecutive numbers in a given list.

    This function calculates the difference between each adjacent pair of numbers.
    Specifically, for a list [n1, n2, n3, ...], it returns [n2-n1, n3-n2, ...].

    Edge Cases Handled:
    - Empty list: Returns an empty list.
    - Single element: Returns an empty list (as there are no consecutive pairs).
    - All equal elements: Differences will be 0.
    - Negative numbers: Handled correctly by standard arithmetic.
    - Zero: Handled correctly.

    Input Validation:
    - Ensures input is a list.
    - Ensures all elements are numeric (int or float, excluding booleans).

    Args:
        sequence: A list of numeric values.

    Returns:
        A list of numbers representing the differences between consecutive elements.
        If the input list has fewer than 2 elements, an empty list is returned.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-numeric elements.
    """
    # Step 1: Validate the input structure and contents explicitly.
    validate_numeric_sequence(sequence)

    # Step 2: Define the length of the input list for clarity.
    sequence_length = len(sequence)

    # Step 3: Handle the degenerate case where there are no consecutive pairs.
    # If length is 0 (empty) or 1 (single element), no differences can be calculated.
    if sequence_length < 2:
        return []

    # Step 4: Initialize a list to store the results.
    # We use [] and append for explicit step-by-step construction, avoiding dense comprehension.
    result_list: List[Number] = []

    # Step 5: Iterate through the list up to the second-to-last element.
    # The range starts at 0 and goes up to (sequence_length - 2).
    # In each iteration, 'i' is the index of the first number in the pair.
    for i in range(sequence_length - 1):
        # Identify the current number (the predecessor).
        current_number = sequence[i]

        # Identify the next number (the successor).
        next_number = sequence[i + 1]

        # Step 6: Calculate the difference explicitly.
        difference = compute_difference(current_number, next_number)

        # Step 7: Append the calculated difference to the result list.
        result_list.append(difference)

    # Step 8: Return the fully constructed list of differences.
    return result_list