def rearrange_bigger(n):
    """
    Given a number, find the next bigger number by rearranging the digits.
    If no such number exists, return False.
    """
    s = list(str(n))
    digits = sorted(s)

    # Find the largest possible number formed by these digits
    max_num = int("".join(digits[::-1]))

    # If the largest possible number is equal to n, no bigger number exists
    if max_num == n:
        return False

    # Optimization: check if a bigger number is even possible
    if max_num <= n:
        return False

    # To find the smallest bigger number:
    # 1. Find the rightmost digit that is smaller than the digit to its right.
    # 2. Find the smallest digit to its right that is larger than it.
    # 3. Swap them.
    # 4. Sort the digits to the right of the original position in ascending order.

    # Since the constraints on the input size aren't specified but usually 
    # imply standard integer limits, we can iterate through all permutations 
    # and find the minimum value strictly greater than n.
    # However, for efficiency, we use the standard "next lexicographical permutation" algorithm.

    nums = list(str(n))
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1

    nums[i], nums[j] = nums[j], nums[i]

    # Sort everything after i in ascending order
    nums[i+1:] = sorted(nums[i+1:])

    result = int("".join(nums))

    # Ensure the result is actually bigger (handles cases where leading zeros might occur)
    # but since we are rearranging digits of a number, we just need the smallest bigger.
    if result > n:
        return result
    else:
        return False