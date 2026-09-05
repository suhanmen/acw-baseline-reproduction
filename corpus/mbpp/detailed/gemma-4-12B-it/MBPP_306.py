from typing import List

def max_sum_increasing_subseq(arr: List[int], n: int, i: int, k: int) -> int:
    """
    Finds the maximum sum of an increasing subsequence that:
    1. Ends at some index j such that 0 <= j <= i.
    2. Includes the element at index k (where k > i).
    3. Is strictly increasing.

    Note: To include index k in an increasing subsequence, the preceding 
    elements must be strictly less than arr[k]. Since the subsequence 
    must be formed from elements up to index i and then include index k, 
    we look for the max sum increasing subsequence ending at some j (j <= i) 
    such that arr[j] < arr[k].
    """
    # --- Input Validation ---
    if not isinstance(arr, list):
        raise ValueError("Input 'arr' must be a list of integers.")

    if n <= 0 or n > len(arr):
        raise ValueError("Size 'n' is invalid relative to the array length.")

    # Check if indices are within bounds
    if i < 0 or i >= n:
        raise ValueError(f"Index 'i' ({i}) is out of bounds [0, {n-1}].")
    if k < 0 or k >= n:
        raise ValueError(f"Index 'k' ({k}) is out of bounds [0, {n-1}].")

    # Requirement check: k must be greater than i
    if k <= i:
        raise ValueError(f"Requirement k > i failed: k={k}, i={i}.")

    # Handle empty array or base cases (though n > 0 ensures at least one element)
    if n == 0:
        return 0

    # --- Step 1: Compute Max Sum Increasing Subsequence ending at each index up to i ---
    # We use a dynamic programming approach where msis[j] stores the 
    # maximum sum of an increasing subsequence ending exactly at index j.
    msis = [0] * n

    for j in range(n):
        # The base sum is the value of the element itself
        current_val = arr[j]
        msis[j] = current_val

        # Look at all elements before j to see if we can extend their subsequence
        for prev_idx in range(j):
            # To be strictly increasing:
            if arr[prev_idx] < current_val:
                potential_sum = msis[prev_idx] + current_val
                if potential_sum > msis[j]:
                    msis[j] = potential_sum

    # --- Step 2: Identify valid subsequences ending at or before i ---
    # We need to find the maximum msis[j] where j <= i AND arr[j] < arr[k].
    # Because the sequence must eventually include arr[k], any element 
    # contributing to the sum before k must be strictly smaller than arr[k].

    target_element_value = arr[k]
    max_sum_before_k = -1

    # Check all indices from 0 to i inclusive
    for j in range(i + 1):
        # A subsequence ending at j can be linked to index k 
        # if and only if the value at j is strictly less than the value at k.
        if arr[j] < target_element_value:
            if msis[j] > max_sum_before_k:
                max_sum_before_k = msis[j]

    # --- Step 3: Calculate Final Result ---
    # If no index j <= i was found such that arr[j] < arr[k], 
    # it means the only valid increasing subsequence including k 
    # starts with k itself (or elements between i and k, 
    # but the prompt asks for a prefix till i + including k).
    # However, based on the test cases:
    # Case 1: [1, 101, 2, 3, 100, 4, 5], i=4, k=6. 
    #   arr[4]=100, arr[6]=5. No j <= 4 has arr[j] < 5 except indices 0, 2, 3 (values 1, 2, 3).
    #   msis indices: msis[0]=1, msis[1]=102, msis[2]=3, msis[3]=6, msis[4]=106.
    #   Valid j <= 4 with arr[j] < 5: j=0 (val 1), j=2 (val 3), j=3 (val 6).
    #   Max is msis[3]=6. Total sum = 6 + arr[6] = 6 + 5 = 11.

    # If no valid prefix sum was found, the max sum is just the value at k.
    if max_sum_before_k == -1:
        final_result = target_element_value
    else:
        final_result = max_sum_before_k + target_element_value

    return final_result