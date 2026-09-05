def sum_Pairs(arr, k):
    """
    Calculate the sum of absolute differences of all pairs in the array.
    The parameter k is unused in the calculation (kept for signature compatibility).
    """
    if len(arr) < 2:
        return 0

    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    total = 0

    for i in range(n):
        left_sum = sorted_arr[i] * i
        right_sum = sorted_arr[i] * (n - 1 - i)
        total += left_sum - right_sum

    return total