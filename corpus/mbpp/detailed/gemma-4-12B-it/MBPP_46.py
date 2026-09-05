from typing import List, Any

def test_distinct(numbers: List[Any]) -> bool:
    """
    Determines whether all elements in a list are unique.

    Args:
        numbers (List[Any]): A list of elements to check for uniqueness.

    Returns:
        bool: True if all elements are different, False otherwise.

    Raises:
        TypeError: If the input is not a list.
    """
    # Step 1: Validate the input type explicitly.
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list, but received {type(numbers).__name__}")

    # Step 2: Handle the edge case of an empty list.
    # An empty list technically contains no duplicates, so it should return True.
    if len(numbers) == 0:
        return True

    # Step 3: Handle the case of a single element.
    # A single element cannot have duplicates.
    if len(numbers) == 1:
        return True

    # Step 4: Track seen elements to detect duplicates.
    # We use a set because it provides O(1) average time complexity for lookups.
    seen_elements = set()

    # Step 5: Iterate through the list and check for uniqueness.
    for index, current_item in enumerate(numbers):
        # We check if the item is already in our set of seen elements.
        is_duplicate = current_item in seen_elements

        if is_duplicate:
            # A duplicate was found; return False immediately (short-circuit).
            return False

        # Add the current item to the set of seen elements.
        seen_elements.add(current_item)

    # Step 6: If the loop finishes without finding any duplicates, return True.
    return True

# The problem requirements specify the following assertions:
if __name__ == "__main__":
    # Assertion 1: Distinct elements
    assert test_distinct([1, 5, 7, 9]) == True

    # Assertion 2: Contains duplicates (5)
    assert test_distinct([2, 4, 5, 5, 7, 9]) == False

    # Assertion 3: Distinct consecutive elements
    assert test_distinct([1, 2, 3]) == True