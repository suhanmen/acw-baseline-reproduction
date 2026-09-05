from typing import Dict

def get_perrin(n: int) -> int:
    """
    Calculates the n'th Perrin number using a recursive approach with memoization.

    The Perrin sequence is defined by the recurrence relation:
    P(n) = P(n-2) + P(n-3)
    With initial values:
    P(0) = 3
    P(1) = 0
    P(2) = 2

    Args:
        n (int): The index of the Perrin number to retrieve (non-negative integer).

    Returns:
        int: The n'th Perrin number.

    Raises:
        ValueError: If n is a negative integer.
        TypeError: If n is not an integer.
    """

    # Input Validation: Ensure n is an integer
    if not isinstance(n, int):
        raise TypeError(f"Input n must be an integer. Received: {type(n).__name__}")

    # Input Validation: Ensure n is non-negative
    if n < 0:
        raise ValueError(f"Input n must be a non-negative integer. Received: {n}")

    # Memoization dictionary to store results and optimize recursive calls
    # This prevents the O(2^n) exponential complexity of naive recursion
    memo: Dict[int, int] = {}

    def _recursive_perrin(current_n: int) -> int:
        """
        Internal helper function to perform the recursive calculation
        with memoization to ensure efficiency.
        """
        # Base Case: P(0) = 3
        if current_n == 0:
            return 3

        # Base Case: P(1) = 0
        if current_n == 1:
            return 0

        # Base Case: P(2) = 2
        if current_n == 2:
            return 2

        # Check if value was already calculated
        if current_n in memo:
            return memo[current_n]

        # Recursive step: P(n) = P(n-2) + P(n-3)
        # We compute the components separately to maintain clarity
        term_minus_2 = _recursive_perrin(current_n - 2)
        term_minus_3 = _recursive_perrin(current_n - 3)

        result = term_minus_2 + term_minus_3

        # Store result in memo before returning
        memo[current_n] = result
        return result

    # Execute the recursion
    final_result = _recursive_perrin(n)
    return final_result

# Validation of the provided requirements
if __name__ == "__main__":
    # These assertions confirm the logic meets the specific problem requirements.
    assert get_perrin(9) == 12
    assert get_perrin(4) == 2
    assert get_perrin(6) == 5