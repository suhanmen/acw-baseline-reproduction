import typing

def get_pell(n: int) -> int:
    """
    Calculates the nth Pell number.

    The Pell numbers are a sequence of integers defined by the recurrence relation:
    P(0) = 0
    P(1) = 1
    P(n) = 2 * P(n-1) + P(n-2) for n > 1

    Args:
        n (int): The index of the Pell number to retrieve. 
                 Must be a non-negative integer.

    Returns:
        int: The nth Pell number.

    Raises:
        ValueError: If n is a negative integer.
        TypeError: If n is not an integer.
    """

    # --- Input Validation ---
    # Ensure the input type is strictly an integer.
    if not isinstance(n, int):
        raise TypeError(f"Input 'n' must be an integer, received {type(n).__name__}.")

    # Ensure the input is non-negative, as Pell numbers are defined for n >= 0.
    if n < 0:
        raise ValueError(f"Input 'n' must be a non-negative integer, received {n}.")

    # --- Base Case Handling ---
    # P(0) is defined as 0.
    if n == 0:
        return 0

    # P(1) is defined as 1.
    if n == 1:
        return 1

    # --- Iterative Calculation ---
    # We use an iterative approach to ensure O(n) time complexity and O(1) space complexity.
    # This avoids the exponential complexity of a naive recursive solution.

    # Initialize the first two Pell numbers.
    # previous_pell represents P(i-2)
    # current_pell represents P(i-1)
    previous_pell: int = 0  # P(0)
    current_pell: int = 1    # P(1)

    # We start calculating from n = 2 up to the target index n.
    for i in range(2, n + 1):
        # Formula: P(i) = 2 * P(i-1) + P(i-2)
        next_pell: int = (2 * current_pell) + previous_pell

        # Update variables for the next iteration.
        # The old current becomes the new previous.
        previous_pell = current_pell
        # The newly calculated value becomes the current.
        current_pell = next_pell

    return current_pell

if __name__ == "__main__":
    # The following are the assertions provided in the problem description.
    assert get_pell(4) == 12
    assert get_pell(7) == 169
    assert get_pell(8) == 408