from typing import List

def get_Min_Squares(n: int) -> int:
    """
    Finds the minimum number of perfect squares that sum up to a given integer n.

    This problem is a variation of the change-making problem and can be solved
    efficiently using Dynamic Programming or Breadth-First Search.
    Given the requirement for production-grade code, we implement a Dynamic 
    Programming approach to ensure we find the global minimum.

    Args:
        n (int): The target integer to decompose into squares.

    Returns:
        int: The minimum number of perfect squares.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # --- Input Validation ---
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer. Received: {type(n).__name__}")

    if n < 0:
        raise ValueError(f"Input must be a non-negative integer. Received: {n}")

    # --- Edge Cases ---
    # If the number is 0, the minimum number of squares is 0.
    if n == 0:
        return 0

    # --- Initialization ---
    # We use a DP table where dp[i] represents the minimum number of 
    # squares that sum up to integer i.
    # We initialize the table with a value larger than any possible answer.
    # Since the worst case is n = 1^2 + 1^2 + ... + 1^2 (n times), 
    # n + 1 is a safe "infinity".
    dp_table: List[int] = [0] * (n + 1)
    for i in range(1, n + 1):
        dp_table[i] = n + 1

    # Base case: 0 requires 0 squares.
    dp_table[0] = 0

    # --- Core Logic ---
    # Pre-calculate all possible perfect squares less than or equal to n.
    # This prevents repeated square root calculations in the inner loop.
    max_root = int(n**0.5)
    perfect_squares: List[int] = []
    for i in range(1, max_root + 1):
        perfect_squares.append(i * i)

    # Fill the DP table
    # For every number i from 1 to n:
    for i in range(1, n + 1):
        # Check every perfect square j that is less than or equal to i
        for square in perfect_squares:
            if square > i:
                # Since perfect_squares is sorted, we can break early
                break

            # The recurrence relation:
            # To reach i, we can take the square 'square' and add 1 to 
            # the result of (i - square).
            previous_value = dp_table[i - square]
            current_count = 1 + previous_value

            if current_count < dp_table[i]:
                dp_table[i] = current_count

    result = dp_table[n]

    # Double check for safety, though logic guarantees result <= n for n > 0
    if result > n:
        return 0

    return result

# The following assertions verify the logic against the provided requirements.
if __name__ == "__main__":
    assert get_Min_Squares(6) == 3   # 4 + 1 + 1
    assert get_Min_Squares(2) == 2   # 1 + 1
    assert get_Min_Squares(4) == 1   # 4