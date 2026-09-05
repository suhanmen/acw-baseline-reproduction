from typing import List, Tuple

def max_Product(nums: List[int]) -> Tuple[int, int]:
    if len(nums) < 2:
        raise ValueError("Array must contain at least two elements.")

    # Initialize with the first two elements
    first = nums[0]
    second = nums[1]
    first_idx = 0
    second_idx = 1

    # Iterate through the rest
    for i in range(2, len(nums)):
        if nums[i] > first:
            second = first
            second_idx = first_idx
            first = nums[i]
            first_idx = i
        elif nums[i] > second:
            second = nums[i]
            second_idx = i

    # Check if the largest product comes from two smallest negatives
    # Reset tracking
    min1 = min(nums[0], nums[1])
    min2 = max(nums[0], nums[1])
    min1_idx = 0 if nums[0] <= nums[1] else 1
    min2_idx = 1 if nums[0] <= nums[1] else 0

    for i in range(2, len(nums)):
        if nums[i] < min1:
            min2 = min1
            min2_idx = min1_idx
            min1 = nums[i]
            min1_idx = i
        elif nums[i] < min2:
            min2 = nums[i]
            min2_idx = i

    # Compare products
    max_product = first * second
    min_product = min1 * min2

    if min_product > max_product:
        return (min1, min2)
    else:
        return (first, second)