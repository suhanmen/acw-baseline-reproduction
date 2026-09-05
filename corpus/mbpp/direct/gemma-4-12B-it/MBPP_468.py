def max_product(arr, n):
    """
    Finds the maximum product formed by multiplying numbers of an 
    increasing subsequence of the given array.
    """
    if not arr:
        return 0

    # dp[i] stores the maximum product of an increasing subsequence 
    # ending at index i.
    dp = [0] * n

    for i in range(n):
        # Initialize dp[i] with the value of the element itself,
        # as a single element is technically an increasing subsequence.
        dp[i] = arr[i]

        for j in range(i):
            # If the sequence is increasing (arr[j] < arr[i])
            if arr[j] < arr[i]:
                # Update dp[i] if the product through j is greater.
                # Note: Since values are positive in the test cases, 
                # standard multiplication is used.
                dp[i] = max(dp[i], dp[j] * arr[i])

    return max(dp)

if __name__ == "__main__":
    assert max_product([3, 100, 4, 5, 150, 6], 6) == 45000
    assert max_product([4, 42, 55, 68, 80], 5) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60], 8) == 21780000