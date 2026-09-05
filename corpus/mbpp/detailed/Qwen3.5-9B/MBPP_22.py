from typing import List, Optional

def validate_input(input_list: List[int]) -> bool:
    """
    Validates that the input is a list and contains only integers.

    Args:
        input_list: The list to validate.

    Returns:
        True if valid, False otherwise.
    """
    if not isinstance(input_list, list):
        return False

    for element in input_list:
        if not isinstance(element, int):
            return False

    return True

def create_seen_set() -> set:
    """
    Creates an empty set to track elements we have encountered so far.

    Returns:
        An empty set.
    """
    return set()

def find_first_duplicate(input_list: List[int]) -> int:
    """
    Finds the first duplicate element in a given array of integers.

    The "first duplicate" is defined as the element that appears a second time
    at the earliest index position in the array.

    For example:
    - [1, 2, 3, 4, 4, 5] -> 4 (appears at index 4, which is the first time any 
      value has been seen twice)
    - [1, 1, 2, 3, 3, 2, 2] -> 1 (the second 1 is at index 1, which comes before 
      the second 2 at index 5)
    - [1, 2, 3, 4] -> -1 (no duplicates)

    Args:
        input_list: A list of integers.

    Returns:
        The first duplicate element if found, otherwise -1.

    Raises:
        ValueError: If the input is not a list of integers.
    """
    # Step 1: Validate the input
    if not validate_input(input_list):
        raise ValueError("Input must be a list of integers.")

    # Step 2: Handle empty input case
    if len(input_list) == 0:
        return -1

    # Step 3: Initialize tracking structures
    seen_elements = create_seen_set()
    first_duplicate_value: Optional[int] = None

    # Step 4: Iterate through the list to find duplicates
    for current_index in range(len(input_list)):
        current_element = input_list[current_index]

        # Step 5: Check if we've already seen this element
        if current_element in seen_elements:
            # Step 6: This is our first duplicate found
            # We return immediately because we want the first occurrence in the sequence
            return current_element

        # Step 7: Mark this element as seen
        seen_elements.add(current_element)

    # Step 8: No duplicate was found after checking all elements
    return -1