def bell_number(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: B(0) is defined as 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        for j in range(i):
            dp[i] += dp[j]
    return dp[n]

# Verify the assertions
assert bell_number(2) == 2, "Failed on bell_number(2)"
assert bell_number(10) == 115975, "Failed on bell_number(10)"
assert bell_number(56) == 6775685320645824322581483068371419745979053216268760300, "Failed on bell_number(56)"
print("All assertions passed")