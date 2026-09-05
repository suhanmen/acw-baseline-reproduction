from typing import List, Tuple, Any, Optional, Union

Number = Union[int, float]

# Type alias for the return tuple to make it explicit in function signature
SearchResult = Tuple[bool, int]


def _validate_array(data: Any) -> List[Number]:
    """
    Validates that the input is a list containing only numeric elements.
    Raises TypeError if validation fails.
    """
    if not isinstance(data, list):
        raise TypeError(f"Input must be a list, got {type(data).__name__} instead.")

    if len(data) == 0:
        return []

    for i, item in enumerate(data):
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"All elements must be numeric. "
                f"Invalid element found at index {i}: {item!r} (type: {type(item).__name__})."
            )

    return data


def _find_target_index(searched_list: List[Number], target: Number) -> Optional[int]:
    """
    Performs the sequential search logic.

    Iterates through the list from index 0 to the end.
    If the current element matches the target, returns its index immediately.
    If the loop completes without finding a match, returns None.

    Args:
        searched_list: The list of numbers to search within.
        target: The numeric value to search for.

    Returns:
        The index of the first occurrence of the target, or None if not found.
    """
    index = 0
    total_items = len(searched_list)

    # Handle the degenerate case of an empty list explicitly for clarity
    # (Though _validate_array allows empty lists, the search logic must handle them)
    if total_items == 0:
        return None

    while index < total_items:
        current_element = searched_list[index]

        if current_element == target:
            # Match found. 
            # Note: We cast to int for the return type consistency with the requirements,
            # assuming indices are integers which they always are in Python lists.
            return index

        index += 1

    # If we exit the loop here, the target was not found.
    return None


def sequential_search(search_array: List[Number], element: Number) -> SearchResult:
    """
    Searches for a specific element in a given array using sequential (linear) search.

    This function performs a linear scan from the beginning of the array to the end.
    It returns a tuple containing:
    - A boolean indicating whether the element was found.
    - The integer index where the element was found (1-based as per the problem requirements),
      or 0 if not found.

    Based on the provided assertions:
    - sequential_search([11,23,58,31,...], 31) returns (True, 3) -> 31 is at 0-based index 2.
    - This implies the problem requires 1-based indexing for the result.

    Args:
        search_array: The list of numbers to search through.
        element: The numeric value to search for.

    Returns:
        A tuple (found: bool, position: int).
        - found is True if element is in search_array, False otherwise.
        - position is the 1-based index of the element if found, otherwise 0.

    Raises:
        TypeError: If the input array is not a list or contains non-numeric values.
    """
    # Step 1: Validate inputs and convert to a usable list structure
    validated_array = _validate_array(search_array)

    # Step 2: Retrieve the target value we are looking for
    target = element

    # Step 3: Perform the actual search logic
    zero_based_index = _find_target_index(validated_array, target)

    # Step 4: Format the result based on the requirements
    # Requirements show: (True, 3) for an element at 0-based index 2.
    # This confirms 1-based indexing is required.

    if zero_based_index is not None:
        # Found the element
        one_based_index = zero_based_index + 1
        return (True, one_based_index)
    else:
        # Element not found
        return (False, 0)