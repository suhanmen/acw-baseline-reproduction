from typing import Tuple, Any, Iterable

def validate_tuple_input(item: Any) -> Tuple[bool, str]:
    """
    Validates that the input is a tuple.

    Args:
    item: The input to validate.

    Returns:
    A tuple (is_valid, error_message) where is_valid is a boolean and error_message
    describes the error if the input is invalid, or an empty string if valid.
    """
    if not isinstance(item, tuple):
        return False, "Input must be a tuple."
    return True, ""

def check_distinct(input_data: Tuple[Any, ...]) -> bool:
    """
    Checks if all elements in the given tuple are distinct.

    This function performs several steps:
    1. Validates that the input is indeed a tuple.
    2. Handles the edge case where the tuple is empty (considers it distinct).
    3. Iterates through the tuple to find any duplicate elements.
    4. Returns True if no duplicates are found, False otherwise.

    Args:
    input_data: The tuple of elements to check for distinctness.

    Returns:
    True if all elements in the tuple are distinct, False otherwise.

    Raises:
    TypeError: If the input is not a tuple.
    """

    # Step 1: Validate input type
    is_valid, error_message = validate_tuple_input(input_data)

    if not is_valid:
        raise TypeError(error_message)

    # Step 2: Handle empty tuple edge case
    if len(input_data) == 0:
        # An empty tuple has no duplicates, so it is considered distinct
        return True

    # Step 3: Initialize a set to track seen elements
    seen_elements: set = set()

    # Step 4: Iterate through each element in the tuple
    for element in input_data:
        # Step 4a: Check if the current element is already in the set of seen elements
        if element in seen_elements:
            # If found, the tuple is not distinct
            return False

        # Step 4b: Add the current element to the set of seen elements
        seen_elements.add(element)

    # Step 5: If the loop completes without finding duplicates, the tuple is distinct
    return True