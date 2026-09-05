from typing import List, Tuple, Any, Optional, Union

Number = Union[int, float]

def _validate_tuple_item(item: Any) -> bool:
    """
    Validate that the given item is a valid tuple containing exactly two numeric values.

    Returns:
        True if the item is valid.
        Raises:
            TypeError: If the item is not a tuple or does not contain exactly two elements.
            ValueError: If any of the elements in the tuple are not numeric.
    """
    # Check if the item is a tuple (or tuple subclass)
    if not isinstance(item, tuple):
        raise TypeError(
            f"Invalid input type: Expected a tuple, but got {type(item).__name__}."
        )

    # Check if the tuple has exactly two elements
    if len(item) != 2:
        raise ValueError(
            f"Invalid tuple length: Expected a tuple with exactly 2 elements, but got {len(item)}."
        )

    # Validate the first element
    first_element = item[0]
    if not isinstance(first_element, (int, float)) or isinstance(first_element, bool):
        raise ValueError(
            f"Invalid first element: Expected a numeric type (int or float), "
            f"but got {type(first_element).__name__} (value: {first_element}). "
            "Note: Booleans are treated as subclasses of int in Python and are not accepted here."
        )

    # Validate the second element
    second_element = item[1]
    if not isinstance(second_element, (int, float)) or isinstance(second_element, bool):
        raise ValueError(
            f"Invalid second element: Expected a numeric type (int or float), "
            f"but got {type(second_element).__name__} (value: {second_element}). "
            "Note: Booleans are treated as subclasses of int in Python and are not accepted here."
        )

    return True


def _find_max_in_tuple(t: Tuple[Number, Number]) -> Number:
    """
    Find the maximum value within a single tuple record.

    Args:
        t: A tuple containing exactly two numeric values.

    Returns:
        The maximum value found in the tuple.
    """
    value_one = t[0]
    value_two = t[1]

    if value_one > value_two:
        return value_one
    else:
        return value_two


def _find_global_max_in_list_of_tuples(tuples_list: List[Tuple[Number, Number]]) -> Number:
    """
    Find the maximum element among all elements in all provided tuple records.

    This function iterates through each tuple in the list, finds the maximum
    of the current tuple, and keeps track of the global maximum found so far.

    Args:
        tuples_list: A list of tuples, where each tuple contains exactly two numeric values.

    Returns:
        The maximum number found across all numbers in all tuples.

    Raises:
        ValueError: If the input list is empty.
    """
    # Handle empty list edge case
    if len(tuples_list) == 0:
        raise ValueError("The input list of tuples is empty. Cannot find a maximum value.")

    # Initialize global_max with the maximum of the first tuple
    # This handles cases where all numbers are negative correctly.
    current_tuple_index = 0
    current_tuple = tuples_list[current_tuple_index]

    # Validate the first tuple before using it to initialize
    _validate_tuple_item(current_tuple)
    max_in_first_tuple = _find_max_in_tuple(current_tuple)

    global_max = max_in_first_tuple

    # Iterate through the remaining tuples
    for index in range(1, len(tuples_list)):
        next_tuple = tuples_list[index]

        # Validate each subsequent tuple
        _validate_tuple_item(next_tuple)

        # Find the max within the current tuple
        tuple_max_value = _find_max_in_tuple(next_tuple)

        # Compare and update global maximum
        if tuple_max_value > global_max:
            global_max = tuple_max_value

    return global_max


def find_max(data: List[Tuple[Number, Number]]) -> Number:
    """
    Find the maximum element of all the given tuple records.

    This function validates that all inputs are valid tuples of two numbers,
    handles edge cases such as empty lists, and returns the largest single
    numeric value found across all tuples in the list.

    Args:
        data: A list of tuples, where each tuple contains exactly two numeric values (int or float).

    Returns:
        The maximum number found across all numbers in all tuples.

    Raises:
        TypeError: If the input is not a list or contains non-tuple elements.
        ValueError: If the input list is empty, or if any tuple has invalid length or non-numeric values.
    """
    # Validate the main input type
    if not isinstance(data, list):
        raise TypeError(
            f"The 'data' argument must be a list, but got {type(data).__name__}."
        )

    # Call the core logic function which handles internal validation and calculation
    return _find_global_max_in_list_of_tuples(data)