def max_sum_increasing_subseq(arr, k, i, total_len):
    if k > total_len or i < 0:
        return 0
    max_sum = [0] * total_len
    max_sum[i] = arr[i]
    if i < k:
        max_sum[i] = max(max_sum[i], arr[k])
    for j in range(i, total_len):
        if arr[j] > arr[k]:
            max_sum[j] = max(arr[j], arr[k] + max_sum[j-1])
        else:
            max_sum[j] = max(arr[j], max_sum[j-1])
    if max_sum[i] >= max_sum[k]:
        return max_sum[k]
    return max_sum[i]