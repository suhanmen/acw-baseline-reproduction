def frequency_Of_Smallest(n, arr):
    if not arr:
        return 0
    min_val = min(arr)
    return arr.count(min_val)