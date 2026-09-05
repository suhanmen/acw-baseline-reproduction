from typing import List

def find_lucas(n: int) -> int:
    """
    Calculates the n'th Lucas number.

    The Lucas sequence is defined as:
    L(0) = 2
    L(1) = 1
    L(n) = L(n-1) + L(n-2) for n > 1

    Args:
        n (int): The index of the Lucas number to retrieve.

    Returns:
        int: The n'th Lucas number.

    Raises:
        ValueError: If n is a negative integer.
        TypeError: If n is not an integer.
    """

    # Validate the input type
    if not isinstance(n, int):
        raise TypeError(f"Input n must be an integer. Received: {type(n).__name__}")

    # Validate the input value (Lucas numbers are typically defined for n >= 0)
    if n < 0:
        raise ValueError(f"Input n must be a non-negative integer. Received: {n}")

    # Handle the base cases explicitly
    if n == 0:
        return 2

    if n == 1:
        return 1

    # Use an iterative approach to calculate the n'th Lucas number.
    # This provides O(n) time complexity and O(1) space complexity,
    # which is more efficient than recursion for large n.

    # current_prev represents L(i-2)
    # current represents L(i-1)
    current_prev: int = 2  # L(0)
    current: int = 1        # L(1)

    # We start calculating from L(2) up to L(n)
    for i in range(2, n + 1):
        # Calculate the next number in the sequence
        next_lucas: int = current_prev + current

        # Update the variables for the next iteration
        current_prev = current
        current = next_lucas

    return current

if __name__ == "__main__":
    # The assertions provided in the problem description
    assert find_lucas(9) == 76
    assert find_lucas(4) == 7
    assert find_lucas(3) == 4