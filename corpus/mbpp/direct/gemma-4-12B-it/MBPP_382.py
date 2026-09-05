def find_rotation_count(nums):
    """
    Finds the number of rotations in a circularly sorted array.
    The number of rotations is equal to the index of the minimum element.
    """
    if not nums:
        return 0

    low = 0
    high = len(nums) - 1

    # If the array is not rotated at all
    if nums[low] <= nums[high]:
        return 0

    while low <= high:
        mid = (low + high) // 2

        # Check if mid+1 is the minimum element
        if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
            return mid + 1

        # Check if mid is the minimum element
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid

        # Decide which half to search
        if nums[mid] >= nums[low]:
            # Left side is sorted, pivot must be on the right
            low = mid + 1
        else:
            # Right side is sorted, pivot must be on the left
            high = mid - 1

    return 0