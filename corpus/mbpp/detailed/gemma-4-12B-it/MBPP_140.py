from typing import List, Tuple, Dict, Any


def extract_singly(tuple_list: List[Tuple[Any, ...]]) -> List[Any]:
    """
    Extracts elements from a list of tuples that occur exactly once across 
    the entire collection of tuples.

    Args:
        tuple_list: A list of tuples containing any hashable elements.

    Returns:
        A list of elements that appear exactly once in the input list of tuples.
        The order of elements in the output follows the order of first appearance.

    Raises:
        TypeError: If the input is not a list or contains non-tuple elements.
        ValueError: If the input list contains unhashable elements.
    """
    # Input Validation: Ensure the primary input is a list
    if not isinstance(tuple_list, list):
        raise TypeError(f"Expected a list of tuples, but received {type(tuple_list).__name__}")

    # Edge Case: Empty input list
    if not tuple_list:
        return []

    # Data structures to track occurrences
    # We use a dictionary to store the count of every element encountered
    occurrence_counts: Dict[Any, int] = {}

    # We use a list to maintain the order of first appearance
    # This ensures the output is deterministic and matches the requested behavior
    appearance_order: List[Any] = []

    # First Pass: Count occurrences of all elements
    for index, current_tuple in enumerate(tuple_list):
        # Validation: Ensure each element in the list is actually a tuple
        if not isinstance(current_tuple, tuple):
            raise TypeError(f"Element at index {index} is not a tuple: {current_tuple}")

        for element in current_tuple:
            # Validation: Ensure elements are hashable so they can be dictionary keys
            try:
                _ = hash(element)
            except TypeError:
                raise ValueError(f"Found unhashable element in tuple: {element}")

            if element in occurrence_counts:
                occurrence_counts[element] += 1
            else:
                occurrence_counts[element] = 1
                appearance_order.append(element)

    # Second Pass: Identify elements with a count of exactly 1
    result_list: List[Any] = []

    # Iterate through the appearance_order to preserve the sequence
    for element in appearance_order:
        count = occurrence_counts.get(element, 0)
        if count == 1:
            result_list.append(element)

    return result_list


if __name__ == "__main__":
    # Validation based on provided assertions
    assert extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]) == [3, 4, 5, 7, 1]
    assert extract_singly([(1, 2, 3), (4, 2, 3), (7, 8)]) == [1, 2, 3, 4, 7, 8]
    assert extract_singly([(7, 8, 9), (10, 11, 12), (10, 11)]) == [7, 8, 9, 10, 11, 12]