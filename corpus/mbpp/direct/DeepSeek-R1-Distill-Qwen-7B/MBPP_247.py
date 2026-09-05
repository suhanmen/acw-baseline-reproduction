def lps(s):
    n = len(s)
    # Create a table to store lengths of longest palindromic subsequences
    # Initialize a 2D table with zeros
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Check for palindromic subsequences of length 2 and above
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the longest palindromic subsequence is at dp[0][n-1]
    return dp[0][n - 1]

# Example usage:
# assert lps("TENS FOR TENS") == 5 
# assert lps("CARDIO FOR CARDS") == 7
# assert lps("PART OF THE JOURNEY IS PART") == 9