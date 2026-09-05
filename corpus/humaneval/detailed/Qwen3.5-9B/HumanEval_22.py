from typing import List, Any


def _validate_input(values: List[Any]) -> None:
    """
    Validate that the input is a list.
    Raises a TypeError if the input is not a list.
    """
    if not isinstance(values, list):
        raise TypeError(
            f"Expected input to be of type 'list', but got '{type(values).__name__}' instead."
        )


def _is_integer(value: Any) -> bool:
    """
    Determine if a given value is an integer.

    This function returns True if and only if:
    1. The value is of type int.
    2. The value is not of type bool (since bool is a subclass of int in Python).

    It returns False for floats, strings, None, custom objects, and other types.
    """
    return isinstance(value, int) and not isinstance(value, bool)


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    This function iterates through the provided list and collects only those
    elements that are strictly integers (excluding booleans).

    Args:
        values: A list containing values of any type.

    Returns:
        A new list containing only the integer values from the input list.

    Raises:
        TypeError: If the input 'values' is not a list.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
        >>> filter_integers([])
        []
        >>> filter_integers([True, False, 0, 1])
        [0, 1]
        >>> filter_integers([-5, 0, 5])
        [-5, 0, 5]
    """
    # Step 1: Validate the input to ensure it is a list.
    # This handles edge cases where None, a tuple, or a single integer might be passed.
    _validate_input(values)

    # Step 2: Initialize an empty list to store the filtered integer values.
    # Using an empty list ensures we return [] for empty inputs or inputs with no integers.
    filtered_integers: List[int] = []

    # Step 3: Iterate through each element in the input list.
    # We use an explicit for-loop for clarity and to allow detailed processing per element.
    for current_value in values:
        # Step 4: Check if the current value is an integer using the helper function.
        # The helper function explicitly excludes booleans, which are technically integers in Python.
        if _is_integer(current_value):
            # Step 5: Append the valid integer to our result list.
            filtered_integers.append(current_value)

    # Step 6: Return the newly constructed list of integers.
    return filtered_integers