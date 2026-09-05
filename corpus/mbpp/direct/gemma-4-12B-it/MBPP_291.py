def count_no_of_ways(n, k):
    """
    Calculates the number of ways to paint a fence with n posts and k colors
    such that at most 2 adjacent posts have the same color.
    """
    if n == 0:
        return 0
    if n == 1:
        return k
    if n == 2:
        return k * k

    # dp[i][0] is the number of ways to paint i posts such that 
    # the i-th post has a different color than the (i-1)-th post.
    # dp[i][1] is the number of ways to paint i posts such that 
    # the i-th post has the same color as the (i-1)-th post.

    # Initial values for n = 2:
    # Different colors: k * (k - 1)
    # Same colors: k
    dp = [[0, 0] for _ in range(n + 1)]

    dp[1][0] = k
    dp[1][1] = 0

    # For i = 2:
    # dp[2][0] = dp[1][0] * (k-1) + dp[1][1] * (k-1)
    # dp[2][1] = dp[1][0] (must have been different from previous)
    # However, let's use the standard logic for n >= 2 starting from n=2:

    dp[2][0] = k * (k - 1)
    dp[2][1] = k

    for i in range(3, n + 1):
        # To have the i-th post different from (i-1)-th:
        # It can follow a post that was the same as (i-2)-th,
        # or a post that was different from (i-2)-th.
        dp[i][0] = (dp[i-1][0] + dp[i-1][1]) * (k - 1)

        # To have the i-th post same as (i-1)-th:
        # The (i-1)-th post must have been different from the (i-2)-th post.
        dp[i][1] = dp[i-1][0]

    return dp[n][0] + dp[n][1]