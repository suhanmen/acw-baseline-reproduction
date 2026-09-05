def sum_Pairs(arr, n):
    """
    Finds the sum of absolute differences in all pairs of the given array.
    The formula for the sum of absolute differences of a sorted array is:
    Sum = sum(i * arr[i] - (n - 1 - i) * arr[i]) for i from 0 to n-1.
    This simplifies to sum( (2*i - n + 1) * arr[i] ).
    """
    arr.sort()
    total_sum = 0
    for i in range(n):
        # Each element arr[i] is added i times and subtracted (n - 1 - i) times
        # in the expanded sum of |arr[i] - arr[j]| for all pairs j < i.
        # Actually, the formula for the total sum of |arr[i] - arr[j]| 
        # for all i, j (including i=j and counting both (i,j) and (j,i))
        # is 2 * sum_{i=0 to n-1} (2*i - n + 1) * arr[i].
        # However, the standard "sum of all pairs" in these types of problems 
        # usually refers to pairs (i, j) where i < j.
        # Let's check the first assertion: [1, 8, 9, 15, 16], n=5
        # Pairs (i < j): 
        # |1-8|=7, |1-9|=8, |1-15|=14, |1-16|=15 -> 44
        # |8-9|=1, |8-15|=7, |8-16|=8 -> 16
        # |9-15|=6, |9-16|=7 -> 13
        # |15-16|=1 -> 1
        # Total = 44 + 16 + 13 + 1 = 74. Correct.

        # The formula for sum_{i=0 to n-1} sum_{j=i+1 to n-1} (arr[j] - arr[i])
        # is sum_{i=0 to n-1} (i * arr[i] - (n - 1 - i) * arr[i]) 
        # wait, no: 
        # arr[i] is subtracted for all j > i (which is n-1-i times)
        # arr[i] is added for all j < i (which is i times)
        # Sum = sum_{i=0 to n-1} (i - (n - 1 - i)) * arr[i]
        # Sum = sum_{i=0 to n-1} (2*i - n + 1) * arr[i]

        # Let's re-verify: 
        # i=0: (0 - 4) * 1 = -4
        # i=1: (2 - 4) * 8 = -16
        # i=2: (4 - 4) * 9 = 0
        # i=3: (6 - 4) * 15 = 30
        # i=4: (8 - 4) * 16 = 64
        # -4 - 16 + 0 + 30 + 64 = 74. Correct.

        total_sum += (2 * i - n + 1) * arr[i]

    return total_sum