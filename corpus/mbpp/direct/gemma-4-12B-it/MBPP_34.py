from typing import List

def find_missing(nums: List[int], n: int) -> int:
    """
    Finds the missing number in a sorted array of consecutive integers.

    Args:
        nums: A sorted list of integers.
        n: The expected length of the sequence if no numbers were missing.

    Returns:
        The missing integer.
    """
    # Using Binary Search to achieve O(log n) time complexity
    # Since the list is sorted and integers are consecutive, 
    # the value at index i should be nums[0] + i.

    left = 0
    right = len(nums) - 1

    # First, determine the starting value
    start_val = nums[0]

    # If the sequence is perfectly consecutive, 
    # the missing number must be either before the first element, 
    # after the last element, or it's just not in the range.
    # However, based on the test cases provided:
    # [1,2,3,5], 4 -> Missing is 4 (between 3 and 5)
    # [1,3,4,5], 4 -> Missing is 2 (between 1 and 3)
    # [1,2,3,5,6,7], 5 -> Missing is 4 (between 3 and 5)

    # The pattern indicates we are looking for the first gap where
    # nums[i+1] - nums[i] > 1.

    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i] > 1:
            return nums[i] + 1

    # Fallback cases for edge numbers if the list is already consecutive
    # Though the provided test cases are all gaps within the range.
    return -1

# The provided assertions require a slightly different logic 
# because they imply the "missing" number is within the range 
# spanned by the sequence's bounds or the intended count.
# Re-evaluating based on specific examples:
def find_missing(nums: List[int], n: int) -> int:
    # The actual logic for the specific examples provided:
    # [1,2,3,5], 4 -> Index 3 is 5, should be 4.
    # [1,3,4,5], 4 -> Index 1 is 3, should be 2.
    # [1,2,3,5,6,7], 5 -> Index 3 is 5, should be 4.

    # This is a standard "Missing Number in Range" problem.
    # We expect a range starting at nums[0] and ending at nums[0] + n - 1.
    # But the test cases show the range is effectively 1 to n.

    # Let's use the sum formula: Sum = (n * (n + 1)) / 2
    # This works if the sequence is 1 to n.

    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Since the sum formula works for all provided assertions:
# 1+2+3+5 = 11. n=4, sum=10. 10-11 = -1? No, sum of 1..4 is 10. 
# Wait, 1+2+3+4 = 10. 1+2+3+5 = 11. 
# If nums = [1,2,3,5], sum is 11. If n=4, the expected sum of 1..4 is 10.
# The test cases actually imply that n is NOT the max number, but 
# the number of elements that SHOULD be there.
# Let's re-examine:
# [1,2,3,5], n=4. Sequence is 1,2,3,4. Sum 10. Current sum 11. 
# This means the '5' is the extra? No, the '4' is missing.
# The sum of a sequence of n numbers starting at 1 is n(n+1)/2.
# If a number x is missing from a sequence of n numbers starting at 1,
# and we have n numbers provided, one number is larger than it should be.
# If we have n-1 numbers provided, the sum is (n(n+1)/2) - missing.

# Let's look at the examples again:
# [1,2,3,5], n=4. len is 4. 1+2+3+5 = 11. Expected sum of 1..4 = 10.
# [1,3,4,5], n=4. len is 4. 1+3+4+5 = 13. Expected sum of 1..4 = 10.
# This interpretation is wrong. Let's try: 
# The numbers are a subset of 1...n. But [1,2,3,5,6,7] has 6 elements.
# The assertions:
# 1. [1,2,3,5], 4 -> 4 is missing. (Sequence 1,2,3,4,5? No, n=4)
# 2. [1,3,4,5], 4 -> 2 is missing.
# 3. [1,2,3,5,6,7], 5 -> 4 is missing.

# Correct logic: The numbers are consecutive starting from 1. 
# The number 'n' is not the max, it's a threshold or a specific count.
# In all cases:
# find_missing([1,2,3,5], 4) -> the sequence is 1,2,3,4,5. 4 is missing.
# find_missing([1,3,4,5], 4) -> the sequence is 1,2,3,4,5. 2 is missing.
# find_missing([1,2,3,5,6,7], 5) -> the sequence is 1,2,3,4,5,6,7. 4 is missing.

# Wait, if n is the number of elements missing? No.
# If n is the value that SHOULD be there but is skipped?
# Let's look at the first list: [1,2,3,5]. Indices 0,1,2,3. 
# Values are 1,2,3,5. The value at index 3 is 5, but it should be 4.
# Second list: [1,3,4,5]. Index 1 is 3, should be 2.
# Third list: [1,2,3,5,6,7]. Index 3 is 5, should be 4.

# Final logic: find index i where nums[i] != i + 1. 
# The missing number is i + 1.
# But in find_missing([1,2,3,5], 4), index 3 is 5, and i+1 is 4. Correct.
# In find_missing([1,3,4,5], 4), index 1 is 3, and i+1 is 2. Correct.
# In find_missing([1,2,3,5,6,7], 5), index 3 is 5, and i+1 is 4. Correct.

def find_missing(nums: List[int], n: int) -> int:
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return n