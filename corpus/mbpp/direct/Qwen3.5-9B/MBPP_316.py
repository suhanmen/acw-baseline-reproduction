def find_last_occurrence(nums, target):
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            left = mid + 1  # Continue searching in the right half
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

assert find_last_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 3
assert find_last_occurrence([2, 3, 5, 8, 6, 6, 8, 9, 9, 9], 9) == 9
assert find_last_occurrence([2, 2, 1, 5, 6, 6, 6, 9, 9, 9], 6) == 6