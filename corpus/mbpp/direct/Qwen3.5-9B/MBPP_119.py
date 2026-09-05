def search(nums, n):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        # Determine if mid is a singleton
        if (mid == 0 or nums[mid - 1] != nums[mid]) and \
           (mid == len(nums) - 1 or nums[mid + 1] != nums[mid]):
            return nums[mid]
        # Check if left side has even number of elements up to mid
        if (mid - left) % 2 == 1:
            # Odd number of elements to the left, so single is on the right
            left = mid + 1
        else:
            # Even number of elements to the left, so single is on the left (or at mid)
            right = mid - 1
    return None

assert search([1,1,2,2,3],5) == 3
assert search([1,1,3,3,4,4,5,5,7,7,8],11) == 8
assert search([1,2,2,3,3,4,4],7) == 1