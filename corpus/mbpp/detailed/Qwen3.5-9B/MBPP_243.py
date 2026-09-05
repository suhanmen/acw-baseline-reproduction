from typing import Any, List, Tuple, Dict

def sort_on_occurence(tuples_list: List[Tuple[Any, ...]]) -> List[Any]:
    """
    Sorts the given list of tuples based on the occurrence (frequency) of their first element.

    The function returns a flattened list where:
    1. Elements are grouped by their first tuple element's value.
    2. Groups are ordered by the frequency of that first element in descending order.
    3. Within each group, elements appear in the order of their original appearance.
    4. After all tuples from a group are added, the total count of that group is appended.

    Args:
        tuples_list: A list of tuples where each tuple contains at least one element.

    Returns:
        A list containing the sorted elements followed by the occurrence counts for each group.

    Raises:
        TypeError: If the input is not a list or contains non-tuple elements.
        ValueError: If any tuple is empty.
    """

    # Step 1: Validate the input type
    if not isinstance(tuples_list, list):
        raise TypeError("Input must be a list.")

    # Step 2: Validate that every element in the list is a tuple
    for item in tuples_list:
        if not isinstance(item, tuple):
            raise TypeError(f"All elements must be tuples, but found: {type(item).__name__}")

    # Step 3: Validate that no tuple is empty
    for index, item in enumerate(tuples_list):
        if len(item) == 0:
            raise ValueError(f"Tuple at index {index} cannot be empty.")

    # Step 4: Extract the first element of each tuple
    first_elements: List[Any] = []
    for item in tuples_list:
        first_elements.append(item[0])

    # Step 5: Count the frequency of each first element
    frequency_map: Dict[Any, int] = {}
    for value in first_elements:
        if value in frequency_map:
            frequency_map[value] += 1
        else:
            frequency_map[value] = 1

    # Step 6: Sort the unique first elements by their frequency in descending order
    # If frequencies are equal, we maintain the original relative order (stable sort logic applied manually below)
    unique_keys = list(frequency_map.keys())
    sorted_keys = sorted(unique_keys, key=lambda x: frequency_map[x], reverse=True)

    # Step 7: Reconstruct the original list structure to preserve relative order for equal frequencies
    # We need to map each original tuple to its group key and count
    tuple_with_meta: List[Tuple[Tuple[Any, ...], Any, int]] = []

    for index, item in enumerate(tuples_list):
        key = item[0]
        count = frequency_map[key]
        tuple_with_meta.append((item, key, count))

    # Step 8: Group the items by their key while preserving original relative order within groups
    grouped_items: Dict[Any, List[Tuple[Tuple[Any, ...], Any, int]]] = {}

    for entry in tuple_with_meta:
        item, key, count = entry
        if key not in grouped_items:
            grouped_items[key] = []
        grouped_items[key].append(entry)

    # Step 9: Build the result list
    result: List[Any] = []

    for key in sorted_keys:
        group_entries = grouped_items[key]

        # Add all tuples from this group in their original relative order
        for entry in group_entries:
            item, _, _ = entry
            result.append(item)

        # Append the occurrence count for this group
        result.append(frequency_map[key])

    return result