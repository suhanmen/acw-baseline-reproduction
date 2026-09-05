from typing import List

def max_product(nums: List[int], n: int) -> int:
    """
    Finds the maximum product formed by multiplying numbers of an 
    increasing subsequence of the given array.

    Args:
        nums: A list of integers.
        n: The number of elements in the list (should match len(nums)).

    Returns:
        The maximum product of an increasing subsequence.

    Raises:
        ValueError: If inputs are invalid.
    """
    # --- Input Validation ---
    if not isinstance(nums, list):
        raise ValueError("Input 'nums' must be a list of integers.")

    if not isinstance(n, int):
        raise ValueError("Input 'n' must be an integer.")

    if len(nums) != n:
        raise ValueError(f"The length of 'nums' ({len(nums)}) does not match 'n' ({n}).")

    # Edge case: Empty array or single element
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    # --- Problem Logic ---
    # Let dp[i] be the maximum product of an increasing subsequence 
    # ending at index i.
    # We initialize dp[i] with nums[i] because the subsequence can 
    # consist of just the element itself.

    # Using a list to store maximum products for each index.
    dp: List[int] = [0] * n

    for i in range(n):
        # Initially, the best product ending at i is the value at i itself.
        dp[i] = nums[i]

        # Compare current element nums[i] with all previous elements nums[j].
        for j in range(i):
            # A subsequence is strictly increasing if the current 
            # element is strictly greater than the previous element.
            if nums[j] < nums[i]:
                # Calculate the product of the best subsequence ending at j
                # multiplied by the current element.
                current_product = dp[j] * nums[i]

                # If this product is greater than the currently stored 
                # value for index i, update it.
                if current_product > dp[i]:
                    dp[i] = current_product

    # The answer is the maximum value in our dp table.
    # We use a dedicated variable for clarity.
    max_val = dp[0]
    for i in range(1, n):
        if dp[i] > max_val:
            max_val = dp[i]

    return max_val

# The assertions provided in the problem description:
# assert max_product([3, 100, 4, 5, 150, 6], 6) == 45000 
# (Subsequence: 3, 4, 5, 150 -> 3 * 4 * 5 * 150 = 9000? 
# Wait, looking at the sample: 100 * 150 is 15000. 
# Actually, 3 * 4 * 5 * 150 = 9000. 
# Let's re-check: 3 * 4 * 5 * 150 = 9000. 
# Wait, 100 * 150 is only 15000.
# 3 * 100 * 150 is not possible as 100 > 150 is false.
# Wait, 3 * 4 * 5 * 150 is 9000.
# Let's check the first assertion again: max_product([3, 100, 4, 5, 150, 6], 6) == 45000.
# 3 * 100 * 150 is not possible.
# 4 * 5 * 150 = 3000.
# Ah, 3 * 100 = 300. 300 * 150 is not possible (100 < 150). 
# 3 * 100 * 150 = 45000.
# Let's re-verify indices: 
# index 0: 3
# index 1: 100
# index 2: 4
# index 3: 5
# index 4: 150
# index 5: 6
# Increasing subsequence: 3 (idx 0), 100 (idx 1), 150 (idx 4).
# Product: 3 * 100 * 150 = 45000. Correct.

# assert max_product([4, 42, 55, 68, 80], 5) == 50265600
# 4 * 42 * 55 * 68 * 80 = 50265600. Correct.

# assert max_product([10, 22, 9, 33, 21, 50, 41, 60], 8) == 21780000
# 10 * 22 * 33 * 50 * 60 = 21780000. Correct.