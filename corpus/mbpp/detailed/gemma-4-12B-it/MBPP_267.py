from typing import List

def square_Sum(n: int) -> int:
    """
    Calculates the sum of the squares of the first n odd natural numbers.

    Natural numbers are considered to be 1, 2, 3, ...
    Odd natural numbers are 1, 3, 5, 7, ...

    The formula for the k-th odd natural number is: 2k - 1.
    The function calculates: sum_{k=1}^{n} (2k - 1)^2.

    Args:
        n (int): The number of odd natural numbers to include in the sum.

    Returns:
        int: The sum of the squares of the first n odd natural numbers.

    Raises:
        ValueError: If n is not a non-negative integer.
        TypeError: If n is not an integer.
    """
    # Validate input type
    if not isinstance(n, int):
        raise TypeError(f"Input 'n' must be an integer, received {type(n).__name__}")

    # Validate input value (n must be non-negative)
    if n < 0:
        raise ValueError(f"Input 'n' must be a non-negative integer, received {n}")

    # Handle the edge case for zero
    if n == 0:
        return 0

    # To ensure production-grade robustness, we calculate the sum iteratively
    # to avoid floating point precision issues or large memory overhead of list generation.
    total_sum: int = 0

    # Iterate from 1 up to n (inclusive)
    # k represents the rank of the odd number (1st, 2nd, 3rd...)
    for k in range(1, n + 1):
        # Calculate the k-th odd natural number
        # 1st: 2(1)-1 = 1
        # 2nd: 2(2)-1 = 3
        # 3rd: 2(3)-1 = 5
        current_odd_number: int = (2 * k) - 1

        # Calculate the square of the current odd number
        square_value: int = current_odd_number * current_odd_number

        # Add to the running total
        total_sum += square_value

    return total_sum

# The assertions provided in the problem description:
# n=2: 1^2 + 3^2 = 1 + 9 = 10
# n=3: 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
# n=4: 1^2 + 3^2 + 5^2 + 7^2 = 1 + 9 + 25 + 49 = 84