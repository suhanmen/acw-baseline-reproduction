from typing import List

def check_Consecutive(numbers: List[int]) -> bool:
    """
    Determines if a given list of integers consists of strictly consecutive numbers.
    Consecutive numbers are defined as a sequence where each element is exactly
    one greater than the previous element.

    Args:
        numbers (List[int]): A list of integers to check.

    Returns:
        bool: True if the list is consecutive, False otherwise.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Input Validation: Ensure the input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}")

    # Edge Case: An empty list is technically consecutive (vacuously true)
    # or could be considered non-consecutive. Based on standard logic for 
    # sequences, we will treat an empty list or a single element as True.
    if len(numbers) == 0:
        return True

    if len(numbers) == 1:
        return True

    # Input Validation: Ensure all elements are integers
    for item in numbers:
        if not isinstance(item, int):
            raise ValueError(f"All elements in the list must be integers. Found: {type(item).__name__}")

    # Logic:
    # To be consecutive, the difference between any element at index 'i' 
    # and the element at index 'i-1' must be exactly 1.

    # We iterate starting from the second element (index 1)
    for current_index in range(1, len(numbers)):
        previous_value = numbers[current_index - 1]
        current_value = numbers[current_index]

        # Calculate the step difference
        difference = current_value - previous_value

        # If the difference is not exactly 1, the sequence is not consecutive.
        # This handles gaps (e.g., 1, 3), backwards movement (e.g., 2, 1),
        # and duplicates (e.g., 1, 1).
        if difference != 1:
            return False

    # If the loop completes without returning False, the list is consecutive.
    return True

# Standard assertions to verify the logic
if __name__ == "__main__":
    assert check_Consecutive([1, 2, 3, 4, 5]) == True
    assert check_Consecutive([1, 2, 3, 5, 6]) == False
    assert check_Consecutive([1, 2, 1]) == False
    # Additional test cases for robustness
    assert check_Consecutive([10, 11, 12]) == True
    assert check_Consecutive([1]) == True
    assert check_Consecutive([]) == True
    assert check_Consecutive([-3, -2, -1, 0]) == True