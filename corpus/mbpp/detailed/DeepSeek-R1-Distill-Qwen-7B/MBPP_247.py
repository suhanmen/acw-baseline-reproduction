def lps(s):
    n = len(s)
    if n == 0:
        return 0

    # Create a table to store results of subproblems
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 2
        else:
            dp[i][i + 1] = 1

    # Fill the table for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                # If first and last characters are same, then take the result of the inner substring
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # Otherwise, take the maximum of the two possibilities
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]