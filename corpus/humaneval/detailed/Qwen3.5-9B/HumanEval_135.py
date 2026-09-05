from typing import List, Union


def can_arrange(arr: List[Union[int, float]]) -> int:
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    return _find_largest_decrease_index(arr)


def _validate_input(input_list: List) -> List:
    """
    Validates the input list to ensure it is indeed a list (or tuple treated as list)
    and contains only numeric values. Raises a ValueError if invalid.
    """
    if not isinstance(input_list, list):
        raise TypeError(
            f"Input must be a list of numbers, but received: {type(input_list).__name__}"
        )

    if not all(isinstance(item, (int, float)) for item in input_list):
        non_numeric_index = next(
            i for i, item in enumerate(input_list) 
            if not isinstance(item, (int, float))
        )
        raise TypeError(
            f"All elements must be numbers. Found non-numeric element at index {non_numeric_index}: "
            f"{input_list[non_numeric_index]} (type: {type(input_list[non_numeric_index]).__name__})"
        )

    return input_list


def _is_decreasing_pair(predecessor: Union[int, float], current: Union[int, float]) -> bool:
    """
    Determines if the current element is strictly less than the predecessor.
    The problem asks for an element that is "not greater than or equal to" the predecessor.
    Mathematically: current <= predecessor.
    However, the problem statement also guarantees no duplicate values.
    Therefore, current == predecessor is impossible.
    Thus, the condition simplifies to: current < predecessor.
    """
    return current < predecessor


def _find_largest_decrease_index(arr: List[Union[int, float]]) -> int:
    """
    Iterates through the array to find the largest index 'i' such that
    arr[i] < arr[i-1].

    Returns:
        The largest index 'i' satisfying the condition, or -1 if no such index exists.
    """
    if len(arr) < 2:
        # An array with fewer than 2 elements cannot have a "preceding" element.
        return -1

    largest_decreasing_index = -1

    # We iterate from index 1 up to the second-to-last element.
    # This allows us to compare arr[i] with arr[i-1] for all valid pairs.
    # We use an explicit loop to inspect every comparison.
    for current_index in range(1, len(arr)):
        predecessor_value = arr[current_index - 1]
        current_value = arr[current_index]

        # Check the condition: is current_value not greater than or equal to predecessor_value?
        # Given no duplicates, this is equivalent to current_value < predecessor_value.
        is_current_less_than_predecessor = _is_decreasing_pair(predecessor_value, current_value)

        if is_current_less_than_predecessor:
            # If we find such an index, we record it.
            # Since we iterate in increasing order, the last one we find will be the largest.
            largest_decreasing_index = current_index

    return largest_decreasing_index