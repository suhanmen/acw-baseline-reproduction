def neg_nos(nums):
    negatives = []
    for num in nums:
        if num < 0:
            negatives.append(num)
    return negatives

# Test cases
print(neg_nos([-1,4,5,-6]))  # Output: [-1,-6]
print(neg_nos([-1,-2,3,4]))  # Output: [-1,-2]
print(neg_nos([-7,-6,8,9]))  # Output: [-7,-6]