from typing import Any, List, Tuple


def _validate_input_list(value: Any, name: str) -> List[Any]:
    """
    Validates that the given value is a list.

    If the input is not a list, raises a TypeError with a descriptive message.
    This ensures type safety before further processing.

    Args:
        value: The value to validate.
        name: The name of the variable for error messages.

    Returns:
        The validated list.

    Raises:
        TypeError: If value is not a list.
    """
    if not isinstance(value, list):
        raise TypeError(f"{name} must be a list, got {type(value).__name__}")
    return value


def _is_numeric(value: Any) -> bool:
    """
    Determines if a value is numeric (int or float).

    This helper ensures we only process numeric types to prevent
    unexpected behavior with mixed-type lists.

    Args:
        value: The value to check.

    Returns:
        True if the value is an int or float, False otherwise.
    """
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _extract_unique_elements(items: List[Any]) -> List[Any]:
    """
    Extracts unique elements from a list while preserving order for hashing.

    Since sets do not preserve order and we need deterministic results,
    this function removes duplicates by tracking seen items.
    This is a preparatory step to ensure we only consider unique elements
    before finding the intersection.

    Args:
        items: The list of items to deduplicate.

    Returns:
        A new list containing only the unique elements from the input list.
    """
    unique_elements = []
    seen_set = set()

    for item in items:
        # We accept non-numeric types if they are hashable, 
        # but we flag them for potential warning if strict numeric validation is needed later.
        # For this problem, we proceed with any hashable type.
        # Note: Lists themselves are not hashable, so passing a list here would raise TypeError naturally.

        # Attempt to add to set to check for existence and uniqueness
        try:
            is_present = item in seen_set
        except TypeError:
            # If item is unhashable (like a list or dict), it cannot be in a set.
            # We treat it as unique by default but we cannot easily find intersections
            # involving unhashable types using set operations.
            # Given the problem context of numbers in examples, we will raise an error
            # if we encounter unhashable types to maintain robustness.
            raise TypeError(f"List contains unhashable type '{type(item).__name__}'. "
                           "All elements must be hashable to find common elements.") from None

        if not is_present:
            unique_elements.append(item)
            seen_set.add(item)

    return unique_elements


def _find_intersection(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Finds the intersection of two lists of unique elements.

    Args:
        list1: First list of unique elements.
        list2: Second list of unique elements.

    Returns:
        A list of common elements.
    """
    # Convert the second list to a set for O(1) average time complexity lookups
    set2 = set(list2)

    intersection = []

    # Iterate through the first list and check existence in the second set
    for item in list1:
        if item in set2:
            intersection.append(item)

    return intersection


def common(l1: list, l2: list) -> List[Any]:
    """Return sorted unique common elements for two lists.

    This function finds the common elements between two input lists, ensures they are unique,
    sorts them in ascending order, and returns the result.

    Args:
        l1: The first list of elements. Must be a list of hashable elements.
        l2: The second list of elements. Must be a list of hashable elements.

    Returns:
        A sorted list of unique elements that appear in both l1 and l2.

    Raises:
        TypeError: If either input is not a list or if the list contains unhashable types.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
        >>> common([], [1, 2, 3])
        []
        >>> common([1, 1, 1], [1, 1, 1])
        [1]
        >>> common([-1, -2, 3], [-2, -3, 10])
        [-2]
    """
    # Step 1: Validate inputs
    validated_l1 = _validate_input_list(l1, "l1")
    validated_l2 = _validate_input_list(l2, "l2")

    # Step 2: Check for unhashable types which would break set operations
    # Although Python handles some cases gracefully, explicit checking is more defensive.
    for idx, item in enumerate(validated_l1):
        try:
            hash(item)
        except TypeError:
            raise TypeError(f"l1 contains unhashable element at index {idx}: {item}")

    for idx, item in enumerate(validated_l2):
        try:
            hash(item)
        except TypeError:
            raise TypeError(f"l2 contains unhashable element at index {idx}: {item}")

    # Step 3: Handle edge case where either list is empty
    # If either list is empty, the intersection must be empty.
    if not validated_l1 or not validated_l2:
        return []

    # Step 4: Deduplicate elements in both lists
    unique_l1 = _extract_unique_elements(validated_l1)
    unique_l2 = _extract_unique_elements(validated_l2)

    # Step 5: Find the intersection
    common_elements = _find_intersection(unique_l1, unique_l2)

    # Step 6: Sort the result
    # Python's default sort works for mixed numeric types and handles integers/floats correctly.
    sorted_common_elements = sorted(common_elements)

    return sorted_common_elements