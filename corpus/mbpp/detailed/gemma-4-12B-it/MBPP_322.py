from typing import List

def position_min(numbers: List[int]) -> List[int]:
    """
    Finds all index positions of the minimum values in a given list of integers.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of indices where the minimum value occurs, sorted ascending.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input list is empty.
    """
    # --- Input Validation ---

    # Check if input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, received {type(numbers).__name__}")

    # Check for empty list
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty.")

    # Check if all elements are integers
    for item in numbers:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers, found {type(item).__name__}")

    # --- Logic ---

    # Step 1: Identify the minimum value in the list
    # We use the built-in min() which is efficient.
    min_value = min(numbers)

    # Step 2: Collect all indices where the value matches the minimum
    indices: List[int] = []

    for current_index in range(len(numbers)):
        current_value = numbers[current_index]

        # Compare current value to the identified minimum
        if current_value == min_value:
            indices.append(current_index)

    # Step 3: Return the collected indices
    # Since we iterated from 0 to len-1, indices are already sorted.
    return indices

# Verification of provided assertions
if __name__ == "__main__":
    # Test Case 1
    test1 = [12,33,23,10,67,89,45,667,23,12,11,10,54]
    assert position_min(test1) == [3, 11]

    # Test Case 2
    test2 = [1,2,2,2,4,4,4,5,5,5,5]
    assert position_min(test2) == [0]

    # Test Case 3
    test3 = [2,1,5,6,8,3,4,9,10,11,8,12]
    assert position_min(test3) == [1]