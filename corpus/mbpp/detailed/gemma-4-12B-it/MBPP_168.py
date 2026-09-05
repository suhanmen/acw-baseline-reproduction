from typing import List, Any


def frequency(numbers: List[int], target: int) -> int:
    """
    Calculates the frequency of a specific target number within a list of integers.

    Args:
        numbers (List[int]): A list of integers to search through.
        target (int): The integer value to count.

    Returns:
        int: The number of times the target appears in the list.

    Raises:
        TypeError: If inputs are not of the expected types.
    """
    # Validate input types strictly for production reliability
    if not isinstance(numbers, list):
        raise TypeError(f"Expected 'numbers' to be a list, but got {type(numbers).__name__}")

    if not isinstance(target, int):
        raise TypeError(f"Expected 'target' to be an integer, but got {type(target).__name__}")

    # Handle the edge case of an empty list explicitly
    if len(numbers) == 0:
        return 0

    # Initialize the counter
    occurrence_count = 0

    # Iterate through the list to count matches
    # We use a standard for-loop to ensure every step is visible and clear.
    for item in numbers:
        # Validate that every item in the list is an integer
        # This prevents runtime errors during comparison if the list is malformed
        if not isinstance(item, int):
            raise TypeError(f"List contains non-integer element: {item} (type: {type(item).__name__})")

        # Check if the current item matches the target
        if item == target:
            # Increment the counter only on a successful match
            occurrence_count += 1

    return occurrence_count


if __name__ == "__main__":
    # Verification of the provided test cases
    assert frequency([1, 2, 3], 4) == 0
    assert frequency([1, 2, 2, 3, 3, 3, 4], 3) == 3
    assert frequency([0, 1, 2, 3, 1, 2], 1) == 2

    # Additional edge cases for robustness
    assert frequency([], 10) == 0                 # Empty list
    assert frequency([5, 5, 5], 5) == 3           # All elements match
    assert frequency([-1, -1, 2, 0], -1) == 2     # Negative numbers
    assert frequency([0, 0, 0], 0) == 3           # Zeros