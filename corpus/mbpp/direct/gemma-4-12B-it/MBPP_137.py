def zero_count(arr):
    if not arr:
        return 0.0
    zeros = arr.count(0)
    return zeros / len(arr)