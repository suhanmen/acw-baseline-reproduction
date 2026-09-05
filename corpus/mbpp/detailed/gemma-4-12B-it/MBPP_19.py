from typing import List

def test_duplicate(numbers: List[int]) -> bool:
    """
    Determines whether a given array of integers contains any duplicate element.

    Args:
        numbers (List[int]): A list of integers to be checked.

    Returns:
        bool: True if any value appears more than once, False otherwise.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate that the input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}")

    # Handle the edge case of an empty list immediately
    if len(numbers) == 0:
        return False

    # Validate that all elements in the list are integers
    for index, element in enumerate(numbers):
        if not isinstance(element, int):
            raise TypeError(
                f"Element at index {index} is {type(element).__name__}, "
                "but only integers are allowed."
            )

    # Use a set to keep track of unique elements encountered so far.
    # A set provides O(1) average time complexity for lookups and insertions.
    seen_elements = set()

    for current_number in numbers:
        # Check if the current number has already been added to the set
        is_already_seen = current_number in seen_elements

        if is_already_seen:
            # A duplicate has been found, return True immediately
            return True

        # If not seen, add it to the set and continue to the next element
        seen_elements.add(current_number)

    # If the loop completes without finding any duplicates, return False
    return False

# Assertions to verify correctness
if __name__ == "__main__":
    assert test_duplicate([1, 2, 3, 4, 5]) == False
    assert test_duplicate([1, 2, 3, 4, 4]) == True
    assert test_duplicate([1, 1, 2, 2, 3, 3, 4, 4, 5]) == True

    # Additional edge cases
    assert test_duplicate([]) == False                # Empty list
    assert test_duplicate([1]) == False               # Single element
    assert test_duplicate([0, 0]) == True             # Zeros
    assert test_duplicate([-1, -1]) == True           # Negatives
    assert test_duplicate([10, 20, 30, 10]) == True   # Duplicate at ends