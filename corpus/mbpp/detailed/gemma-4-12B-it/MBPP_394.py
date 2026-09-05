from typing import Tuple, Any


def check_distinct(input_tuple: Tuple[Any, ...]) -> bool:
    """
    Determines whether all elements within a given tuple are unique.

    Args:
        input_tuple (Tuple[Any, ...]): A tuple containing elements to be checked.

    Returns:
        bool: True if all elements in the tuple are distinct, False otherwise.

    Raises:
        TypeError: If the input provided is not a tuple.
    """
    # Validate input type
    if not isinstance(input_tuple, tuple):
        raise TypeError(f"Input must be a tuple, but received {type(input_tuple).__name__}")

    # Handle edge case: Empty tuple
    # An empty set of elements is vacuously distinct (no duplicates exist).
    if len(input_tuple) == 0:
        return True

    # Handle edge case: Single element
    # A single element cannot have a duplicate.
    if len(input_tuple) == 1:
        return True

    # Logic for checking distinctness:
    # We use a set to track elements we have already encountered.
    # Sets only store unique values, providing O(1) average time complexity for lookups.
    seen_elements = set()

    # Iterate through each element in the tuple one by one.
    for index, current_element in enumerate(input_tuple):
        # Defensive check: Elements must be hashable to be placed in a set.
        # This handles cases where the tuple might contain lists or dictionaries.
        if not hasattr(current_element, "__hash__") or isinstance(current_element, (list, dict, set)):
            # If the element is unhashable, we fallback to a nested loop comparison
            # to ensure the function remains robust, though this is O(n^2).
            is_duplicate = False
            for i in range(index):
                if input_tuple[i] == current_element:
                    is_duplicate = True
                    break

            if is_duplicate:
                return False
            continue

        # Check if the current element has been seen before in the iteration.
        if current_element in seen_elements:
            # If it exists in the set, it is a duplicate.
            return False

        # If it's a new element, add it to the set of seen elements.
        seen_elements.add(current_element)

    # If the loop completes without finding any duplicates, all elements are distinct.
    return True


if __name__ == "__main__":
    # Test cases provided in the requirements
    assert check_distinct((1, 4, 5, 6, 1, 4)) == False
    assert check_distinct((1, 4, 5, 6)) == True
    assert check_distinct((2, 3, 4, 5, 6)) == True

    # Additional edge cases
    assert check_distinct(()) == True
    assert check_distinct((1,)) == True
    assert check_distinct((1, 1, 1)) == False
    assert check_distinct((0, -1, 1.5, "string", "string")) == False