def re_arrange_array(arr, n):
    result = [0] * n
    neg_idx = 0
    pos_idx = 0

    # Place negatives at the beginning
    for i in range(n):
        if arr[i] < 0:
            result[neg_idx] = arr[i]
            neg_idx += 1

    # Place positives (and zeros, if any) after negatives
    for i in range(n):
        if arr[i] >= 0:
            result[pos_idx] = arr[i]
            pos_idx += 1

    return result