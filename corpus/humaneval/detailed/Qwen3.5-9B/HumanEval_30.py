from typing import List, Union

Number = Union[int, float]

def _is_positive(value: Number) -> bool:
    """
    Check if a numeric value is strictly positive.

    A value is considered positive if it is greater than zero.
    Zero and negative values are considered non-positive.

    Args:
        value: A numeric value (int or float).

    Returns:
        True if the value is strictly greater than zero, False otherwise.
    """
    # Explicitly check against zero to ensure strict positivity
    if value > 0:
        return True
    else:
        return False

def _validate_input(l: list) -> None:
    """
    Validate that the input is a list and contains only numeric values.

    This function raises a TypeError if the input is not a list.
    It also raises a TypeError if any element within the list is not
    a number (int or float).

    Args:
        l: The input list to validate.

    Raises:
        TypeError: If l is not a list or contains non-numeric elements.
    """
    # Check if the input is a list instance
    if not isinstance(l, list):
        raise TypeError("Input must be a list.")

    # Iterate through each element to check for numeric types
    for index, item in enumerate(l):
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"Element at index {index} is not a number. "
                f"Expected int or float, got {type(item).__name__}."
            )

def get_positive(l: list) -> List[Number]:
    """
    Return only positive numbers in the list.

    This function filters a list to return only the elements that are
    strictly greater than zero. It includes both integers and floats.
    Zero and negative numbers are excluded.

    Args:
        l: A list of numbers (integers or floats).

    Returns:
        A new list containing only the positive numbers from the input list,
        in the order they originally appeared.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.

    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
        >>> get_positive([])
        []
        >>> get_positive([0, 0, 0])
        []
        >>> get_positive([-1, -2, -3])
        []
        >>> get_positive([1.5, 2.5, -0.5])
        [1.5, 2.5]
    """
    # Step 1: Validate the input structure and contents
    _validate_input(l)

    # Step 2: Initialize an empty list to store positive numbers
    positive_numbers: List[Number] = []

    # Step 3: Iterate through each element in the input list explicitly
    for item in l:
        # Step 4: Check if the current element is positive
        if _is_positive(item):
            # Step 5: If positive, append it to our result list
            positive_numbers.append(item)

    # Step 6: Return the list of positive numbers found
    return positive_numbers