def count_no_of_ways(n: int, k: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return k
    if n == 2:
        return k * k

    # dp[i][0] = number of ways where ith post is different from (i-1)th
    # dp[i][1] = number of ways where ith post is same as (i-1)th
    prev_diff = k * (k - 1)  # for i=2, one choice for first, (k-1) for second (different)
    prev_same = 0            # for i=2, can't have same if we consider building from diff base correctly

    # Recalibrate for i=2:
    # Total ways for 2 posts = k*k
    # Same adjacent: k (first any, second same as first)
    # Different adjacent: k*(k-1)
    prev_same = k
    prev_diff = k * (k - 1)

    current_diff = 0
    current_same = 0

    for i in range(3, n + 1):
        current_same = prev_diff  # can only be same if previous was diff
        current_diff = (prev_diff + prev_same) * (k - 1)  # current diff can come from either prev state
        prev_same, prev_diff = current_same, current_diff

    return prev_same + prev_diff