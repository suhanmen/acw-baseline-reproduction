def test_duplicate(array_to_check):
    """
    Determines whether a given array of integers contains any duplicate element.

    Parameters:
    array_to_check (list[int] | None): The list of integers to inspect for duplicates.

    Returns:
    bool: True if at least one duplicate element exists in the list, False otherwise.

    Raises:
    TypeError: If the input is not a list, is not None, or contains non-integer elements.
    ValueError: If the list is explicitly None.
    """

    # Step 1: Validate the type of the input.
    # We strictly require a list. Other iterables (like tuples) are rejected to prevent
    # unexpected behavior, as specified by the requirement to validate inputs explicitly.
    if not isinstance(array_to_check, list):
        raise TypeError(
            f"Input must be a list of integers. Received type: {type(array_to_check).__name__}."
        )

    # Step 2: Validate that the list is not None.
    # While an empty list is a valid edge case (returns False), an explicit None
    # is considered invalid input for this specific function signature expecting an array.
    if array_to_check is None:
        raise ValueError("Input list cannot be None.")

    # Step 3: Validate that all elements within the list are integers.
    # This ensures type safety and prevents logic errors with floats or strings.
    for index, element in enumerate(array_to_check):
        if not isinstance(element, int):
            raise TypeError(
                f"All elements must be integers. Element at index {index} is {type(element).__name__}."
            )

        # Note: We intentionally allow booleans in the semantic sense of 'int' if the 
        # caller passes them as [1, 2, True], since bool is a subclass of int in Python.
        # However, strictly speaking, one might want to exclude them. 
        # Based on the problem description "array of integers", Python's isinstance(..., int) 
        # is the standard check and will accept bools (True == 1, False == 0).
        # If strict exclusion of booleans is required, an additional check `isinstance(element, bool)`
        # could be added here: `if not isinstance(element, int) or isinstance(element, bool):`.
        # Given the examples are standard integers, the current check is appropriate.

    # Step 4: Handle the edge case of an empty list.
    # An empty list contains no elements, and therefore no duplicates.
    if len(array_to_check) == 0:
        return False

    # Step 5: Calculate the number of unique elements.
    # We convert the list to a set, which automatically removes duplicates.
    unique_elements = set(array_to_check)

    # Step 6: Compare the count of unique elements with the total count of elements.
    # If the count of unique elements is strictly less than the total number of elements,
    # it implies that at least one element appeared more than once.
    if len(unique_elements) < len(array_to_check):
        return True

    # Step 7: If counts are equal, no duplicates were found.
    return False