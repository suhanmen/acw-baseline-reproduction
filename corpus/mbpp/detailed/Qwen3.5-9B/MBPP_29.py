from collections import Counter
from typing import Any, List, Optional

def _validate_list(data: Any) -> List:
    """
    Validate that the input is a list.
    Raises a TypeError if the input is not a list.
    """
    if not isinstance(data, list):
        raise TypeError(f"Expected a list, but received {type(data).__name__}")
    return data

def _validate_count(expected_count: Any) -> int:
    """
    Validate that the second argument is an integer representing the expected length.
    Raises a TypeError if it is not an integer, or a ValueError if it is negative.
    """
    if not isinstance(expected_count, int):
        raise TypeError(f"Expected an integer for count, but received {type(expected_count).__name__}")
    if expected_count < 0:
        raise ValueError(f"Count must be non-negative, but received {expected_count}")
    return expected_count

def _check_actual_length(data: List, expected_length: int) -> None:
    """
    Validate that the actual length of the list matches the expected length.
    Raises a ValueError if they do not match.
    """
    actual_length = len(data)
    if actual_length != expected_length:
        raise ValueError(
            f"List length mismatch: expected {expected_length}, but got {actual_length}"
        )

def _get_element_counts(data: List) -> dict:
    """
    Count the occurrences of each element in the list.
    Returns a dictionary where keys are elements and values are their counts.
    """
    counter = Counter(data)
    return dict(counter)

def _find_odd_occurrence_occurrences(counts: dict) -> Optional[int]:
    """
    Iterate through the counts to find elements with an odd occurrence count.
    Returns a list of such elements.
    Based on the problem context, we expect exactly one such element.
    """
    odd_occurrence_elements = []
    for element, count in counts.items():
        if count % 2 != 0:
            odd_occurrence_elements.append(element)
    return odd_occurrence_elements

def get_Odd_Occurrence(data: Any, count: Any) -> Any:
    """
    Find the element occurring an odd number of times in the list.

    The function strictly validates:
    1. Input is a list.
    2. The provided 'count' is a non-negative integer.
    3. The actual length of the list matches the provided 'count'.

    It assumes that under these conditions, exactly one element occurs an odd number of times.
    If no such element exists or multiple exist, it raises a ValueError describing the anomaly.

    Parameters:
        data (Any): The input data, expected to be a list of hashable elements.
        count (Any): The expected number of elements in the list (must be non-negative int).

    Returns:
        Any: The element that occurs an odd number of times.

    Raises:
        TypeError: If data is not a list or count is not an integer.
        ValueError: If count is negative or if the list length does not match count.
    """
    # Step 1: Validate the list structure
    validated_list = _validate_list(data)

    # Step 2: Validate the count parameter
    validated_count = _validate_count(count)

    # Step 3: Verify the list length matches the expected count
    _check_actual_length(validated_list, validated_count)

    # Step 4: Count occurrences of each element
    element_counts = _get_element_counts(validated_list)

    # Step 5: Identify elements with odd occurrence counts
    odd_occurrence_list = _find_odd_occurrence_occurrences(element_counts)

    # Step 6: Handle the result based on the problem constraints (exactly one odd occurrence)
    if len(odd_occurrence_list) == 0:
        # This case implies an error in the problem assumption (no odd occurrences)
        raise ValueError(
            f"No element found with an odd occurrence in the list of length {validated_count}."
            " This usually implies all elements appear an even number of times."
        )
    elif len(odd_occurrence_list) > 1:
        # This case implies multiple elements have odd occurrences, violating the unique solution premise
        raise ValueError(
            f"Multiple elements ({len(odd_occurrence_list)}) found with odd occurrences: {odd_occurrence_list}."
            " The problem expects a unique solution."
        )
    else:
        # Exactly one element found, which is the expected behavior
        return odd_occurrence_list[0]