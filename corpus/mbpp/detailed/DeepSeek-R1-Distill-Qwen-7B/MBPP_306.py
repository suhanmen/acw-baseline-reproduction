def max_sum_increasing_subseq(arr, i, k, result):
    if not arr:
        return 0

    n = len(arr)
    if i < 0 or i >= n or k < 0 or k >= n or k <= i:
        return 0

    # Handle single element case
    if n == 1:
        return arr[0]

    # Dynamic programming to find max sum up to each index
    dp = [0] * n
    dp[0] = arr[0]

    for j in range(1, n):
        dp[j] = arr[j]
        for m in range(j):
            if arr[m] < arr[j] and dp[m] + arr[j] > dp[j]:
                dp[j] = dp[m] + arr[j]

    max_sum = dp[i]

    # If k is after i, consider including arr[k]
    if k > i:
        if dp[k] > max_sum:
            max_sum = dp[k]

    return max_sum