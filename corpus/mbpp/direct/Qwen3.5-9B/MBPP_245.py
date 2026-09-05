def max_sum(arr, n):
    if n == 0:
        return 0

    inc = [0] * n  # Max sum of increasing subsequence ending at i
    dec = [0] * n  # Max sum of decreasing subsequence ending at i

    for i in range(n):
        inc[i] = arr[i]
        dec[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i]:
                inc[i] = max(inc[i], inc[j] + arr[i])
            if arr[j] > arr[i]:
                dec[i] = max(dec[i], dec[j] + arr[i])

    max_total = 0
    for i in range(n):
        max_total = max(max_total, inc[i] + dec[i] - arr[i])

    return max_total