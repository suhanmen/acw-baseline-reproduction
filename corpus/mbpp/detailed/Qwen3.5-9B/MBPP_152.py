from typing import Any, List, Union

Number = Union[int, float]


def is_valid_sort_input(data: Any) -> bool:
    """
    Validate that the input is a list containing only numbers.

    This function checks:
    1. The input is a list.
    2. The input is not None.
    3. Every element in the list is a number (int or float).

    Returns True if valid, False otherwise.
    """
    if not isinstance(data, list):
        return False

    if len(data) == 0:
        return True

    for item in data:
        if not isinstance(item, (int, float)):
            return False

    return True


def create_empty_list() -> List[Number]:
    """Returns an empty list to serve as a base case for merge sort."""
    return []


def create_single_element_list(element: Number) -> List[Number]:
    """Creates a list containing exactly one element."""
    return [element]


def merge_sorted_lists(left: List[Number], right: List[Number]) -> List[Number]:
    """
    Merges two sorted lists into a single sorted list.

    This is the core logic of merge sort. It uses two pointers to traverse
    both lists and combines them in ascending order.

    Parameters:
    left: A sorted list of numbers.
    right: A sorted list of numbers.

    Returns:
    A new list containing all elements from both input lists in sorted order.
    """
    result: List[Number] = create_empty_list()

    left_index: int = 0
    right_index: int = 0

    total_left_length: int = len(left)
    total_right_length: int = len(right)

    while left_index < total_left_length and right_index < total_right_length:
        current_left_value: Number = left[left_index]
        current_right_value: Number = right[right_index]

        if current_left_value <= current_right_value:
            result.append(current_left_value)
            left_index += 1
        else:
            result.append(current_right_value)
            right_index += 1

    while left_index < total_left_length:
        result.append(left[left_index])
        left_index += 1

    while right_index < total_right_length:
        result.append(right[right_index])
        right_index += 1

    return result


def merge_sort_recursive(data: List[Number]) -> List[Number]:
    """
    Recursively sorts a list using the merge sort algorithm.

    Base cases:
    1. An empty list is already sorted.
    2. A single-element list is already sorted.

    Recursive step:
    Split the list into two halves, sort each half recursively,
    and then merge the two sorted halves.

    Parameters:
    data: A list of numbers to be sorted.

    Returns:
    A new list containing the sorted elements.
    """
    list_length: int = len(data)

    if list_length <= 1:
        return data

    middle_index: int = list_length // 2

    left_half: List[Number] = data[:middle_index]
    right_half: List[Number] = data[middle_index:]

    sorted_left: List[Number] = merge_sort_recursive(left_half)
    sorted_right: List[Number] = merge_sort_recursive(right_half)

    merged_result: List[Number] = merge_sorted_lists(sorted_left, sorted_right)

    return merged_result


def merge_sort(array: Any) -> List[Number]:
    """
    Sorts a given array using the merge sort algorithm.

    This function acts as the public interface for sorting. It first validates
    the input to ensure it meets the requirements for sorting numbers. If the
    input is valid, it delegates to the recursive helper function to perform
    the actual sorting.

    Parameters:
    array: The input data to be sorted. Expected to be a list of numbers.

    Returns:
    A new list containing the sorted elements.

    Raises:
    TypeError: If the input is not a list or contains non-number elements.
    """
    if not is_valid_sort_input(array):
        raise TypeError(
            "Input must be a list containing only integers or floats."
        )

    sorted_array: List[Number] = merge_sort_recursive(array)

    return sorted_array