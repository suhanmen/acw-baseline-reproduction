from typing import Any, List, Optional

def _validate_input_list(data: Any) -> Optional[List[Any]]:
    """
    Validates that the input is a list and returns it.
    Returns None if validation fails.
    """
    if not isinstance(data, list):
        return None
    return data

def _check_single_element_list(elements: List[Any]) -> bool:
    """
    Handles the edge case where the list contains exactly one element.
    A single-element list is considered to have all same elements.
    """
    if len(elements) <= 1:
        return True
    return False

def _compare_all_elements_equal(elements: List[Any]) -> bool:
    """
    Iterates through the list to verify if every element is equal to the first one.
    Returns True if all are equal, False otherwise.
    """
    if not elements:
        return True

    first_element = elements[0]
    is_all_equal = True

    for index in range(1, len(elements)):
        current_element = elements[index]
        if current_element is not first_element:
            is_all_equal = False
            break

    return is_all_equal

def chkList(data: Any) -> bool:
    """
    Checks whether all elements in the provided list are the same.

    Handles:
    - Invalid types (non-list input)
    - Empty lists
    - Single element lists
    - Lists with mixed types or values

    Returns:
        True if all elements are identical.
        False otherwise or if input is invalid.
    """
    # Step 1: Validate input
    validated_list = _validate_input_list(data)

    if validated_list is None:
        return False

    # Step 2: Handle empty list edge case
    if len(validated_list) == 0:
        return True

    # Step 3: Handle single element edge case
    if len(validated_list) == 1:
        return True

    # Step 4: Compare all elements against the first one
    return _compare_all_elements_equal(validated_list)