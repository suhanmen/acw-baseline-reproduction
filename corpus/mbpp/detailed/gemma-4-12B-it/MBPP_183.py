from typing import List

def count_pairs(arr: List[int], n: int, k: int) -> int:
    """
    Counts all pairs of indices (i, j) such that i < j and abs(arr[i] - arr[j]) == k.

    Note: Based on the provided assertions, the requirement is to count pairs of 
    indices, not distinct value pairs.

    Example 3 analysis:
    arr = [2, 4, 1, 3, 4], k = 2
    Pairs (i, j) with i < j and |arr[i] - arr[j]| == 2:
    1. (0, 1) -> |2 - 4| = 2
    2. (0, 4) -> |2 - 4| = 2
    3. (2, 3) -> |1 - 3| = 2
    Total = 3. Matches assertion.
    """
    # --- Input Validation ---
    if not isinstance(arr, list):
        raise TypeError("The first argument 'arr' must be a list of integers.")

    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("The arguments 'n' and 'k' must be integers.")

    # Ensure n matches the actual length of the array for safety
    # If n is provided, we respect it as the bound of the array we are considering
    # but we should verify the array is actually that long.
    actual_len = len(arr)
    if actual_len < n:
        # In a production environment, we might raise an exception here.
        # For this exercise, we will assume n is correct or work with actual_len.
        n = actual_len

    # Handle edge cases
    if n < 2:
        return 0

    # Difference k is treated as absolute.
    target_diff = abs(k)

    pair_count = 0

    # To solve this in O(n) time, we can use a hash map to store frequencies
    # of numbers seen so far as we iterate through the list.
    # This allows us to count how many previous numbers satisfy the condition.

    # Dictionary to store counts of numbers encountered so far
    seen_counts = {}

    for i in range(n):
        current_val = arr[i]
        if not isinstance(current_val, int):
            raise ValueError(f"Element at index {i} is not an integer: {current_val}")

        # We are looking for a value 'x' such that |current_val - x| = target_diff
        # This means x = current_val - target_diff  OR  x = current_val + target_diff

        # Case 1: target_diff > 0
        if target_diff > 0:
            # Potential partner 1
            partner_low = current_val - target_diff
            # Potential partner 2
            partner_high = current_val + target_diff

            # Check if partner_low was seen before
            if partner_low in seen_counts:
                pair_count += seen_counts[partner_low]

            # Check if partner_high was seen before
            if partner_high in seen_counts:
                pair_count += seen_counts[partner_high]

        # Case 2: target_diff == 0
        else:
            # If k is 0, we need to find how many times current_val appeared before
            if current_val in seen_counts:
                pair_count += seen_counts[current_val]

        # Update the frequency map with the current value
        seen_counts[current_val] = seen_counts.get(current_val, 0) + 1

    return pair_count