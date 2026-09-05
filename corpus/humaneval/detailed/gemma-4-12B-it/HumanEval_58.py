from typing import List, Any


def common(l1: List[Any], l2: List[Any]) -> List[Any]:
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # Validate that inputs are actually lists
    if not isinstance(l1, list) or not isinstance(l2, list):
        raise TypeError("Both arguments must be of type 'list'.")

    # Handle cases where lists are empty
    if not l1 or not l2:
        return []

    # Convert both lists to sets to eliminate duplicates within each list
    # and provide O(1) average time complexity for lookup operations.
    set1 = set(l1)
    set2 = set(l2)

    # Use set intersection to find elements present in both sets.
    # This ensures that we only consider elements that appear in both inputs.
    common_elements_set = set1.intersection(set2)

    # Convert the resulting set back into a list.
    common_elements_list = list(common_elements_set)

    # The problem specifies returning a "sorted" list.
    # We use sorted() which returns a new list in ascending order.
    # Note: This assumes elements are comparable (e.g., all integers or all strings).
    try:
        sorted_common_elements = sorted(common_elements_list)
    except TypeError as e:
        # This catches cases where the list contains incomparable types (e.g., [1, "a"])
        raise TypeError("Lists must contain comparable types to be sorted.") from e

    return sorted_common_elements