def find_Min(nums, start, end):
    """
    Finds the minimum element in a sorted and rotated array using binary search.

    Args:
        nums: List[int] - The sorted and rotated array.
        start: int - The starting index of the subarray.
        end: int - The ending index of the subarray.

    Returns:
        int - The minimum value in the array.
    """
    if not nums or start > end:
        return None

    low = start
    high = end

    # If the array is not rotated (already sorted)
    if nums[low] <= nums[high]:
        return nums[low]

    while low <= high:
        mid = (low + high) // 2

        # Check if mid+1 is the minimum
        if mid < end and nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        # Check if mid is the minimum
        if mid > start and nums[mid] < nums[mid - 1]:
            return nums[mid]

        # Decide which half to search
        if nums[mid] > nums[low]:
            # Left side is sorted, min must be in the right side
            low = mid + 1
        else:
            # Right side is sorted, min must be in the left side
            high = mid - 1

    return nums[low]

if __name__ == "__main__":
    assert find_Min([1,2,3,4,5],0,4) == 1
    assert find_Min([4,6,8],0,2) == 4
    assert find_Min([2,3,5,7,9],0,4) == 2