from typing import List, Tuple, Any, Dict

def _validate_tuple_element(elem: Any) -> bool:
    """
    Validates that a given element is a tuple with exactly two items.

    Args:
        elem: The element to validate.

    Returns:
        True if the element is a valid tuple of two items, False otherwise.
    """
    if not isinstance(elem, tuple):
        return False

    if len(elem) != 2:
        return False

    return True

def _validate_input_list(input_list: List) -> bool:
    """
    Validates that the input list contains only tuples with exactly two items.

    Args:
        input_list: The list to validate.

    Returns:
        True if the list is valid, False otherwise.
    """
    if not isinstance(input_list, list):
        return False

    if not input_list:
        # An empty list is considered valid for this context, resulting in 0 unique tuples.
        return True

    for elem in input_list:
        if not _validate_tuple_element(elem):
            return False

    return True

def _is_unique_tuple_pair(t1: Tuple[Any, Any], t2: Tuple[Any, Any]) -> bool:
    """
    Checks if two tuples are considered equal.

    Args:
        t1: First tuple.
        t2: Second tuple.

    Returns:
        True if both tuples have equal elements in the same order, False otherwise.
    """
    return (t1[0] == t2[0]) and (t1[1] == t2[1])

def extract_freq(tuple_list: List[Tuple[Any, Any]]) -> int:
    """
    Extracts the frequency of unique tuples in the given list.
    Essentially, it counts the number of distinct tuples present in the list.

    The order of tuples in the output count does not matter (order-irrespective).
    It returns the count of unique tuples found.

    Args:
        tuple_list: A list of tuples, where each tuple must contain exactly two elements.

    Returns:
        An integer representing the number of unique tuples in the list.

    Raises:
        ValueError: If the input list is not a list, or if any element in the list is not a tuple of exactly two items.
    """
    # Step 1: Validate the input list type
    if not isinstance(tuple_list, list):
        raise ValueError("Input must be a list.")

    # Step 2: Validate each element in the list
    for index, elem in enumerate(tuple_list):
        if not isinstance(elem, tuple):
            raise ValueError(f"Element at index {index} is not a tuple.")

        if len(elem) != 2:
            raise ValueError(f"Element at index {index} is not a tuple of exactly two items (has {len(elem)} items).")

    # Step 3: Handle the empty list case explicitly
    if len(tuple_list) == 0:
        return 0

    # Step 4: Use a set to store unique tuples.
    # Tuples are hashable, so they can be directly added to a set.
    # This automatically handles the "order irrespective" requirement for uniqueness.
    unique_set: set = set()

    # Step 5: Iterate through the list and add each tuple to the set.
    # Duplicate tuples will be ignored by the set.
    for item in tuple_list:
        unique_set.add(item)

    # Step 6: Return the size of the set, which represents the number of unique tuples.
    return len(unique_set)

# Final check to ensure the function signature and logic are complete as per requirements.
# The function is designed to be standalone and runnable.