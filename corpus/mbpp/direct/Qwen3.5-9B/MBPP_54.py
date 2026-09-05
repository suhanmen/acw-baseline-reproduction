def counting_sort(arr):
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1

    count = [0] * range_val
    for num in arr:
        count[num - min_val] += 1

    result = []
    for i, c in enumerate(count):
        if c > 0:
            result.extend([i + min_val] * c)

    return result