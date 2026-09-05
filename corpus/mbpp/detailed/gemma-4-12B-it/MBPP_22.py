from typing import List, Union

def find_first_duplicate(numbers: List[int]) -> int:
    """
    Identifies the first element in a list that appears more than once.

    The 'first' duplicate is defined as the element whose second occurrence 
    appears earliest in the list.

    Args:
        numbers (List[int]): A list of integers to search.

    Returns:
        int: The first duplicate integer found, or -1 if all elements are unique.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input Validation: Ensure the input is a list.
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, got {type(numbers).__name__}")

    # Input Validation: Ensure all elements in the list are integers.
    for item in numbers:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers, found {type(item).__name__}")

    # Handle edge cases: empty list or single element list.
    # Neither can contain a duplicate.
    if len(numbers) < 2:
        return -1

    # We use a set to track the unique integers we have encountered so far.
    # Sets provide O(1) average time complexity for lookups and insertions.
    seen_elements = set()

    # Iterate through the list sequentially to preserve the order of occurrence.
    for current_number in numbers:
        # Check if the current number has been encountered before.
        if is_already_seen(current_number, seen_elements):
            # This is the first time we are encountering a repeated number.
            # Since we are iterating from left to right, the first time we 
            # find a number already in the set, it is the 'first' duplicate.
            return current_number

        # If not seen, add it to our collection of seen numbers.
        seen_elements.add(current_number)

    # If the loop completes, no duplicates were detected.
    return -1

def is_already_seen(element: int, seen_collection: set) -> bool:
    """
    Helper function to check if an element exists in a set.
    Explicitly separated for clarity and naming.
    """
    # Using 'in' on a set is highly efficient.
    exists = element in seen_collection
    return exists

if __name__ == "__main__":
    # The following assertions verify the requirements.
    assert find_first_duplicate([1, 2, 3, 4, 4, 5]) == 4
    assert find_first_duplicate([1, 2, 3, 4]) == -1
    assert find_first_duplicate([1, 1, 2, 3, 3, 2, 2]) == 1

    # Additional edge cases for robustness
    assert find_first_duplicate([]) == -1
    assert find_first_duplicate([10]) == -1
    assert find_first_duplicate([5, 5]) == 5
    assert find_first_duplicate([-1, -1, 0]) == -1 # Wait, -1 is a duplicate
    # Correcting mental check: [-1, -1, 0] should return -1
    assert find_first_duplicate([-1, -1, 0]) == -1 # Wait, I misread my own logic. 
    # Correction: [-1, -1, 0] should return -1? No, -1 is the duplicate.
    # Let's re-verify:
    assert find_first_duplicate([-1, -1, 0]) == -1 # Incorrect, it should be -1. 
    # Wait, the logic returns the number itself.
    # Let's re-trace: numbers = [-1, -1, 0]. 
    # Loop 1: current = -1. Not in set. Add to set.
    # Loop 2: current = -1. IS in set. Return -1. 
    # This is confusing because the value IS -1. 
    # If the function returns -1 when a duplicate is found and -1 when no duplicate 
    # is found, there is an ambiguity. 
    # However, the problem description says return -1 if NO duplicate is found.
    # If the duplicate IS -1, the code returns -1, which is indistinguishable from 'no duplicate'.
    # This is a limitation of the problem's return value specification (returning -1).
    # Given the assertions, it is expected to return the integer.