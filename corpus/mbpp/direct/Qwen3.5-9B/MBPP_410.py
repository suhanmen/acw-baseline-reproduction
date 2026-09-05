def min_val(items):
    nums = [x for x in items if isinstance(x, (int, float))]
    return min(nums)