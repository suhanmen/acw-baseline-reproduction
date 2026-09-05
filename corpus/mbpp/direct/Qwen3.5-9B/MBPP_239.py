def get_total_number_of_sequences(n: int, m: int) -> int:
    """
    Returns the number of possible sequences of length n such that:
      - The first element is at least 1.
      - Each subsequent element is >= 2 * previous element.
      - Each element is <= m.
    """
    if n <= 0 or m <= 0:
        return 0

    # dp[i][x] = number of valid sequences of length i ending with value x
    # We only need previous length, so use two rows.
    max_val = m
    prev = [1] * (max_val + 1)  # length 1 sequences: one for each starting value 1..m

    for length in range(2, n + 1):
        curr = [0] * (max_val + 1)
        for x in range(1, max_val + 1):
            # next value y must satisfy: y >= 2*x and y <= m
            # So for a given previous value p, allowed next values are [2*p, m]
            # Instead of iterating over p then y, we iterate y and sum over valid p:
            # y >= 2*p  =>  p <= y // 2
            # Also p >= 1
            limit = y // 2
            if limit >= 1:
                curr[y] += sum(prev[1:limit + 1])
        prev = curr

    # Sum over all possible last values for sequence of length n
    return sum(prev)