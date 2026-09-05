from typing import List, Any, Set, Tuple


def _validate_input_list(value: Any) -> Tuple[bool, str]:
    """
    Validates that the input is a list.

    Args:
        value: The input to validate.

    Returns:
        A tuple of (is_valid, error_message).
        If valid, is_valid is True and error_message is empty.
        If invalid, is_valid is False and error_message explains why.
    """
    if not isinstance(value, list):
        return False, "Input must be a list."
    return True, ""


def _remove_duplicates(elements: List[Any]) -> List[Any]:
    """
    Removes duplicate elements from a list while preserving the order of first occurrence.
    Note: Order is not strictly required by the final problem statement (which asks for sorted),
    but we handle this explicitly to build the unique set before sorting.

    This implementation uses a set to track seen items and a list to maintain uniqueness.

    Args:
        elements: The list containing potential duplicates.

    Returns:
        A new list containing only the unique elements from the input.
    """
    if not elements:
        return []

    unique_elements: List[Any] = []
    seen_items: Set[Any] = set()

    for item in elements:
        if item not in seen_items:
            seen_items.add(item)
            unique_elements.append(item)

    return unique_elements


def _sort_elements(unique_list: List[Any]) -> List[Any]:
    """
    Sorts a list of unique elements in ascending order.

    Args:
        unique_list: A list containing unique elements (order doesn't matter here).

    Returns:
        A new list with elements sorted in ascending order.

    Note:
        The sort is stable for equal elements (though duplicates are already removed).
        It handles mixed types by attempting to compare them; if comparison fails
        (e.g., comparing string to int), Python 3 raises a TypeError naturally,
        which is the expected behavior for invalid comparisons in sorting.
    """
    return sorted(unique_list)


def unique(l: list) -> List[Any]:
    """
    Return sorted unique elements in a list.

    This function takes a list of elements, removes any duplicates, and returns
    a new list containing only the unique elements sorted in ascending order.

    Args:
        l: A list of elements. Can contain integers, floats, strings, or other
           hashable types that support comparison operations.

    Returns:
        A list containing the unique elements from the input list, sorted in ascending order.

    Raises:
        TypeError: If the input is not a list or if elements cannot be compared during sorting.
        ValueError: If the input is empty (though an empty list is handled gracefully by returning []).

    Examples:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
        >>> unique([])
        []
        >>> unique([1, 1, 1, 1])
        [1]
        >>> unique([-5, -1, -5, 0, 1, -1])
        [-5, -1, 0, 1]
        >>> unique(['a', 'b', 'a', 'c'])
        ['a', 'b', 'c']
    """
    # Step 1: Validate the input type
    is_valid, error_message = _validate_input_list(l)

    if not is_valid:
        raise TypeError(error_message)

    # Step 2: Check for empty list (though logic handles it, explicit check for clarity)
    if len(l) == 0:
        return []

    # Step 3: Remove duplicates from the list
    unique_elements = _remove_duplicates(l)

    # Step 4: Sort the unique elements
    sorted_unique_elements = _sort_elements(unique_elements)

    return sorted_unique_elements