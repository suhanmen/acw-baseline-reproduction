from typing import List, Union

def _validate_input_elements(elements: List[Union[int, float]]) -> None:
    """
    Validates that all elements in the provided list are either integers or floats.
    Raises a TypeError if any element is invalid.
    """
    for index, element in enumerate(elements):
        if not isinstance(element, (int, float)):
            raise TypeError(
                f"All elements in the array must be numeric (int or float). "
                f"Invalid type found at index {index}: {type(element).__name__}"
            )


def _validate_input_length(elements: List[Union[int, float]]) -> None:
    """
    Validates that the provided list is not empty.
    Raises a ValueError if the list is empty.
    """
    if len(elements) == 0:
        raise ValueError(
            "The input list cannot be empty. "
            "Provide at least one element to calculate pairwise absolute differences."
        )


def _calculate_sum_of_pairs(elements: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculates the sum of absolute differences for all unique pairs (i, j) where i < j.

    The formula for the sum of absolute differences for all pairs (i, j) where i < j
    in an array of numbers is equivalent to iterating through the sorted array and
    summing the absolute differences. However, since the problem does not specify
    sorting and the absolute difference is symmetric (|a - b| = |b - a|), we can
    iterate over all pairs (i, j) where i < j without sorting, as the order does
    not affect the sum.

    Args:
    elements (List[Union[int, float]]): The list of numeric elements.

    Returns:
    Union[int, float]: The sum of absolute differences of all unique pairs.
    """
    total_sum = 0.0

    # Use float for accumulation to handle cases where inputs are floats or mixed
    # Even if inputs are integers, the accumulation logic remains consistent.

    # Iterate over all unique pairs (i, j) such that i < j
    # This ensures we count each pair exactly once and avoid comparing an element to itself.
    for i in range(len(elements)):
        current_element_i = elements[i]

        for j in range(i + 1, len(elements)):
            current_element_j = elements[j]

            # Calculate the absolute difference for the current pair
            absolute_diff = abs(current_element_i - current_element_j)

            # Add to the running total
            total_sum += absolute_diff

    return total_sum


def sum_Pairs(input_list: List[Union[int, float]], _: Union[int, float]) -> Union[int, float]:
    """
    Finds the sum of absolute differences in all pairs of the given array.

    The second argument is kept for signature compatibility but is unused in the calculation.
    This function validates the input, computes the sum of absolute differences for
    all unique pairs (i, j) where i < j, and returns the result.

    Args:
    input_list (List[Union[int, float]]): The list of numeric elements.
    _ (Union[int, float]): Unused argument (signature placeholder).

    Returns:
    Union[int, float]: The sum of absolute differences of all unique pairs.

    Raises:
    ValueError: If the input list is empty.
    TypeError: If any element in the input list is not a number.
    """
    # Validate inputs explicitly
    _validate_input_elements(input_list)
    _validate_input_length(input_list)

    # Calculate and return the result
    return _calculate_sum_of_pairs(input_list)