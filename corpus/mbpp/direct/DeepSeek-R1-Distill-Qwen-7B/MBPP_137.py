def zero_count(arr):
    zero_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1
    return zero_count / len(arr)