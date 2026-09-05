def zero_count(arr):
    if len(arr) == 0:
        return 0.0
    return float(arr.count(0)) / len(arr)