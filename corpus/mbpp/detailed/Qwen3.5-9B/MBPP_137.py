from typing import List, Union

def _validate_input(array: List[Union[int, float]]) -> None:
    """
    Validates that the input is a non-empty list of integers or floats.

    This function performs explicit checks to ensure the data passed
    to the zero ratio calculation is valid. It raises a ValueError if:
    - The input is not a list.
    - The list is empty (as division by zero is undefined for ratios).
    - Any element within the list is not a number (int or float).

    Parameters:
        array (List[Union[int, float]]): The list of numbers to validate.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
        ValueError: If the input list is empty.
    """
    if not isinstance(array, list):
        raise TypeError("Input must be a list.")

    if len(array) == 0:
        raise ValueError("Input list cannot be empty; ratio cannot be calculated for zero elements.")

    for i, item in enumerate(array):
        if not isinstance(item, (int, float)):
            raise TypeError(f"Element at index {i} is not a number: {type(item).__name__}.")


def _count_zeroes(array: List[Union[int, float]]) -> int:
    """
    Counts the number of zero values in the provided list.

    This function iterates through the array and increments a counter
    for every element that evaluates to zero.

    Parameters:
        array (List[Union[int, float]]): The list of numbers to scan.

    Returns:
        int: The count of zeroes found in the list.
    """
    zero_count = 0

    for item in array:
        # Check if the current item is exactly zero
        # This works for both integer 0 and float 0.0
        if item == 0:
            zero_count += 1

    return zero_count


def _calculate_total_elements(array: List[Union[int, float]]) -> int:
    """
    Calculates the total number of elements in the provided list.

    Parameters:
        array (List[Union[int, float]]): The list of numbers to count.

    Returns:
        int: The total length of the list.
    """
    return len(array)


def _compute_ratio(zero_count: int, total_count: int) -> float:
    """
    Computes the ratio of zeroes to the total count of elements.

    Parameters:
        zero_count (int): The number of zeroes found.
        total_count (int): The total number of elements in the array.

    Returns:
        float: The calculated ratio.

    Note:
        The validation step before this function ensures total_count > 0,
        so no division by zero check is needed here.
    """
    return zero_count / total_count


def zero_count(array: List[Union[int, float]]) -> float:
    """
    Calculates the ratio of zeroes in an array of integers (or floats).

    This function determines the proportion of elements in the array
    that have a value of zero. The result is returned as a floating-point
    number representing the fraction of zeroes.

    Parameters:
        array (List[Union[int, float]]): A list of integers or floats.

    Returns:
        float: The ratio of zeroes to total elements (between 0.0 and 1.0).

    Raises:
        TypeError: If the input is not a list or contains non-numeric values.
        ValueError: If the input list is empty.
    """
    # Step 1: Validate the input data explicitly
    _validate_input(array)

    # Step 2: Count the number of zeroes in the validated array
    count_of_zeroes = _count_zeroes(array)

    # Step 3: Get the total number of elements for the denominator
    total_number_of_elements = _calculate_total_elements(array)

    # Step 4: Compute the ratio using the explicit helper to ensure clarity
    ratio_result = _compute_ratio(count_of_zeroes, total_number_of_elements)

    return ratio_result