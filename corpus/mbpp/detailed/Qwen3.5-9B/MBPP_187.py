def longest_common_subsequence(sequence_a: str, sequence_b: str, len_a: int, len_b: int) -> str:
    """
    Finds and returns the Longest Common Subsequence (LCS) for two input strings.

    This function implements the standard dynamic programming approach for LCS,
    constructing a 2D table where dp[i][j] represents the length of the LCS
    of sequence_a[0:i] and sequence_b[0:j]. After building the table, it traces
    back from dp[len_a][len_b] to reconstruct the actual subsequence string.

    Parameters:
    sequence_a (str): The first input sequence.
    sequence_b (str): The second input sequence.
    len_a (int): The length of sequence_a. Expected to be len(sequence_a).
    len_b (int): The length of sequence_b. Expected to be len(sequence_b).

    Returns:
    str: The longest common subsequence as a string.

    Raises:
    TypeError: If sequences are not strings or lengths are not integers.
    ValueError: If lengths do not match the actual sequence lengths or lengths are negative.
    """

    # --- Input Validation Phase ---

    # Validate types for sequences
    if not isinstance(sequence_a, str):
        raise TypeError(f"sequence_a must be a string, got {type(sequence_a).__name__}")
    if not isinstance(sequence_b, str):
        raise TypeError(f"sequence_b must be a string, got {type(sequence_b).__name__}")

    # Validate types for lengths
    if not isinstance(len_a, int):
        raise TypeError(f"len_a must be an integer, got {type(len_a).__name__}")
    if not isinstance(len_b, int):
        raise TypeError(f"len_b must be an integer, got {type(len_b).__name__}")

    # Validate length values are non-negative
    if len_a < 0:
        raise ValueError(f"len_a cannot be negative. Got {len_a}")
    if len_b < 0:
        raise ValueError(f"len_b cannot be negative. Got {len_b}")

    # Validate lengths match actual string lengths
    if len(sequence_a) != len_a:
        raise ValueError(f"Provided len_a ({len_a}) does not match actual length of sequence_a ({len(sequence_a)})")
    if len(sequence_b) != len_b:
        raise ValueError(f"Provided len_b ({len_b}) does not match actual length of sequence_b ({len(sequence_b)})")

    # --- Edge Case Handling ---

    # Handle empty input cases explicitly
    # If either sequence is empty, the LCS length is 0, and the result is an empty string.
    if len_a == 0 or len_b == 0:
        return ""

    # Handle single element cases
    if len_a == 1 and len_b == 1:
        if sequence_a[0] == sequence_b[0]:
            return sequence_a[0]
        else:
            return ""

    # Handle cases where one sequence is a subset of length 1 and the other is longer
    # (Logically covered by the DP, but we ensure the DP matrix dimensions are correct)
    # No special short-circuit needed for single elements beyond the check above,
    # as the DP algorithm naturally handles it.

    # --- Dynamic Programming Table Initialization ---

    # Initialize a 2D list (matrix) with dimensions (len_a + 1) x (len_b + 1).
    # Rows correspond to indices of sequence_a (0 to len_a).
    # Columns correspond to indices of sequence_b (0 to len_b).
    # All cells initialized to 0.
    dp_matrix = []

    for row_index in range(len_a + 1):
        row = []
        for col_index in range(len_b + 1):
            row.append(0)
        dp_matrix.append(row)

    # --- Dynamic Programming Calculation Phase ---

    # Iterate through the table to fill it based on the recurrence relation:
    # dp[i][j] = dp[i-1][j-1] + 1 if sequence_a[i-1] == sequence_b[j-1]
    # dp[i][j] = max(dp[i-1][j], dp[i][j-1]) otherwise

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            char_a = sequence_a[i - 1]
            char_b = sequence_b[j - 1]

            if char_a == char_b:
                # Characters match: extend the LCS found so far diagonally
                current_value = dp_matrix[i - 1][j - 1] + 1
                dp_matrix[i][j] = current_value
            else:
                # Characters do not match: take the maximum of excluding current char from A or B
                value_excluding_b = dp_matrix[i - 1][j]
                value_excluding_a = dp_matrix[i][j - 1]

                if value_excluding_b > value_excluding_a:
                    dp_matrix[i][j] = value_excluding_b
                else:
                    dp_matrix[i][j] = value_excluding_a

    # --- Reconstruction Phase ---

    # Start from the bottom-right corner of the matrix
    i = len_a
    j = len_b
    reconstructed_sequence_chars = []

    # Traverse backwards to reconstruct the string
    while i > 0 and j > 0:
        current_char_a = sequence_a[i - 1]
        current_char_b = sequence_b[j - 1]

        if current_char_a == current_char_b:
            # This character is part of the LCS
            reconstructed_sequence_chars.append(current_char_a)
            i -= 1
            j -= 1
        else:
            # Move in the direction of the larger value
            value_from_top = dp_matrix[i - 1][j]
            value_from_left = dp_matrix[i][j - 1]

            if value_from_top >= value_from_left:
                # Move up (exclude current char from sequence_a)
                i -= 1
            else:
                # Move left (exclude current char from sequence_b)
                j -= 1

    # The characters were collected in reverse order (last to first)
    # Reverse the list to get the correct chronological order
    reconstructed_sequence_chars.reverse()

    # Join the characters to form the final string
    final_lcs_string = "".join(reconstructed_sequence_chars)

    return final_lcs_string