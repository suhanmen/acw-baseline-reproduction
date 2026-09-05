from typing import List

def lps(s: str) -> int:
    """
    Finds the length of the longest palindromic subsequence (LPS) in a given string.

    A subsequence is a sequence that can be derived from another sequence by 
    deleting zero or more elements without changing the order of the remaining elements.
    A palindrome reads the same forwards and backwards.

    Args:
        s (str): The input string to analyze.

    Returns:
        int: The length of the longest palindromic subsequence.

    Raises:
        TypeError: If the input is not a string.
    """
    # --- Input Validation ---
    if not isinstance(s, str):
        raise TypeError(f"Input must be a string, received {type(s).__name__}")

    # Handle the degenerate case of an empty string
    if not s:
        return 0

    # Pre-processing: The problem requirements imply we should treat spaces/punctuation
    # as characters since they are present in the assertions (e.g., "TENS FOR TENS").
    # We do not filter them out because they are part of the sequence structure.

    # --- Algorithm Selection ---
    # We use Dynamic Programming. 
    # Let DP[i][j] be the length of the longest palindromic subsequence 
    # in the substring s[i...j].

    # Base Cases:
    # 1. If i == j, DP[i][j] = 1 (a single character is a palindrome of length 1).
    # 2. If i > j, DP[i][j] = 0.

    # Recursive Step:
    # If s[i] == s[j]:
    #    DP[i][j] = DP[i+1][j-1] + 2
    # Else:
    #    DP[i][j] = max(DP[i+1][j], DP[i][j-1])

    n = len(s)

    # Initialize a 2D table with zeros.
    # dp[i][j] will store the LPS length for substring starting at index i and ending at j.
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the DP table
    # We iterate based on the length of the substring we are considering (from 1 to n).
    for current_length in range(1, n + 1):
        for i in range(n - current_length + 1):
            j = i + current_length - 1

            # Case: Substring of length 1
            if i == j:
                dp[i][j] = 1
            else:
                # Check if the characters at the boundaries match
                if s[i] == s[j]:
                    # If characters match, they contribute 2 to the length 
                    # of the LPS found in the inner substring s[i+1...j-1]
                    # If current_length is 2, dp[i+1][j-1] is naturally 0.
                    inner_lps_length = dp[i + 1][j - 1] if (i + 1 <= j - 1) else 0
                    dp[i][j] = inner_lps_length + 2
                else:
                    # If characters do not match, the LPS is the maximum 
                    # obtained by excluding either the first or the last character.
                    lps_excluding_first = dp[i + 1][j]
                    lps_excluding_last = dp[i][j - 1]

                    if lps_excluding_first > lps_excluding_last:
                        dp[i][j] = lps_excluding_first
                    else:
                        dp[i][j] = lps_excluding_last

    # The result for the full string is stored in the top-right corner of the matrix.
    return dp[0][n - 1]

if __name__ == "__main__":
    # Verification based on provided assertions
    assert lps("TENS FOR TENS") == 5
    assert lps("CARDIO FOR CARDS") == 7
    assert lps("PART OF THE JOURNEY IS PART") == 9