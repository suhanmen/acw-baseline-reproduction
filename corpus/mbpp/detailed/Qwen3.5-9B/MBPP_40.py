from collections import Counter
from typing import Any, List, Dict


def _validate_input_list(input_list: List[List[Any]]) -> None:
    """
    Validates that the input is a non-None list where every element is also a list.

    Args:
        input_list: The list to validate.

    Raises:
        TypeError: If input is not a list or contains non-list elements.
    """
    if input_list is None:
        raise TypeError("Input must be a list.")

    if not isinstance(input_list, list):
        raise TypeError("Input must be a list of lists.")

    for index, element in enumerate(input_list):
        if not isinstance(element, list):
            raise TypeError(f"Element at index {index} is not a list.")


def _flatten_nested_lists(nested_list: List[List[Any]]) -> List[Any]:
    """
    Flattens a list of lists into a single list containing all elements.

    Args:
        nested_list: A list where each element is itself a list.

    Returns:
        A single list containing all elements from the inner lists in order.
    """
    flattened_items = []

    for inner_list in nested_list:
        for item in inner_list:
            flattened_items.append(item)

    return flattened_items


def freq_element(list_of_lists: List[List[Any]]) -> Dict[Any, int]:
    """
    Finds the frequency of each element in a given list of lists.

    This function takes a list of lists as input, flattens it into a single sequence,
    counts the occurrences of each unique element using the Counter class from
    the collections module, and returns the result as a dictionary.

    Args:
        list_of_lists: A list containing multiple lists of elements.

    Returns:
        A dictionary where keys are the unique elements found and values are
        the counts of those elements.

    Raises:
        TypeError: If the input is not a list of lists.
    """
    # Step 1: Validate the input structure explicitly
    _validate_input_list(list_of_lists)

    # Step 2: Handle the edge case of an empty list of lists
    if len(list_of_lists) == 0:
        return {}

    # Step 3: Flatten the list of lists into a single list of elements
    all_elements = _flatten_nested_lists(list_of_lists)

    # Step 4: Handle the case where the flattened list is empty (e.g., [[]])
    if len(all_elements) == 0:
        return {}

    # Step 5: Count frequencies using Counter
    frequency_counter = Counter(all_elements)

    # Step 6: Convert Counter object to a standard dictionary
    result_dict = dict(frequency_counter)

    return result_dict