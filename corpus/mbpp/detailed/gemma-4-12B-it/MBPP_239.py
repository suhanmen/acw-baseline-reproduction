from typing import List

def get_total_number_of_sequences(n: int, m: int) -> int:
    """
    Finds the number of sequences of length n such that:
    1. Each element a_i is in the range [1, m].
    2. For i > 1, a_i >= 2 * a_{i-1}.
    3. For i > 1, a_i <= m.

    Args:
        n: The length of the sequence.
        m: The maximum possible value for any element in the sequence.

    Returns:
        The total count of valid sequences.
    """
    # --- Input Validation ---
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError("Both n and m must be integers.")

    if n < 0:
        raise ValueError("Sequence length n must be non-negative.")

    if m < 0:
        raise ValueError("Maximum value m must be non-negative.")

    # --- Edge Case Handling ---
    # A sequence of length 0 is technically 1 empty sequence.
    if n == 0:
        return 1

    # A sequence of length 1 can be any integer from 1 to m.
    # If m is 0, and n > 0, no such sequence exists.
    if n == 1:
        return max(0, m)

    if m <= 0:
        # If m is 0 or less, and n >= 1, no positive integers exist.
        # The problem implies positive integers based on the logic of 
        # "greater than or equal to twice", but if m=0 is allowed,
        # a sequence of 0s could be argued. However, standard 
        # sequence problems like this imply a positive range.
        # Given the test cases, m is at least 2.
        return 0

    # --- Dynamic Programming Approach ---
    # We need to count sequences a_1, a_2, ..., a_n.
    # Let dp[i][v] be the number of valid sequences of length i
    # ending with the value v.

    # Since we only need the previous length's results to calculate the 
    # current length, we can optimize space to use two rows.

    # dp_prev[v] = number of valid sequences of length (k-1) ending in v.
    # Initialize for length 1: every value from 1 to m is a valid sequence of length 1.
    dp_prev = [0] * (m + 1)
    for v in range(1, m + 1):
        dp_prev[v] = 1

    # Iterate to build sequences up to length n
    for length in range(2, n + 1):
        dp_current = [0] * (m + 1)

        # For each possible value v at the current position
        for v in range(1, m + 1):
            # The previous value u must satisfy:
            # 1. u * 2 <= v  =>  u <= v // 2
            # 2. u >= 1
            max_prev_val = v // 2

            if max_prev_val >= 1:
                # The number of sequences of length (length-1) ending in 
                # any u such that 1 <= u <= max_prev_val.
                # We sum dp_prev[1] + dp_prev[2] + ... + dp_prev[max_prev_val].
                current_count = 0
                for u in range(1, max_prev_val + 1):
                    current_count += dp_prev[u]

                dp_current[v] = current_count
            else:
                # If v // 2 < 1, no valid previous value exists.
                dp_current[v] = 0

        # Update dp_prev for the next iteration
        dp_prev = dp_current

    # The answer is the sum of all sequences of length n ending in any value v from 1 to m.
    total_sequences = 0
    for v in range(1, m + 1):
        total_sequences += dp_prev[v]

    return total_sequences