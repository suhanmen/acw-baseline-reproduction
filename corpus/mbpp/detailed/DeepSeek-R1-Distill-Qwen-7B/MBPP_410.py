def min_val(lst):
    if not lst:
        raise ValueError("The list is empty.")

    nums = []
    for item in lst:
        try:
            num = int(item)
            nums.append(num)
        except (ValueError, TypeError):
            pass

    if not nums:
        raise ValueError("All elements are non-numeric.")

    return min(nums)