def largest_neg(nums):
    largest = None
    for num in nums:
        if num < 0:
            if largest is None or num > largest:
                largest = num
    return largest