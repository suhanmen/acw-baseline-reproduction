from collections import Counter
from typing import Any, List, Tuple, Union

def _validate_input(data: Any) -> None:
    """
    Validates that the input is a list and contains only hashable elements.

    Args:
        data: The input to validate.

    Raises:
        TypeError: If the input is not a list or contains unhashable elements.
    """
    if not isinstance(data, list):
        raise TypeError(
            f"Input must be a list, but got {type(data).__name__} instead."
        )

    for index, element in enumerate(data):
        try:
            hash(element)
        except TypeError:
            raise TypeError(
                f"Element at index {index} ({element!r}) is unhashable and cannot be counted."
            )

def _count_occurrences(data: List[Any]) -> List[Tuple[Any, int]]:
    """
    Counts the occurrences of each unique element in the list.

    Args:
        data: The list of elements to count.

    Returns:
        A list of tuples (element, count) sorted by count in descending order,
        then by element value in ascending order for ties.
    """
    # Use Counter for efficient counting
    counts = Counter(data)

    # Convert to a sorted list: primary key is count (descending), 
    # secondary key is element value (ascending) to ensure deterministic output for ties
    sorted_items = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return sorted_items

def max_occurrences(data: List[Any]) -> Union[Any, List[Any]]:
    """
    Finds the item(s) with maximum occurrences in a given list.

    If there is a tie for the maximum occurrence, all tied items are returned 
    in ascending sorted order.

    Args:
        data: A list of hashable elements.

    Returns:
        The single item with the maximum occurrence if it's unique,
        or a list of items tied for the maximum occurrence, sorted ascending.

    Raises:
        TypeError: If input is not a list or contains unhashable elements.
        ValueError: If the input list is empty.
    """
    # Handle the empty list edge case explicitly
    if len(data) == 0:
        raise ValueError("Input list cannot be empty.")

    # Validate the input structure and content
    _validate_input(data)

    # Get all unique items with their counts, sorted by count (desc) then item (asc)
    sorted_items = _count_occurrences(data)

    # Extract the count of the first item (which has the highest count)
    max_count = sorted_items[0][1]

    # Extract all items that have the maximum count
    max_items = [item[0] for item in sorted_items if item[1] == max_count]

    # Return a single item if there is only one, otherwise return the list
    if len(max_items) == 1:
        return max_items[0]
    else:
        # They are already sorted ascending due to the sorting in _count_occurrences
        return max_items