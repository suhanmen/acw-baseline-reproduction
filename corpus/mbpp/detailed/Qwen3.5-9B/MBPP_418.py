from typing import Any, List, Optional

def _is_valid_nested_list(nested_list: Any) -> bool:
    """
    Validates that the input is a list where each element is also a list.

    Returns True if valid, False otherwise.
    """
    if not isinstance(nested_list, list):
        return False

    for item in nested_list:
        if not isinstance(item, list):
            return False

    return True

def _get_element_length(element: Any) -> int:
    """
    Returns the length of a list element.

    If the element is not a list, returns 0.
    """
    if isinstance(element, list):
        return len(element)
    return 0

def _find_maximum_element(items: List[Any]) -> Any:
    """
    Finds the element with the maximum length in the provided list.

    In case of ties, returns the first occurrence.

    Raises:
        ValueError: If the input list is empty.
    """
    if not items:
        raise ValueError("Cannot find maximum in an empty list.")

    max_length = -1
    max_element = None

    for item in items:
        current_length = _get_element_length(item)

        # Update if current length is greater than max_length
        if current_length > max_length:
            max_length = current_length
            max_element = item

    if max_element is None:
        raise RuntimeError("Internal error: max_element was never set.")

    return max_element

def Find_Max(nested_list: Any) -> Optional[List[Any]]:
    """
    Finds the sublist having the maximum length within the given nested list.

    Args:
        nested_list: A list of lists containing elements of any type.

    Returns:
        The sublist with the maximum length.
        Returns None if the input is invalid or empty.
        Returns an empty list if the input contains no sublists (e.g., [[]]).

    Raises:
        ValueError: If the input is not a list or contains non-list elements.
    """
    # Step 1: Validate the outer structure
    if not _is_valid_nested_list(nested_list):
        # Determine specific error for better debugging
        if not isinstance(nested_list, list):
            raise ValueError("Input must be a list of lists.")
        else:
            raise ValueError("All elements in the input list must be lists.")

    # Step 2: Check if the nested list is empty
    if len(nested_list) == 0:
        return None

    # Step 3: Handle the degenerate case where all sublists are empty lists [[]]
    # In this case, technically any empty list is a max length (0), 
    # but often "find sublist" implies returning one of them if valid.
    # Based on typical problem constraints, returning the first empty list is consistent.
    # However, if the problem implies returning nothing for truly empty content, 
    # we rely on the caller checking the result. 
    # Let's proceed with the standard logic which will naturally pick the first one.

    # Step 4: Delegate to the helper to find the maximum element
    try:
        result = _find_maximum_element(nested_list)
        return result
    except ValueError as ve:
        # Re-raise or handle appropriately. For production, re-raising is usually best.
        raise ve