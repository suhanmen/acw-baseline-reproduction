def remove_elements(list1, list2):
    """
    Remove all elements from list1 that are present in list2 and return the modified list1.

    This function handles various edge cases such as empty lists, single-element lists,
    lists with all equal elements, boundary values, zero/negative numbers, and any other
    degenerate cases. It ensures that invalid inputs are handled explicitly.
    """
    # Validate inputs: both list1 and list2 must be lists
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")

    # Validate inputs: list2 must not be empty
    if len(list2) == 0:
        return list1.copy()  # Return a copy to avoid modifying the original list1

    # Create a set of elements to remove for O(1) lookups
    elements_to_remove = set(list2)

    # Remove elements from list1 that are in elements_to_remove
    result = [element for element in list1 if element not in elements_to_remove]

    # Return a copy of the result to avoid modifying the original list1
    return result.copy()