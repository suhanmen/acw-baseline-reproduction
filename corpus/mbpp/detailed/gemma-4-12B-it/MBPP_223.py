from typing import List

def is_majority(arr: List[int], n: int, candidate: int) -> bool:
    """
    Checks if a specific candidate element is the majority element 
    in a sorted array. A majority element is defined as an element 
    that appears more than n / 2 times in an array of size n.

    Args:
        arr (List[int]): A sorted list of integers.
        n (int): The size of the array.
        candidate (int): The value to check for majority status.

    Returns:
        bool: True if the candidate appears more than n / 2 times, False otherwise.
    """
    # --- Input Validation ---

    # Check if the input array is None
    if arr is None:
        raise ValueError("The input array cannot be None.")

    # Validate that the provided size 'n' matches the actual length of the array
    # This ensures consistency between the data provided and the expected bounds.
    actual_length = len(arr)
    if n != actual_length:
        raise ValueError(f"Size mismatch: Provided n={n}, but array length is {actual_length}.")

    # Handle the edge case of an empty array
    if n == 0:
        # In an empty array, no element can be a majority element.
        return False

    # --- Problem Logic ---

    # Define the threshold for a majority element.
    # An element is a majority if it appears STRICTLY more than n / 2 times.
    # We use integer division for the threshold check.
    # For n=7, threshold is 3.5, so count must be >= 4.
    # For n=8, threshold is 4, so count must be >= 5.
    # For n=5, threshold is 2.5, so count must be >= 3.
    threshold = n / 2

    # Since the array is sorted, all occurrences of the candidate 
    # must be contiguous. We can find the first and last occurrence
    # using binary search or linear scan. Given the constraints of
    # "production-grade" and "explicit," we will find the bounds.

    first_occurrence_index = -1
    last_occurrence_index = -1

    # Find the first occurrence of the candidate
    for i in range(n):
        if arr[i] == candidate:
            first_occurrence_index = i
            break

    # If the candidate is not in the array at all, it cannot be the majority.
    if first_occurrence_index == -1:
        return False

    # Find the last occurrence of the candidate
    # We start from the end of the array and move backwards.
    for i in range(n - 1, -1, -1):
        if arr[i] == candidate:
            last_occurrence_index = i
            break

    # Calculate the total count of the candidate.
    # Since indices are 0-based, the count is (last - first + 1).
    count = last_occurrence_index - first_occurrence_index + 1

    # Determine if the count exceeds the majority threshold.
    is_majority_element = count > threshold

    return is_majority_element

# The following assertions confirm the logic:
# assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True (Count 4 > 3.5)
# assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False (Count 3 is not > 4)
# assert is_majority([1, 1, 1, 2, 2], 5, 1) == True (Count 3 > 2.5)