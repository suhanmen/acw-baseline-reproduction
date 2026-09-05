from typing import List

def longest_common_subsequence(
    s1: str, 
    s2: str, 
    m: int, 
    n: int
) -> int:
    """
    Finds the length of the Longest Common Subsequence (LCS) between two strings.

    Args:
        s1: The first sequence as a string.
        s2: The second sequence as a string.
        m: The length of the first sequence.
        n: The length of the second sequence.

    Returns:
        The length of the longest common subsequence.

    Raises:
        ValueError: If input lengths do not match provided m or n.
        TypeError: If inputs are not of the expected types.
    """

    # --- Input Validation ---
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Both sequences must be provided as strings.")

    if not isinstance(m, int) or not isinstance(n, int):
        raise TypeError("Lengths m and n must be integers.")

    # Defensive check: Ensure provided lengths match actual string lengths
    if len(s1) != m:
        raise ValueError(f"Provided length m ({m}) does not match len(s1) ({len(s1)})")
    if len(s2) != n:
        raise ValueError(f"Provided length n ({n}) does not match len(s2) ({len(s2)})")

    # --- Edge Case Handling ---
    # If either string is empty, the LCS is 0
    if m == 0 or n == 0:
        return 0

    # --- Initialization ---
    # We use a 2D DP table where dp[i][j] represents the length of LCS
    # of s1[0...i-1] and s2[0...j-1].
    # The table size is (m+1) x (n+1) to accommodate the empty string case.
    dp_table: List[List[int]] = []

    for i in range(m + 1):
        # Initialize each row with zeros
        row = [0] * (n + 1)
        dp_table.append(row)

    # --- Dynamic Programming Logic ---
    # Iterate through each character of s1 and s2
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Characters are indexed at i-1 and j-1 in the strings
            char1: str = s1[i - 1]
            char2: str = s2[j - 1]

            if char1 == char2:
                # If characters match, the LCS length is 1 + LCS length 
                # of the sequences excluding these characters.
                previous_lcs_length = dp_table[i - 1][j - 1]
                dp_table[i][j] = previous_lcs_length + 1
            else:
                # If characters do not match, the LCS is the maximum of:
                # 1. LCS of s1 excluding the current character
                # 2. LCS of s2 excluding the current character
                option_skip_s1: int = dp_table[i - 1][j]
                option_skip_s2: int = dp_table[i][j - 1]

                if option_skip_s1 > option_skip_s2:
                    dp_table[i][j] = option_skip_s1
                else:
                    dp_table[i][j] = option_skip_s2

    # The result is stored in the bottom-right cell of the DP table
    final_lcs_length: int = dp_table[m][n]
    return final_lcs_length