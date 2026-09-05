def frequency_Of_Smallest(n, arr):
    if not arr:
        return 0
    min_val = min(arr)
    count = 0
    for num in arr:
        if num == min_val:
            count += 1
    return count