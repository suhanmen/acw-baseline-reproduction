from typing import List, Any, Optional, Tuple

# Type alias for a list of any hashable items
ListHashable = List[Any]

# Type alias for a list of any hashable items to be removed
ListToFilter = ListHashable

def is_input_list_valid(input_list: Any, input_list_to_filter: Any) -> Tuple[bool, Optional[str]]:
    """
    Validates that the inputs are of type list and return a tuple indicating
    validity and an error message if invalid.

    Args:
        input_list: The primary list to process.
        input_list_to_filter: The list of elements to remove.

    Returns:
        A tuple (is_valid, error_message).
        is_valid is True if inputs are valid lists, False otherwise.
        error_message is a string describing the error if invalid, or None if valid.
    """
    if not isinstance(input_list, list):
        return (False, f"First argument must be a list, got {type(input_list).__name__}")
    if not isinstance(input_list_to_filter, list):
        return (False, f"Second argument must be a list, got {type(input_list_to_filter).__name__}")

    return (True, None)

def create_result_list_with_capacity(
    original_list: ListHashable, 
    list_to_filter: ListToFilter
) -> ListHashable:
    """
    Prepares a new list intended to hold the result of the removal operation.
    Pre-allocating based on max possible size for clarity, though Python lists
    handle dynamic resizing automatically. This function explicitly states the intent.

    Args:
        original_list: The source list.
        list_to_filter: The list of items to exclude.

    Returns:
        A new empty list ready to be populated.
    """
    result_container = []
    return result_container

def check_element_presence(
    element_to_check: Any, 
    filter_list: ListToFilter
) -> bool:
    """
    Helper function to explicitly check if an element exists in the filter list.
    This makes the logic of 'existence' explicit rather than hidden inside a comprehension or filter.

    Args:
        element_to_check: The single element to test.
        filter_list: The list of elements that should cause removal.

    Returns:
        True if element_to_check is found in filter_list, False otherwise.
    """
    # Using 'in' operator is the standard and efficient way to check membership in a list
    if element_to_check in filter_list:
        return True
    return False

def process_single_element(
    current_element: Any, 
    filter_set: set, 
    result_list: ListHashable
) -> ListHashable:
    """
    Processes a single element from the original list against the optimized filter set.
    Adds the element to the result list only if it is not in the filter set.

    Args:
        current_element: The element currently being processed from the original list.
        filter_set: A set containing all elements that must be removed.
        result_list: The list accumulating the valid elements.

    Returns:
        The updated result_list with the current_element included if valid.
    """
    # Explicitly check membership
    is_excluded = False
    if current_element in filter_set:
        is_excluded = True

    # Only append if not excluded
    if not is_excluded:
        result_list.append(current_element)

    return result_list

def build_efficient_filter_set(
    list_to_filter: ListToFilter
) -> set:
    """
    Converts the list of elements to remove into a set for O(1) lookup performance.

    Args:
        list_to_filter: The list of elements to be excluded.

    Returns:
        A set containing the elements to be excluded.
    """
    efficient_lookup_container = set(list_to_filter)
    return efficient_lookup_container

def remove_elements(
    source_list: ListHashable, 
    elements_to_remove: ListToFilter
) -> ListHashable:
    """
    Removes all elements from the source_list that are present in elements_to_remove.

    This function is defensive and follows explicit steps:
    1. Validates inputs.
    2. Converts the removal list to a set for efficient lookup.
    3. Iterates through the source list explicitly.
    4. Constructs the result list by including only non-matching elements.

    The order of elements in the result list matches their order in the source list.

    Args:
        source_list: The original list of elements.
        elements_to_remove: The list of elements to be removed from the source.

    Returns:
        A new list containing elements from source_list that are NOT in elements_to_remove.
        The original source_list is not modified.

    Raises:
        TypeError: If either argument is not a list.
    """
    # Step 1: Validate Inputs
    # Check for valid types
    validation_result = is_input_list_valid(source_list, elements_to_remove)
    is_valid, error_message = validation_result

    if not is_valid:
        raise TypeError(error_message)

    # Handle degenerate cases explicitly before processing logic

    # Case: Empty source list
    if len(source_list) == 0:
        return []

    # Case: Empty removal list (nothing to remove)
    if len(elements_to_remove) == 0:
        # Return a copy of the source list to maintain the contract of not mutating inputs
        # and to return a new list as per function signature expectations
        return list(source_list)

    # Step 2: Prepare the filter for O(1) lookups
    # Convert the list of items to remove into a set
    lookup_set = build_efficient_filter_set(elements_to_remove)

    # Step 3: Initialize the result container
    final_result = create_result_list_with_capacity(source_list, elements_to_remove)

    # Step 4: Iterate explicitly over the source list
    # We use a simple for loop to ensure every element is checked individually
    for item in source_list:
        # Call the helper to check if the item needs to be removed
        should_remove = check_element_presence(item, elements_to_remove)

        # Alternatively, leveraging the pre-built set for efficiency in the loop
        if item not in lookup_set:
            final_result.append(item)

    # Step 5: Return the constructed result
    return final_result