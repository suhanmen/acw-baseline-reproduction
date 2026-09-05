from typing import List, Any

def _validate_input_is_list(input_data: Any) -> None:
    """
    Verifies that the provided input is a list.
    Raises a TypeError if the input is not a list.
    """
    if not isinstance(input_data, list):
        raise TypeError(f"Input must be of type 'list', but received {type(input_data).__name__}")

def _validate_elements_are_comparable(input_list: List[Any]) -> None:
    """
    Ensures that all elements in the list can be compared with each other
    to allow for sorting. This checks for mixed types that might fail.
    """
    if not input_list:
        return

    first_element = input_list[0]
    for item in input_list[1:]:
        # This is a basic check; in production, we'd handle specific 
        # exceptions during the sort phase, but here we do a sanity check.
        try:
            _ = first_element < item
            _ = item < first_element
        except TypeError:
            raise TypeError(
                f"List contains incomparable types: {type(first_element).__name__} "
                f"and {type(item).__name__}. All elements must be comparable."
            )

def unique(l: list) -> list:
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Step 1: Validate that the input is a list
    _validate_input_is_list(l)

    # Handle edge case: empty list
    if not l:
        return []

    # Step 2: Validate that elements are comparable (required for sorting)
    _validate_elements_are_comparable(l)

    # Step 3: Extract unique elements
    # We use a set to automatically handle duplicates.
    # Note: Elements must be hashable to be put into a set.
    unique_elements_set = set()
    for element in l:
        try:
            unique_elements_set.add(element)
        except TypeError as exc:
            # This handles cases where elements are unhashable (e.g., lists inside lists)
            # In a production environment, we might want to handle this by 
            # falling back to a different uniqueness check, but for this 
            # specification, we raise the error to be explicit.
            raise TypeError(
                "All elements in the list must be hashable to determine uniqueness."
            ) from exc

    # Step 4: Convert the set back to a list
    unique_elements_list = list(unique_elements_set)

    # Step 5: Sort the unique elements
    # Using a standard sort (Timsort) which is stable and efficient.
    unique_elements_list.sort()

    # Step 6: Return the final result
    return unique_elements_list