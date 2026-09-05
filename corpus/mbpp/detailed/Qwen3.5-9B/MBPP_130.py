from typing import List, Tuple, Union, Optional
import collections

def _validate_list_input(input_list: Union[List[int], List[float], List[str], List[bool], None]) -> List:
    """
    Validates that the input is a non-empty list.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list is empty.
    """
    if input_list is None:
        raise ValueError("Input cannot be None.")

    if not isinstance(input_list, list):
        raise TypeError(f"Input must be a list, but got {type(input_list).__name__}.")

    if len(input_list) == 0:
        raise ValueError("Input list cannot be empty.")

    return input_list

def _build_frequency_map(valid_list: List) -> dict:
    """
    Constructs a frequency map (dictionary) from the valid input list.

    Args:
        valid_list: The list to count occurrences for.

    Returns:
        A dictionary mapping each unique element to its count.
    """
    frequency_map = collections.defaultdict(int)

    for item in valid_list:
        frequency_map[item] += 1

    return dict(frequency_map)

def _find_max_occurrence_item(frequency_map: dict) -> Tuple:
    """
    Iterates through the frequency map to find the item with the maximum count.

    In case of a tie, the item that appears first in the map (based on insertion order)
    will be returned, or we can strictly define behavior. Here, we return the first
    item encountered with the maximum value during iteration.

    Args:
        frequency_map: A dictionary mapping items to their counts.

    Returns:
        A tuple (item, count) representing the item and its maximum frequency.
    """
    if not frequency_map:
        # This case should technically be impossible if validation passed,
        # but kept for safety in helper isolation.
        raise RuntimeError("Frequency map should not be empty at this stage.")

    max_item = None
    max_count = -1

    for item, count in frequency_map.items():
        if count > max_count:
            max_count = count
            max_item = item

    return (max_item, max_count)

def max_occurrences(input_list: List) -> Tuple:
    """
    Finds the item with the maximum frequency in a given list.

    This function performs the following steps explicitly:
    1. Validates the input list is not None and is a list type.
    2. Validates the list is not empty.
    3. Constructs a frequency map counting occurrences of each element.
    4. Iterates through the frequency map to identify the item with the highest count.
    5. Returns a tuple (item, count).

    If multiple items share the same maximum frequency, the function returns the
    one that appears first in the original list's traversal order (determined by
    insertion order into the frequency map).

    Args:
        input_list: A list of hashable elements (integers, floats, strings, etc.).

    Returns:
        A tuple containing the element with the highest frequency and its count.
        Example: (2, 5) means '2' appeared 5 times.

    Raises:
        TypeError: If input is not a list.
        ValueError: If input is None or the list is empty.
    """
    # Step 1: Input Validation
    validated_list = _validate_list_input(input_list)

    # Step 2: Build Frequency Map
    frequency_map = _build_frequency_map(validated_list)

    # Step 3: Find Maximum Occurrence
    result = _find_max_occurrence_item(frequency_map)

    return result