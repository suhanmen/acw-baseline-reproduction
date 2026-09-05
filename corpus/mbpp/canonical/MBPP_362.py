def max_occurrences(nums):
    max_val = 0
    result = nums[0] 
    for i in nums:
        occu = nums.count(i)
        if occu > max_val:
            max_val = occu
            result = i 
    return result