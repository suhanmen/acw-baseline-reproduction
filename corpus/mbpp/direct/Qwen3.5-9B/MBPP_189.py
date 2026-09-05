def first_Missing_Positive(nums, n):
    """
    Find the first missing positive integer in the list.
    The function considers only positive integers (>=1) and checks within range [1, n].
    If all numbers from 1 to n are present, it returns n+1.

    :param nums: List of integers
    :param n: Number of elements considered (upper bound for search)
    :return: First missing positive integer
    """
    present = set()
    for num in nums:
        if 1 <= num <= n:
            present.add(num)

    for i in range(1, n + 1):
        if i not in present:
            return i

    return n + 1