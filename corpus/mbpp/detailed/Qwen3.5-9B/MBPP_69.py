from typing import List, Any, Tuple

def _validate_main_list(main_list: Any) -> None:
    """
    Validates that the main list argument is indeed a list.
    Raises a TypeError if the argument is not a list.
    """
    if not isinstance(main_list, list):
        raise TypeError(
            f"Expected a list for the main list, but got {type(main_list).__name__} instead."
        )

def _validate_sublist(sublist: Any) -> None:
    """
    Validates that the sublist argument is indeed a list.
    Raises a TypeError if the argument is not a list.
    """
    if not isinstance(sublist, list):
        raise TypeError(
            f"Expected a list for the sublist, but got {type(sublist).__name__} instead."
        )

def _initialize_length_variable(main_list: List[Any]) -> int:
    """
    Calculates and returns the length of the main list.
    """
    return len(main_list)

def _initialize_length_variable_sublist(sublist: List[Any]) -> int:
    """
    Calculates and returns the length of the sublist.
    """
    return len(sublist)

def _is_sublist_condition_satisfied(
    remaining_main_list: List[Any],
    remaining_sublist: List[Any]
) -> bool:
    """
    Checks if the current remaining sublist matches the start of the current remaining main list.
    Returns True if they match exactly, False otherwise.
    """
    if not remaining_sublist:
        return True

    if not remaining_main_list:
        return False

    # Check if the first element matches
    if remaining_main_list[0] != remaining_sublist[0]:
        return False

    # Recursively check the rest of the elements
    return _is_sublist_condition_satisfied(
        remaining_main_list[1:],
        remaining_sublist[1:]
    )

def is_sublist(main_list: List[Any], sublist: List[Any]) -> bool:
    """
    Checks whether a given sublist exists within the main list.

    This function performs a linear search through the main_list to find 
    any occurrence where the sublist appears consecutively.

    Edge cases handled:
    - Empty sublist: Always True (empty sequence is a sublist of any sequence).
    - Empty main list: True if sublist is empty, False otherwise.
    - Non-list inputs: Raises TypeError.

    Args:
        main_list: The list in which to search for the sublist.
        sublist: The list to search for.

    Returns:
        True if sublist is found within main_list, False otherwise.

    Raises:
        TypeError: If either argument is not a list.
    """
    # Step 1: Validate input types
    _validate_main_list(main_list)
    _validate_sublist(sublist)

    # Step 2: Extract lengths for potential early exit optimization
    main_length = _initialize_length_variable(main_list)
    sublist_length = _initialize_length_variable_sublist(sublist)

    # Step 3: Handle the special case where the sublist is empty
    # An empty list is technically a sublist of any list (including empty)
    if sublist_length == 0:
        return True

    # Step 4: Handle the case where the sublist is longer than the main list
    # This is impossible, so we can immediately return False
    if sublist_length > main_length:
        return False

    # Step 5: Iterate through the main list to find a starting position
    # We only need to check up to (main_length - sublist_length)
    # because any starting position after that wouldn't have enough 
    # remaining elements to match the full sublist.
    current_index = 0

    while current_index <= (main_length - sublist_length):
        # Extract the slice of the main list starting at current_index
        # with a length equal to the sublist
        candidate_slice = main_list[current_index : current_index + sublist_length]

        # Check if this candidate slice matches the sublist element by element
        match_found = True

        # Iterate through the sublist to compare each element
        sub_index = 0
        while sub_index < sublist_length:
            if candidate_slice[sub_index] != sublist[sub_index]:
                match_found = False
                break
            sub_index += 1

        # If we found a match, return True immediately
        if match_found:
            return True

        # Move to the next potential starting position
        current_index += 1

    # Step 6: If no match was found after checking all possible positions
    return False