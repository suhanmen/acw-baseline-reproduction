from typing import List

def sum_difference(n: int) -> int:
    """
    Calculates the difference between the square of the sum of the first n 
    natural numbers and the sum of the squares of the first n natural numbers.

    Formula: (1 + 2 + ... + n)^2 - (1^2 + 2^2 + ... + n^2)

    Args:
        n (int): The upper limit of the natural numbers to consider.

    Returns:
        int: The calculated difference.

    Raises:
        ValueError: If n is not a non-negative integer.
        TypeError: If n is not an integer.
    """
    # Input Validation
    if not isinstance(n, int):
        raise TypeError(f"Input n must be an integer. Received: {type(n).__name__}")

    if n < 0:
        raise ValueError(f"Input n must be a non-negative integer. Received: {n}")

    # Handle edge cases for 0 and 1
    # For n=0, sums are 0, difference is 0.
    # For n=1, (1)^2 - (1^2) = 0.
    if n == 0:
        return 0
    if n == 1:
        return 0

    # Step 1: Calculate the sum of the first n natural numbers
    # Sum = 1 + 2 + ... + n
    # Using the arithmetic series formula: n * (n + 1) / 2
    sum_of_numbers = 0
    for i in range(1, n + 1):
        sum_of_numbers += i

    # Step 2: Calculate the square of that sum
    squared_sum = sum_of_numbers ** 2

    # Step 3: Calculate the sum of the squares of the first n natural numbers
    # Sum = 1^2 + 2^2 + ... + n^2
    # Using the square pyramidal number formula: n * (n + 1) * (2n + 1) / 6
    # However, we will iterate to ensure clarity and avoid floating point issues
    sum_of_squares = 0
    for i in range(1, n + 1):
        square_value = i * i
        sum_of_squares += square_value

    # Step 4: Calculate the final difference
    # Difference = (Sum of first n)^2 - (Sum of squares of first n)
    result_difference = squared_sum - sum_of_squares

    return result_difference

if __name__ == "__main__":
    # Verification based on provided assertions
    assert sum_difference(12) == 5434
    assert sum_difference(20) == 41230
    assert sum_difference(54) == 2151270