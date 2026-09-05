from typing import List

def find_longest_repeating_subseq(s: str) -> int:
    """
    Finds the length of the longest repeating subsequence in a given string.
    A repeating subsequence is a subsequence that appears at least twice 
    in the string such that the characters in the two subsequences 
    do not occupy the same indices in the original string.

    This is equivalent to finding the Longest Common Subsequence (LCS) 
    of the string with itself, with the added constraint that 
    the indices of the characters used from the string must be different.
    """
    # Input Validation: Check if input is a string
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")

    # Handle edge cases: empty string or single character
    # An empty string or a string of length 1 cannot have a repeating 
    # subsequence with distinct indices.
    if len(s) <= 1:
        return 0

    # Convert the string to a list of characters for easier processing
    # though string indexing works fine in Python.
    char_list = list(s)
    n = len(char_list)

    # We use Dynamic Programming to solve the LCS variant.
    # Let dp[i][j] be the length of the longest repeating subsequence
    # using characters from s[0...i-1] and s[0...j-1].

    # Initialize a 2D DP table with dimensions (n+1) x (n+1)
    # dp[i][j] will store the length of LCS for s[0...i-1] and s[0...j-1]
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Build the DP table
    # i represents the index in the first instance of the string
    # j represents the index in the second instance of the string
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Condition: characters match AND indices are different.
            # This ensures that the subsequence is "repeating" at different 
            # positions in the original string.
            char_at_i = char_list[i - 1]
            char_at_j = char_list[j - 1]

            if char_at_i == char_at_j and i != j:
                # If characters match and are at different positions,
                # increment the length from the previous diagonal.
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If they don't match or are at the same position,
                # take the maximum of excluding one character from either sequence.
                option_1 = dp[i - 1][j]
                option_2 = dp[i][j - 1]

                if option_1 > option_2:
                    dp[i][j] = option_1
                else:
                    dp[i][j] = option_2

    # The result is the value in the bottom-right cell of the DP table.
    result = dp[n][n]
    return result