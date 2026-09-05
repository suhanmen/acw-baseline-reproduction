from typing import List, Any


def all_unique(input_list: List[Any]) -> bool:
    """
    Determines whether all elements in a given list are unique.

    A list is considered to have unique elements if no element appears 
    more than once. Empty lists or lists with a single element are 
    considered to have unique elements by definition.

    Args:
        input_list (List[Any]): A list containing elements of any hashable type.

    Returns:
        bool: True if all elements are unique, False otherwise.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains unhashable types (like nested lists).
    """
    # Validate that the input is actually a list
    if not isinstance(input_list, list):
        raise TypeError(f"Expected input type 'list', but received '{type(input_list).__name__}'")

    # Edge case: An empty list contains no duplicates
    if len(input_list) == 0:
        return True

    # Edge case: A single element list contains no duplicates
    if len(input_list) == 1:
        return True

    # Use a set to keep track of elements we have already encountered.
    # Sets provide O(1) average time complexity for lookups and insertions.
    seen_elements = set()

    for index, current_element in enumerate(input_list):
        # Defensive check: ensure the element is hashable so it can be placed in a set.
        # This prevents the code from crashing with a TypeError when encountering a list/dict inside.
        try:
            _check_hashability(current_element)
        except TypeError:
            raise ValueError(
                f"List contains an unhashable element at index {index}: {current_element}. "
                "All elements must be of a hashable type (e.g., int, str, tuple)."
            )

        # Check if we have seen this element before
        is_duplicate = current_element in seen_elements

        if is_duplicate:
            # We found a duplicate, return False immediately (short-circuit)
            return False

        # If it's not a duplicate, add it to our collection of seen items
        seen_elements.add(current_element)

    # If the loop finishes without finding any duplicates, return True
    return True


def _check_hashability(item: Any) -> None:
    """
    Helper function to verify if an item can be hashed.
    If it cannot be hashed, it raises a TypeError.
    """
    try:
        hash(item)
    except TypeError:
        raise TypeError(f"Item {item} of type {type(item).__name__} is not hashable.")


if __name__ == "__main__":
    # The following assertions verify the requirements provided in the prompt.
    assert all_unique([1, 2, 3]) == True
    assert all_unique([1, 2, 1, 2]) == False
    assert all_unique([1, 2, 3, 4, 5]) == True