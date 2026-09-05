from typing import Any, List, Union

Number = Union[int, float]

def is_valid_input(item: Any) -> bool:
    """
    Validate that a single item is a numeric type (int or float).
    Returns True if valid, False otherwise.
    """
    return isinstance(item, (int, float)) and not isinstance(item, bool)

def is_valid_list(l: Any) -> bool:
    """
    Validate that the input is a list and contains only numeric items.
    Returns True if valid, False otherwise.
    """
    if not isinstance(l, list):
        return False

    for item in l:
        if not is_valid_input(item):
            return False

    return True

def increment_number(value: Number) -> Number:
    """
    Increment a numeric value by 1.
    """
    return value + 1

def build_incremented_list(input_list: List[Number]) -> List[Number]:
    """
    Build a new list where each element is incremented by 1.
    Uses explicit iteration and named variables.
    """
    result: List[Number] = []

    for current_element in input_list:
        incremented_value = increment_number(current_element)
        result.append(incremented_value)

    return result

def incr_list(l: list) -> List[Number]:
    """
    Return list with elements incremented by 1.

    This function performs rigorous validation on the input list.
    It ensures:
    1. The input is strictly a list instance.
    2. Every element within the list is strictly a number (int or float).
    3. Boolean values (subclass of int) are rejected as invalid numeric data.
    4. Empty lists are handled gracefully (returned as empty).
    5. Single elements, all-equal elements, and boundary values (0, negatives)
       are processed correctly through explicit iteration.

    Raises a TypeError if input validation fails.

    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    >>> incr_list([])
    []
    >>> incr_list([1.5, 2.5])
    [2.5, 3.5]
    >>> incr_list([0, -1, -10])
    [1, 0, -9]
    """
    # Step 1: Validate the type of the container is exactly a list
    if not is_valid_list(l):
        raise TypeError(
            f"Expected a list of numbers, got: {type(l).__name__}"
        )

    # Step 2: Handle the edge case of an empty list explicitly
    if len(l) == 0:
        return []

    # Step 3: Process the list elements
    # We create a new list to ensure immutability of the original input
    incremented_list = build_incremented_list(l)

    return incremented_list