def get_total_number_of_sequences(n, m):
    def dp(k, last):
        if k == 1:
            return 1 if 1 <= last <= m else 0
        total = 0
        for next in range(max(2 * last, 1), min(2 * last * 2, m) + 1):
            total += dp(k - 1, next)
        return total
    return dp(n, 1)