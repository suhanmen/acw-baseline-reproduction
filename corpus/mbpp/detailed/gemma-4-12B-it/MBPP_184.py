from typing import List, Union

def greater_specificnum(numbers: List[Union[int, float]], threshold: Union[int, float]) -> bool:
    """
    Determines if there is at least one value in a list of numbers that is 
    strictly greater than a specified threshold.

    Args:
        numbers: A list of integers or floats.
        threshold: The numerical value to compare against.

    Returns:
        bool: True if any number in the list is greater than the threshold,
              False otherwise.

    Raises:
        TypeError: If the input 'numbers' is not a list or 'threshold' is not a number.
        ValueError: If the 'numbers' list contains non-numeric types.
    """
    # --- Input Validation ---

    # Check if 'numbers' is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Expected 'numbers' to be a list, but received {type(numbers).__name__}")

    # Check if 'threshold' is an integer or float
    if not isinstance(threshold, (int, float)):
        raise TypeError(f"Expected 'threshold' to be an int or float, but received {type(threshold).__name__}")

    # --- Edge Case Handling ---

    # If the list is empty, no value can be greater than the threshold
    if len(numbers) == 0:
        return False

    # --- Logic Implementation ---

    # We want to find if ANY element satisfies the condition.
    # We will iterate through the list and check each value.
    found_greater = False

    for index, current_value in enumerate(numbers):
        # Validate that each element in the list is a number
        if not isinstance(current_value, (int, float)):
            raise ValueError(
                f"Element at index {index} is of type {type(current_value).__name__}, "
                "but only int or float are allowed."
            )

        # Check the condition
        is_current_greater = current_value > threshold

        if is_current_greater:
            # We found at least one, so we can stop early and return True
            found_greater = True
            break

    return found_greater

# The assertions provided in the problem description
if __name__ == "__main__":
    # Test Case 1: At least one value is greater
    assert greater_specificnum([220, 330, 500], 200) == True

    # Test Case 2: No values are greater
    assert greater_specificnum([12, 17, 21], 20) == False

    # Test Case 3: All values are smaller than the threshold
    assert greater_specificnum([1, 2, 3, 4], 10) == False

    # Additional edge cases for robustness
    assert greater_specificnum([], 10) == False          # Empty list
    assert greater_specificnum([5], 5) == False            # Equal value (not strictly greater)
    assert greater_specificnum([10], 5) == True             # Single element greater
    assert greater_specificnum([-10, -5, 0], -1) == False  # Negative numbers