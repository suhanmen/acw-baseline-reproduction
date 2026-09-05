from typing import List

def first_Missing_Positive(nums: List[int], n: int) -> int:
    """
    Finds the first missing positive integer from a list of integers.

    The function identifies the smallest positive integer (starting from 1)
    that is not present in the provided list.

    Args:
        nums (List[int]): A list of integers containing positive, 
                           negative, and zero values.
        n (int): The size of the input list (provided for consistency 
                  with the problem signature).

    Returns:
        int: The first missing positive integer.

    Raises:
        ValueError: If the input list is None or if n does not match 
                    the actual length of the list.
    """
    # --- Input Validation ---
    if nums is None:
        raise ValueError("Input list 'nums' cannot be None.")

    actual_length = len(nums)
    if actual_length != n:
        # Depending on strictness, one might choose to ignore n or raise an error.
        # Given the prompt's requirement for defensive code, we validate n.
        raise ValueError(f"The provided length n ({n}) does not match the "
                         f"actual length of the list ({actual_length}).")

    # --- Edge Case Handling ---
    # If the list is empty, the first missing positive integer is 1.
    if actual_length == 0:
        return 1

    # --- Logic Implementation ---
    # We use a set for O(1) average time complexity lookups.
    # This handles duplicate values and negative numbers efficiently.
    positive_numbers_set = set()

    for current_num in nums:
        # We only care about positive integers.
        # Non-positive integers (0, -1, -2, etc.) do not affect the "first missing positive".
        if current_num > 0:
            positive_numbers_set.add(current_num)

    # We iterate starting from 1 upwards.
    # The first number we encounter that is NOT in our set is the answer.
    # Since there are 'n' elements in the list, the missing number 
    # must fall within the range [1, n + 1].
    current_candidate = 1
    while True:
        if current_candidate not in positive_numbers_set:
            # This is the first positive integer not present in the input.
            return current_candidate

        # Increment to check the next possible positive integer.
        current_candidate += 1

# Standard verification of the provided assertions
if __name__ == "__main__":
    # Test Case 1: [1, 2, 3, -1, 5], n=5
    # Positives present: {1, 2, 3, 5}. Missing: 4.
    assert first_Missing_Positive([1, 2, 3, -1, 5], 5) == 4

    # Test Case 2: [0, -1, -2, 1, 5, 8], n=6
    # Positives present: {1, 5, 8}. Missing: 2.
    assert first_Missing_Positive([0, -1, -2, 1, 5, 8], 6) == 2

    # Test Case 3: [0, 1, 2, 5, -8], n=5
    # Positives present: {1, 2, 5}. Missing: 3.
    assert first_Missing_Positive([0, 1, 2, 5, -8], 5) == 3