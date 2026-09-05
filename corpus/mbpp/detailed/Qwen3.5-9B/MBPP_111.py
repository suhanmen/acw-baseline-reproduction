from typing import Any, List, Iterable

def _flatten_nested_structure(nested_iterable: Iterable[Any], result: List[Any]) -> None:
    """
    Recursively flattens a nested iterable of arbitrary depth into a single list.

    - It traverses the input iterable item by item.
    - If an item is itself an iterable (but not a string or bytes), it recurses into it.
    - Otherwise, it appends the item to the result list.

    Args:
        nested_iterable: The input iterable that may contain nested iterables.
        result: The list to accumulate flattened items into.

    Side Effects:
        Modifies the 'result' list in place by appending flattened elements.
    """
    for item in nested_iterable:
        # Check if item is iterable but not a string or bytes (which are iterable but atomic for this context)
        if isinstance(item, (list, tuple, set, frozenset)):
            # Use a temporary list for recursive flattening to handle any depth
            _flatten_nested_structure(item, result)
        else:
            result.append(item)


def _get_frequency_map(flat_sequence: List[Any]) -> dict:
    """
    Calculates the frequency of each element in the given flat sequence.

    - Iterates through the flat sequence once.
    - Maintains a dictionary where keys are elements and values are their counts.

    Args:
        flat_sequence: A list of elements to count.

    Returns:
        A dictionary mapping each unique element to its occurrence count.
    """
    frequency_map: dict[Any, int] = {}

    for element in flat_sequence:
        if element in frequency_map:
            current_count = frequency_map[element]
            frequency_map[element] = current_count + 1
        else:
            frequency_map[element] = 1

    return frequency_map


def _filter_elements_with_min_count(frequency_map: dict[Any, int], min_count: int) -> List[Any]:
    """
    Filters elements from the frequency map that appear at least 'min_count' times.

    - Iterates through the keys of the frequency map.
    - Collects keys whose associated value is greater than or equal to min_count.
    - Returns the collected keys as a list.

    Args:
        frequency_map: A dictionary mapping elements to their occurrence counts.
        min_count: The minimum number of occurrences required to be included in the result.

    Returns:
        A list of elements that appear at least 'min_count' times in the original sequence.
    """
    common_elements: List[Any] = []

    for element, count in frequency_map.items():
        if count >= min_count:
            common_elements.append(element)

    return common_elements


def common_in_nested_lists(nested_lists: List[List[Any]]) -> List[Any]:
    """
    Finds common elements across all nested lists in the input.

    The function handles arbitrary nesting within the provided lists by:
    1. Flattening the structure to treat all nested lists as a single sequence of numbers.
    2. Counting the occurrences of each number.
    3. Returning numbers that appear in all lists.

    - If any nested list is empty, the result is an empty list.
    - The result is sorted based on the order of their first appearance in the first non-empty list.
    - Invalid inputs (e.g., non-list arguments) are not accepted and will raise an error.

    Args:
        nested_lists: A list of lists containing integers or other hashable elements.
                      Must be non-empty, and each item must be a list.

    Returns:
        A list of common elements present in all sublists, sorted by first appearance.

    Raises:
        TypeError: If nested_lists is not a list or if any item is not a list.
    """
    # Validate input type: nested_lists must be a list
    if not isinstance(nested_lists, list):
        raise TypeError("Expected input to be a list of lists.")

    if len(nested_lists) == 0:
        return []

    # Validate each item in the input list is itself a list
    for i, sublist in enumerate(nested_lists):
        if not isinstance(sublist, list):
            raise TypeError(f"All items must be lists. Item at index {i} is not a list.")

    # If any sublist is empty, there are no common elements
    for sublist in nested_lists:
        if len(sublist) == 0:
            return []

    # Count occurrences of each element across all flattened lists
    flattened_count_map: dict[Any, int] = {}

    for sublist in nested_lists:
        _flatten_nested_structure(sublist, flattened_count_map)

    # Determine the minimum count required for an element to be common
    # Since we are looking for elements present in ALL lists, the min count is the number of sublists
    num_sublists = len(nested_lists)
    min_required_count = num_sublists

    # Find elements that meet or exceed the minimum count
    common_elements_unsorted = _filter_elements_with_min_count(flattened_count_map, min_required_count)

    # Sort the result based on the first appearance in the first non-empty sublist
    # We reconstruct the order by iterating through the first sublist and checking membership
    if len(common_elements_unsorted) == 0:
        return []

    first_list = nested_lists[0]
    seen_ordered: List[Any] = []
    seen_set = set()

    for element in first_list:
        if element in common_elements_unsorted and element not in seen_set:
            seen_ordered.append(element)
            seen_set.add(element)
            if len(seen_ordered) == len(common_elements_unsorted):
                break

    return seen_ordered