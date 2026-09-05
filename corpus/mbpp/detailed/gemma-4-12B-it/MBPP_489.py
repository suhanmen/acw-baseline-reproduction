from typing import List, Union

def frequency_Of_Largest(n: int, arr: List[Union[int, float]]) -> int:
    """
    Finds the frequency of the largest value in a given array.

    Args:
        n (int): The expected number of elements in the array.
        arr (List[Union[int, float]]): The list of numbers to process.

    Returns:
        int: The count of occurrences of the maximum value.

    Raises:
        ValueError: If the array is empty or does not match the provided size n.
        TypeError: If inputs are of incorrect types.
    """
    # --- Input Validation ---

    # Check if arr is actually a list
    if not isinstance(arr, list):
        raise TypeError(f"Expected a list for 'arr', but got {type(arr).__name__}")

    # Check if n is an integer
    if not isinstance(n, int):
        raise TypeError(f"Expected an integer for 'n', but got {type(n).__name__}")

    # Check if the length of the list matches the provided n
    actual_length = len(arr)
    if actual_length != n:
        raise ValueError(
            f"Input list length ({actual_length}) does not match "
            f"provided size n ({n})."
        )

    # Handle the empty list case explicitly
    if n == 0:
        return 0

    # --- Logic ---

    # Step 1: Find the maximum value in the array.
    # We use a standard approach to ensure visibility of the logic.
    # We initialize max_val with the first element.
    current_max_value = arr[0]

    # Iterate through the array to find the actual maximum
    for i in range(1, actual_length):
        current_element = arr[i]
        if current_element > current_max_value:
            current_max_value = current_element

    # Step 2: Count how many times this maximum value appears.
    frequency_count = 0
    for item in arr:
        if item == current_max_value:
            frequency_count += 1

    return frequency_count

# Verification of requirements through the provided assertions
if __name__ == "__main__":
    # These assertions are provided by the problem statement to verify correctness.
    assert frequency_Of_Largest(5, [1, 2, 3, 4, 4]) == 2
    assert frequency_Of_Largest(3, [5, 6, 5]) == 1
    assert frequency_Of_Largest(4, [2, 7, 7, 7]) == 3