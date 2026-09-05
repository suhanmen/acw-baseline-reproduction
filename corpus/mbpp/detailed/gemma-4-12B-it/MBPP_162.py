from typing import List

def sum_series(n: int) -> int:
    """
    Calculates the sum of the positive integers of the sequence 
    n + (n-2) + (n-4) + ... until the next term is <= 0.

    Example:
    If n = 6: 6 + 4 + 2 = 12
    If n = 10: 10 + 8 + 6 + 4 + 2 = 30
    If n = 9: 9 + 7 + 5 + 3 + 1 = 25
    """
    # Input Validation: Check if input is an integer
    if not isinstance(n, int):
        raise TypeError(f"Input 'n' must be an integer. Received: {type(n).__name__}")

    # Handling edge cases for non-positive integers
    # The series is defined by positive integers; if n <= 0, the sum is 0.
    if n <= 0:
        return 0

    total_sum = 0
    current_term = n

    # We iterate as long as the current term is strictly greater than zero.
    # The problem specifies "until n-x <= 0", which means the last 
    # term included is the smallest positive integer in the sequence.
    while current_term > 0:
        # Defensive check: ensure total_sum doesn't overflow (Python handles
        # large ints automatically, but it's good practice to keep logic clear)
        total_sum += current_term

        # Move to the next term in the sequence (decrement by 2)
        current_term -= 2

    return total_sum

if __name__ == "__main__":
    # Test cases provided in the problem description
    assert sum_series(6) == 12
    assert sum_series(10) == 30
    assert sum_series(9) == 25

    # Additional edge case testing
    assert sum_series(1) == 1
    assert sum_series(2) == 2
    assert sum_series(0) == 0
    assert sum_series(-5) == 0