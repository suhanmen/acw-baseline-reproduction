from collections import Counter
from typing import List, Optional, Any

def _validate_input(values: List[Any], k: int) -> None:
    """
    Validates the input arguments.

    Raises:
        TypeError: If values is not a list or k is not an integer.
        ValueError: If k is less than or equal to zero, or if the required occurrence
                    of an element exceeds the length of the list.
    """
    if not isinstance(values, list):
        raise TypeError(f"Expected 'values' to be a list, got {type(values).__name__}")

    if not isinstance(k, int):
        raise TypeError(f"Expected 'k' to be an integer, got {type(k).__name__}")

    if k <= 0:
        raise ValueError(f"Expected 'k' to be a positive integer (> 0), got {k}")

    if len(values) < k:
        raise ValueError(
            f"List contains {len(values)} elements, but 'k' is {k}. "
            "An element cannot occur k times if the list is shorter than k."
        )

def _count_occurrences(values: List[Any]) -> dict:
    """
    Counts the number of occurrences for each element in the list.

    Returns:
        A dictionary mapping each unique element to its count.
    """
    counts = {}
    for element in values:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts

def _find_first_k_element(values: List[Any], k: int) -> Any:
    """
    Finds the first element in the list that occurs exactly k times.

    Args:
        values: The list of elements to search.
        k: The target number of occurrences.

    Returns:
        The first element that appears k times in the list.

    Raises:
        ValueError: If no element in the list occurs exactly k times.
    """
    # Calculate counts first
    counts = _count_occurrences(values)

    # Iterate through the list again to find the first element with the target count
    for element in values:
        if counts[element] == k:
            return element

    # If we reach here, no element occurred k times
    raise ValueError(f"No element in the list occurs exactly {k} times.")

def first_Element(values: List[Any], k: int, _validate_flag: bool = True) -> Any:
    """
    Finds the first element occurring k times in a given array.

    This function adheres to strict validation and defensive programming practices.
    It explicitly handles edge cases such as empty input, single elements,
    all-equal elements, and boundary values for k.

    Args:
        values: A list of elements (any type) to search within.
        k: A positive integer representing the required number of occurrences.
        _validate_flag: Internal flag to allow skipping validation for specific internal calls 
                        (default is True for production safety).

    Returns:
        The first element found that occurs exactly k times.

    Raises:
        TypeError: If input types are incorrect.
        ValueError: If k is invalid or no element meets the criteria.
    """
    if _validate_flag:
        _validate_input(values, k)

    # Helper function call to find the result
    return _find_first_k_element(values, k)