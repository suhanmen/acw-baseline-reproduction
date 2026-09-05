def lps(s: str) -> int:
    """
    Finds the length of the longest palindromic subsequence in a given string.
    """
    # Handle empty string or single character
    if not s:
        return 0

    n = len(s)
    # Create a DP table where dp[i][j] stores the length of the 
    # longest palindromic subsequence in s[i...j]
    dp = [[0] * n for _ in range(n)]

    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the table for lengths 2 up to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                # If characters match, add 2 to the length of the 
                # inner subsequence
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # If characters don't match, take the maximum 
                # of excluding either the first or the last character
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

if __name__ == "__main__":
    assert lps("TENS FOR TENS") == 5 
    assert lps("CARDIO FOR CARDS") == 7
    assert lps("PART OF THE JOURNEY IS PART") == 9