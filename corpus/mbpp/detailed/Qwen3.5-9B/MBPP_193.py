from typing import Tuple, Any, List


def _validate_tuple_input(input_data: Any) -> None:
    """
    Validates that the input is indeed a tuple.

    If the input is not a tuple, raises a TypeError with a descriptive message.
    """
    if not isinstance(input_data, tuple):
        raise TypeError(
            f"Expected input to be a tuple, but got {type(input_data).__name__}"
        )


def _build_seen_set() -> set:
    """
    Creates and returns an empty set to track elements we have already encountered.

    Using a set provides O(1) average time complexity for membership checks.
    """
    seen_elements: set = set()
    return seen_elements


def _extract_unique_elements(input_tuple: Tuple[Any, ...], seen_set: set) -> List[Any]:
    """
    Iterates through the input tuple and collects unique elements into a list.

    The order of the first occurrence of each element is preserved.
    Elements are only added if they have not been seen before.

    Args:
        input_tuple: The original tuple to process.
        seen_set: The set tracking elements already encountered.

    Returns:
        A list containing the unique elements in their order of first appearance.
    """
    unique_elements_list: List[Any] = []

    for element in input_tuple:
        if element not in seen_set:
            seen_set.add(element)
            unique_elements_list.append(element)

    return unique_elements_list


def _convert_list_to_tuple(unique_list: List[Any]) -> Tuple[Any, ...]:
    """
    Converts the list of unique elements back into a tuple.

    Args:
        unique_list: The list containing unique elements.

    Returns:
        A tuple containing the unique elements.
    """
    result_tuple: Tuple[Any, ...] = tuple(unique_list)
    return result_tuple


def remove_tuple(input_tuple: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """
    Removes duplicates from the given tuple while preserving the order 
    of the first occurrence of each element.

    This function handles edge cases such as:
    - Empty tuples
    - Tuples with a single element
    - Tuples with all identical elements
    - Tuples containing negative numbers, zero, or any other hashable type.

    Args:
        input_tuple: A tuple of hashable elements.

    Returns:
        A new tuple containing only the unique elements from the input, 
        in the order they first appeared.

    Raises:
        TypeError: If the input is not a tuple.

    Examples:
        >>> remove_tuple((1, 3, 5, 2, 3, 5, 1, 1, 3))
        (1, 2, 3, 5)
        >>> remove_tuple((2, 3, 4, 4, 5, 6, 6, 7, 8, 8))
        (2, 3, 4, 5, 6, 7, 8)
        >>> remove_tuple((11, 12, 13, 11, 11, 12, 14, 13))
        (11, 12, 13, 14)
    """
    # Step 1: Validate the input type explicitly
    _validate_tuple_input(input_tuple)

    # Step 2: Handle the degenerate case of an empty tuple explicitly
    # Although the logic below handles it naturally, this makes the intent clear.
    if len(input_tuple) == 0:
        return ()

    # Step 3: Initialize the set to keep track of seen elements
    seen_elements: set = _build_seen_set()

    # Step 4: Extract unique elements preserving order
    unique_elements_list: List[Any] = _extract_unique_elements(input_tuple, seen_elements)

    # Step 5: Convert the resulting list back to a tuple
    result_tuple: Tuple[Any, ...] = _convert_list_to_tuple(unique_elements_list)

    return result_tuple