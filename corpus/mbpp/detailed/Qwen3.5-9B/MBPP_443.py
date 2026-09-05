from typing import List, Optional, Union

Number = Union[int, float]


def _validate_input_list(input_list: List[Number]) -> List[Number]:
    """
    Validates that the input is a list containing only numeric values.

    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
    """
    if not isinstance(input_list, list):
        raise TypeError(f"Input must be a list, got {type(input_list).__name__}")

    for index, item in enumerate(input_list):
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"Element at index {index} is not a number: {type(item).__name__} ({item!r})"
            )

    return input_list


def _find_largest_negative_number(numbers: List[Number]) -> Number:
    """
    Iterates through a list of numbers to find the largest negative number.

    A negative number is defined as any number strictly less than zero.

    Returns:
        The largest negative number found in the list.

    Raises:
        ValueError: If no negative numbers are found in the list.
    """
    largest_negative: Optional[Number] = None

    for current_number in numbers:
        if current_number < 0:
            if largest_negative is None:
                # This is the first negative number found
                largest_negative = current_number
            else:
                # Compare current negative number with the stored largest
                if current_number > largest_negative:
                    largest_negative = current_number

    if largest_negative is None:
        raise ValueError("No negative numbers found in the input list.")

    return largest_negative


def largest_neg(numbers: List[Number]) -> Number:
    """
    Finds the largest negative number from the given list.

    Args:
        numbers: A list of numeric values (integers or floats).

    Returns:
        The largest negative number (the one closest to zero among negatives).

    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
        ValueError: If the list is empty or contains no negative numbers.
    """
    # Step 1: Validate the input structure and content
    validated_list = _validate_input_list(numbers)

    # Step 2: Check for empty list edge case explicitly before processing
    if len(validated_list) == 0:
        raise ValueError("Input list is empty.")

    # Step 3: Find and return the largest negative number
    return _find_largest_negative_number(validated_list)