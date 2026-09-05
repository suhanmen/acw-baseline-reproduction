def max_sum(arr, n):
    """
    Finds the maximum sum of a bi-tonic subsequence in a given array.
    A bi-tonic subsequence is a sequence that first increases and then decreases.
    """
    if n == 0:
        return 0

    # msis[i] will store the maximum sum of an increasing subsequence 
    # ending at index i.
    msis = list(arr)
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and msis[i] < msis[j] + arr[i]:
                msis[i] = msis[j] + arr[i]

    # msds[i] will store the maximum sum of a decreasing subsequence 
    # starting at index i (which is an increasing subsequence from the right).
    msds = list(arr)
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[i] > arr[j] and msds[i] < msds[j] + arr[i]:
                msds[i] = msds[j] + arr[i]

    # The maximum sum bi-tonic subsequence is the max value of (msis[i] + msds[i] - arr[i])
    # We subtract arr[i] because it is counted in both msis[i] and msds[i].
    max_bi_tonic = 0
    for i in range(n):
        max_bi_tonic = max(max_bi_tonic, msis[i] + msds[i] - arr[i])

    return max_bi_tonic