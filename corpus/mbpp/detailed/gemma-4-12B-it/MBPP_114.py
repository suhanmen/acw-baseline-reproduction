from typing import List, Tuple, Dict

def assign_freq(tuple_list: List[Tuple[int, ...]]) -> str:
    """
    Assigns a frequency count to each unique tuple in a list of tuples.
    The final result maintains the order of first appearance of each unique tuple
    and appends the count of occurrences to the end of each tuple.

    Args:
        tuple_list: A list of tuples containing integers.

    Returns:
        A string representation of a list of tuples, where each tuple 
        now includes its frequency as the last element.
    """
    # Validate input type
    if not isinstance(tuple_list, list):
        raise ValueError("Input must be a list of tuples.")

    # Handle the empty list case explicitly
    if not tuple_list:
        return "[]"

    # Step 1: Count the occurrences of each unique tuple.
    # We use a dictionary to map the tuple (as a key) to its count (as a value).
    # Tuples are hashable, so they can serve as dictionary keys.
    frequency_map: Dict[Tuple[int, ...], int] = {}

    for current_tuple in tuple_list:
        # Validate that the element is actually a tuple
        if not isinstance(current_tuple, tuple):
            raise ValueError("All elements in the list must be tuples.")

        # Increment the count in the dictionary
        if current_tuple in frequency_map:
            frequency_map[current_tuple] += 1
        else:
            frequency_map[current_tuple] = 1

    # Step 2: Build the result list while preserving the order of first appearance.
    # We iterate through the original input list to ensure the output order matches
    # the order in which unique tuples first appeared.
    processed_tuples: List[Tuple[int, ...]] = []
    seen_tuples: set = set()

    for original_tuple in tuple_list:
        # If we have already added this tuple's processed version to our result, skip it.
        if original_tuple in seen_tuples:
            continue

        # Retrieve the count from our frequency map.
        occurrence_count = frequency_map[original_tuple]

        # Create a new tuple by appending the count.
        # Conversion to list is necessary to append, then back to tuple.
        base_elements = list(original_tuple)
        base_elements.append(occurrence_count)
        new_tuple = tuple(base_elements)

        # Add to the result list and mark as seen.
        processed_tuples.append(new_tuple)
        seen_tuples.add(original_tuple)

    # Step 3: Convert the list of tuples to a string representation.
    # The problem requirements show a string representation of the list.
    # Note: Python's str(list_of_tuples) matches the expected output format.
    result_string = str(processed_tuples)

    return result_string