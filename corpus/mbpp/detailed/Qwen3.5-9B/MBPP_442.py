from typing import List, Optional, Union

Number = Union[int, float]

def _validate_input_array(array: List[Number]) -> None:
    """
    Validates that the input is a list of numbers.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    if not isinstance(array, list):
        raise TypeError(
            f"Expected input to be a list of numbers, but received type: {type(array).__name__}"
        )

    for index, item in enumerate(array):
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"Element at index {index} is not a number (received {type(item).__name__})"
            )

def _is_positive(number: Number) -> bool:
    """
    Determines if a number is strictly positive.

    Returns:
        True if the number is greater than zero, False otherwise.
    """
    return number > 0

def _count_positives(array: List[Number]) -> int:
    """
    Counts the number of strictly positive integers in the array.

    Args:
        array: A list of numeric values.

    Returns:
        An integer representing the count of values > 0.
    """
    count = 0
    for value in array:
        if _is_positive(value):
            count += 1
    return count

def positive_count(array: List[Number]) -> Optional[float]:
    """
    Calculates the ratio of positive numbers in an array of integers.

    The ratio is calculated as: (count of positive numbers) / (total count of numbers).

    Rules for calculation:
    - Zero (0) is NOT considered positive.
    - Negative numbers are NOT considered positive.
    - If the array is empty, the function returns None (ratio is undefined).

    Args:
        array: A list of numeric values (integers or floats).

    Returns:
        float: The ratio of positive numbers (value between 0.0 and 1.0).
        None: If the input array is empty.

    Raises:
        TypeError: If the input is not a list or contains invalid elements.
    """
    # Step 1: Validate the input structure and contents
    _validate_input_array(array)

    # Step 2: Calculate the total number of elements
    total_elements = len(array)

    # Step 3: Handle the empty list edge case explicitly
    # The ratio cannot be calculated if there are no elements (division by zero).
    if total_elements == 0:
        return None

    # Step 4: Calculate the number of positive elements
    positive_count_value = _count_positives(array)

    # Step 5: Compute the ratio
    ratio = positive_count_value / float(total_elements)

    return ratio