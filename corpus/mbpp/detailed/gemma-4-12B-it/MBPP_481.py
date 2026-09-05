from typing import List


def is_subset_sum(nums: List[int], n: int, target_sum: int) -> bool:
    """
    Determines if there is a subset of the first 'n' elements of 'nums' 
    that sums up to 'target_sum'.

    Args:
        nums: A list of integers.
        n: The number of elements from the start of the list to consider.
        target_sum: The target sum to reach.

    Returns:
        bool: True if a subset exists, False otherwise.
    """
    # Input Validation
    if not isinstance(nums, list):
        raise ValueError("Input 'nums' must be a list.")

    if not isinstance(n, int) or n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")

    if not isinstance(target_sum, int):
        raise ValueError("Input 'target_sum' must be an integer.")

    # Edge Case: Handle 'n' being larger than the actual list length
    # The problem implies we consider the first n elements.
    effective_n = min(n, len(nums))

    # Extract the relevant subset of numbers
    subset_pool = nums[:effective_n]

    # Edge Case: Target sum is 0. 
    # An empty subset always sums to 0.
    if target_sum == 0:
        return True

    # Edge Case: Empty subset_pool and non-zero target_sum.
    if effective_n == 0:
        return False

    # Problem constraints: This is the classic Subset Sum Problem.
    # We use Dynamic Programming to solve this efficiently.
    # dp[i] will be True if a sum 'i' is achievable with the current numbers.

    # The size of our DP table is target_sum + 1.
    # If target_sum is negative, we cannot achieve it with a subset of 
    # non-negative integers (standard subset sum assumption).
    # If the problem allows negative numbers, the logic would require 
    # a different approach (offsetting or dictionary-based DP).
    # Given the test cases (positive numbers), we handle target_sum < 0.
    if target_sum < 0:
        # In standard subset sum problems, we assume non-negative numbers.
        # If negative numbers exist in nums, this logic needs adjustment.
        # However, based on provided assertions, target_sum is positive.
        # We check if the sum can be reached regardless.
        # For simplicity and standard behavior, we return False for negative targets
        # unless the list contains negative numbers that could sum to it.
        # Let's stick to the standard DP for non-negative target sums.
        pass

    # To handle negative target_sums and negative numbers, 
    # a dictionary-based DP is more robust.
    # reachable_sums stores all possible sums we can achieve.
    reachable_sums = {0}

    for current_num in subset_pool:
        # We create a set of new sums to avoid modifying the set 
        # while iterating over it.
        new_sums = set()
        for existing_sum in reachable_sums:
            combined_sum = existing_sum + current_num
            new_sums.add(combined_sum)

        # Update our collection of reachable sums
        reachable_sums.update(new_sums)

        # Optimization: If we already found the target_sum, we can exit early.
        if target_sum in reachable_sums:
            return True

    # Final check if the target_sum was ever reached.
    is_found = target_sum in reachable_sums
    return is_found


# Standard competitive programming / interview style DP 
# is usually O(n * target_sum), but dictionary-based DP 
# is O(n * number_of_unique_sums).