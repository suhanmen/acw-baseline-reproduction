from typing import List

def get_divisors_sum(n: int) -> int:
    """
    Calculates the sum of all proper divisors of a positive integer n.
    Proper divisors are all positive integer divisors of n excluding n itself.

    Args:
        n: The integer to evaluate.

    Returns:
        The sum of the proper divisors.

    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input: Problem context implies natural numbers.
    # Divisors are typically defined for positive integers.
    if not isinstance(n, int):
        raise ValueError(f"Input must be an integer, got {type(n).__name__}")

    if n <= 0:
        raise ValueError(f"Input must be a positive integer, got {n}")

    # Special case: 1 has no proper divisors less than itself.
    if n == 1:
        return 0

    divisor_sum = 0

    # We only need to iterate up to the square root of n.
    # If i is a divisor, then n/i is also a divisor.
    limit = int(n**0.5)

    for i in range(1, limit + 1):
        if n % i == 0:
            # i is a divisor.
            # Check if it's a proper divisor (i < n).
            if i < n:
                divisor_sum += i

            # Find the corresponding divisor pair: n / i.
            paired_divisor = n // i

            # Ensure we don't count the same divisor twice (e.g., 6*6 = 36).
            # Also ensure we don't count n itself as a proper divisor.
            if paired_divisor != i and paired_divisor < n:
                divisor_sum += paired_divisor

    return divisor_sum

def areEquivalent(num1: int, num2: int) -> bool:
    """
    Checks whether the sum of proper divisors of two integers are the same.

    Args:
        num1: First integer.
        num2: Second integer.

    Returns:
        True if the sum of divisors are equal, False otherwise.

    Raises:
        ValueError: If inputs are not valid positive integers.
    """
    # Validate inputs before processing
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Both arguments must be integers.")

    if num1 <= 0 or num2 <= 0:
        raise ValueError("Both arguments must be positive integers.")

    # Step 1: Calculate sum of divisors for the first number
    sum1 = get_divisors_sum(num1)

    # Step 2: Calculate sum of divisors for the second number
    sum2 = get_divisors_sum(num2)

    # Step 3: Compare results
    is_equal = (sum1 == sum2)

    return is_equal

# The assertions provided in the problem:
# 36: divisors are 1, 2, 3, 4, 6, 9, 12, 18. Sum = 55
# 57: divisors are 1, 3, 19. Sum = 23
# areEquivalent(36, 57) -> 55 == 23 -> False

# 2: divisors are 1. Sum = 1
# 4: divisors are 1, 2. Sum = 3
# areEquivalent(2, 4) -> 1 == 3 -> False

# 23: divisor is 1. Sum = 1
# 47: divisor is 1. Sum = 1
# areEquivalent(23, 47) -> 1 == 1 -> True