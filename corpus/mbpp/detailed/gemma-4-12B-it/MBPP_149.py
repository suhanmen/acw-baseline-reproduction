from typing import List


def longest_subseq_with_diff_one(nums: List[int], n: int) -> int:
    """
    Finds the length of the longest subsequence where the difference 
    between adjacent elements is exactly 1 (or -1).

    Note: The problem description implies a subsequence where |a[i] - a[i-1]| = 1.
    However, the provided assertions suggest a specific interpretation:
    The assertions seem to count the total number of elements in the array 
    that can form a chain where each step changes by exactly 1.

    Let's re-examine the assertions:
    1. [1, 2, 3, 4, 5, 3, 2], n=7 -> Result 6. 
       Explanation: The subsequence [1, 2, 3, 4, 5] is 5. 
       Wait, the result is 6. If we include the 3 and 2 at the end:
       [1, 2, 3, 4, 5] -> 5. [1, 2, 3, 2] -> 4. [1, 2, 3, 4, 3, 2] -> 6.
       This confirms it's a subsequence where |curr - prev| == 1.

    2. [10, 9, 4, 5, 4, 8, 6], n=7 -> Result 3.
       [10, 9] is 2. [4, 5, 4] is 3. [8] is 1. [6] is 1. Max is 3.

    3. [1, 2, 3, 2, 3, 7, 2, 1], n=8 -> Result 7.
       [1, 2, 3, 2, 3, 2, 1] -> 7 elements.

    Strategy:
    This is a Dynamic Programming problem. For each element x in the array,
    the longest subsequence ending at x is 1 + max(length ending at x-1, 
    length ending at x+1).
    """
    # Validation of input types
    if not isinstance(nums, list):
        raise ValueError("Input 'nums' must be a list.")
    if not isinstance(n, int):
        raise ValueError("Input 'n' must be an integer.")

    # Validation of array length
    if len(nums) != n:
        # Depending on requirements, we could raise an error or just use len(nums)
        # Since the assertion implies n is the size, we check consistency.
        pass

    # Handle empty input case
    if n == 0 or len(nums) == 0:
        return 0

    # dp dictionary stores the length of the longest subsequence 
    # ending with a specific value.
    # key: value of the element, value: length of subsequence ending there.
    dp: dict[int, int] = {}

    max_length = 0

    for current_val in nums:
        # For the current number, the longest subsequence ending here
        # can be formed by appending current_val to a subsequence 
        # ending in (current_val - 1) or (current_val + 1).

        # Option 1: Subsequence ending in current_val - 1
        prev_minus_one = current_val - 1
        length_from_minus_one = 0
        if prev_minus_one in dp:
            length_from_minus_one = dp[prev_minus_one]

        # Option 2: Subsequence ending in current_val + 1
        prev_plus_one = current_val + 1
        length_from_plus_one = 0
        if prev_plus_one in dp:
            length_from_plus_one = dp[prev_plus_one]

        # The best we can do ending at 'current_val' is 
        # 1 + the best of the two neighbors.
        # If neither exists, it's just 1 (the element itself).
        best_prev_length = max(length_from_minus_one, length_from_plus_one)
        current_max_len = 1 + best_prev_length

        # Update the DP table. 
        # We take the max because there might be multiple ways 
        # to reach 'current_val' with different lengths.
        if current_val in dp:
            dp[current_val] = max(dp[current_val], current_max_len)
        else:
            dp[current_val] = current_max_len

        # Track the global maximum
        if dp[current_val] > max_length:
            max_length = dp[current_val]

    return max_length