def _validate_numeric_sequence(sequence) -> None:
    """
    Validates that the input is a list and contains only numeric elements (int or float).
    Raises a ValueError if validation fails.
    """
    if not isinstance(sequence, list):
        raise ValueError(
            f"Input must be a list of numbers, but got a {type(sequence).__name__} instead."
        )

    if len(sequence) == 0:
        raise ValueError("Input list must not be empty.")

    for index, element in enumerate(sequence):
        if not isinstance(element, (int, float)):
            raise ValueError(
                f"Element at index {index} is not a number. "
                f"Expected int or float, got {type(element).__name__}."
            )


def _is_distinct_from_front(num_to_check: float, already_seen: set) -> bool:
    """
    Helper function to check if a single number exists in the set of already seen numbers.
    Returns True if the number is found (i.e., it is NOT distinct), False otherwise.
    """
    return num_to_check in already_seen


def _build_seen_set(sequence: list) -> set:
    """
    Iterates through the sequence and builds a set of encountered numbers.
    Returns an empty set if the input sequence is empty (though validation prevents this).
    """
    seen_elements = set()
    for number in sequence:
        seen_elements.add(number)
    return seen_elements


def test_distinct(sequence) -> bool:
    """
    Determines whether all numbers in the provided sequence are distinct (different from each other).

    Parameters:
        sequence (list): A list of numeric values (int or float).

    Returns:
        bool: True if all numbers in the list are unique, False otherwise.

    Raises:
        ValueError: If the input is not a list, is empty, or contains non-numeric elements.
    """
    # Step 1: Validate the input structure and contents explicitly.
    _validate_numeric_sequence(sequence)

    # Step 2: Determine if the set of elements has the same length as the list.
    # If the set length is less than the list length, duplicates exist.
    # This approach is O(n) and O(n) space.
    unique_elements = _build_seen_set(sequence)
    total_elements_count = len(sequence)
    distinct_elements_count = len(unique_elements)

    # Step 3: Compare the counts to determine the result.
    are_all_different = distinct_elements_count == total_elements_count

    return are_all_different