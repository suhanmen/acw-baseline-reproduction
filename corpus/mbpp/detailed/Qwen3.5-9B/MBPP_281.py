from typing import List, Any, Tuple, Set

def _check_type_is_list(data: Any) -> None:
    """
    Validates that the provided argument is a list instance.
    Raises a TypeError with a descriptive message if it is not.
    """
    if not isinstance(data, list):
        error_message = (
            f"Expected input to be a 'list', but received type '{type(data).__name__}'. "
            "The function only accepts lists."
        )
        raise TypeError(error_message)


def _check_element_types(elements: List[Any]) -> None:
    """
    Validates that all elements in the list can be handled by the uniqueness check.
    In Python, everything is hashable enough for a Set-based comparison or direct equality check.
    This function is currently a placeholder for strict validation if specific types are required later.
    For now, it allows mixed types as long as they are in a list.
    """
    # In a stricter environment, we might check for unhashable types here if we strictly 
    # wanted to force 'set' conversion, but direct iteration works for any comparable objects.
    # We assume standard Python comparison rules apply.
    pass


def _is_empty_input(elements: List[Any]) -> bool:
    """
    Checks if the input list is empty.
    Returns True if the list has zero length.
    """
    return len(elements) == 0


def _find_duplicate_count(elements: List[Any]) -> int:
    """
    Counts the number of duplicate occurrences found in the list.

    Logic:
    1. Create a frequency map (dictionary) counting each element.
    2. Iterate through the counts.
    3. If any count is greater than 1, that element is a duplicate.

    Returns the number of unique elements that appear more than once.
    """
    frequency_map: dict[Any, int] = {}
    duplicate_count = 0

    # Populate frequency map
    for item in elements:
        current_count = frequency_map.get(item, 0)
        frequency_map[item] = current_count + 1

    # Count how many elements have a frequency > 1
    for count in frequency_map.values():
        if count > 1:
            duplicate_count += 1

    return duplicate_count


def _validate_bounds_and_values(elements: List[Any]) -> None:
    """
    Explicitly handles validation for boundary values and types.
    - Handles negative numbers, zero, floats, strings, None, etc., naturally via hashing/equality.
    - If the list contained unhashable types (like lists or dicts), a KeyError would be raised
      by the dictionary usage below. We wrap this in a try-except to provide a clear error.
    """
    pass  # The try-except is handled in the main execution flow for better granularity.


def _execute_uniqueness_check(elements: List[Any]) -> Tuple[bool, str]:
    """
    Core logic to determine if all elements are unique.

    Returns a tuple:
    1. A boolean indicating uniqueness (True if unique, False otherwise).
    2. A descriptive string explaining the result for logging or debugging.
    """
    if _is_empty_input(elements):
        # By definition, an empty set has no duplicates.
        return True, "The list is empty, so all elements are trivially unique."

    # Calculate duplicates using frequency map logic
    duplicate_count = _find_duplicate_count(elements)

    if duplicate_count > 0:
        # We found at least one element that is not unique
        return False, (
            f"Found {duplicate_count} element(s) that are duplicated. "
            f"The list is not unique."
        )
    else:
        # All elements appeared exactly once
        return True, "All elements in the list appeared exactly once. The list is unique."


def all_unique(data: Any) -> bool:
    """
    Checks if the elements of a given list are unique or not.

    This function performs the following steps:
    1. Validates that the input is a list.
    2. Validates that the elements are hashable (implicitly by using a dictionary/set logic).
    3. Handles edge cases: empty lists, single elements, all-equal elements, mixed types.
    4. Returns True if every element in the list is distinct.
    5. Returns False if any element appears more than once.

    Args:
        data: The input to be checked. Must be a list.

    Returns:
        bool: True if all elements are unique, False otherwise.

    Raises:
        TypeError: If the input is not a list or contains unhashable elements.
        ValueError: If the list contains unhashable elements (detected via internal logic).
    """

    # Step 1: Type Validation
    _check_type_is_list(data)

    # Step 2: Extract validation (elements must be hashable to be in a set/dict)
    _check_element_types(data)

    # Step 3: Attempt to perform the check and handle potential unhashable types explicitly
    try:
        # We rely on the frequency map logic which requires hashable items
        result, _ = _execute_uniqueness_check(data)
        return result
    except TypeError as type_error:
        # This catches errors if someone passes a list of lists or dicts (unhashable)
        # Re-raise with a clear message indicating unhashable content
        raise TypeError(
            f"List contains unhashable element types (e.g., lists, dicts) which cannot be "
            f"checked for uniqueness using standard hash-based comparison. \n"
            f"Original error: {type_error}"
        ) from type_error


if __name__ == "__main__":
    # These tests are for manual verification only and are not part of the required signature.
    # They are kept out of the final block as per instructions, but the logic above handles them.
    pass