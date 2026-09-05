from typing import List, Any

def _is_strictly_positive(value: Any) -> bool:
    """
    Helper function to determine if a value is a positive number.
    Strictly positive means the value must be greater than zero.
    """
    # Check if the value is an instance of int or float to prevent
    # boolean or string comparisons from causing unexpected behavior.
    if not isinstance(value, (int, float)):
        return False

    # Booleans are technically integers in Python (True == 1), 
    # but we should strictly exclude them if we want 'numbers'.
    if isinstance(value, bool):
        return False

    is_greater_than_zero = value > 0
    return is_greater_than_zero

def get_positive(l: list) -> List[Any]:
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    # Validate that the input is actually a list
    if not isinstance(l, list):
        raise TypeError(f"Expected input type 'list', but received '{type(l).__name__}'")

    # Handle empty list edge case
    if len(l) == 0:
        return []

    # Initialize the result container
    positive_numbers: List[Any] = []

    # Iterate through each item in the input list
    for item in l:
        # Check if the item satisfies the positivity condition
        is_positive = _is_strictly_positive(item)

        if is_positive:
            # Append the valid positive number to our results
            positive_numbers.append(item)

    return positive_numbers