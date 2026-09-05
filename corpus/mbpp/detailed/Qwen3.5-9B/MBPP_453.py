import math

def _is_even(n: int) -> bool:
    """
    Helper function to check if a number is even.

    Returns True if n is divisible by 2 without a remainder.
    Returns False otherwise.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is even, False otherwise.
    """
    return n % 2 == 0

def _find_factors(number: int) -> list[int]:
    """
    Helper function to find all positive factors of a given number.

    This function uses an efficient O(sqrt(n)) approach.
    It iterates from 1 up to the square root of the number.
    If a divisor is found, both the divisor and the quotient are added to the list.

    Args:
        number (int): A positive integer whose factors are to be found.

    Returns:
        list[int]: A sorted list of all unique positive factors of the number.
    """
    if number <= 0:
        # Should not happen based on validation in main function,
        # but good to handle defensively within helper if called externally.
        return []

    factors = []
    # We use integer square root logic.
    limit = int(math.isqrt(number))

    # Iterate from 1 up to and including the square root.
    for candidate in range(1, limit + 1):
        # Check if candidate is a divisor of number
        if number % candidate == 0:
            divisor = candidate
            quotient = number // divisor

            # Add the divisor
            factors.append(divisor)

            # Add the quotient if it's different from the divisor
            # (This handles perfect squares correctly without duplicates)
            if quotient != divisor:
                factors.append(quotient)

    # Sort the factors to ensure a deterministic order, though not strictly required for summation
    factors.sort()

    return factors

def _sum_even_items(items: list[int]) -> int:
    """
    Helper function to calculate the sum of items in a list that satisfy a condition (evenness).

    Args:
        items (list[int]): A list of integers.

    Returns:
        int: The sum of the even integers in the list.
    """
    total_sum = 0

    for item in items:
        if _is_even(item):
            total_sum += item

    return total_sum

def sumofFactors(number: int) -> int:
    """
    Calculates the sum of all even factors of a given positive integer.

    The function validates the input to ensure it is a positive integer.
    It then finds all factors, filters for even ones, and returns their sum.

    Args:
        number (int): The positive integer to analyze.

    Returns:
        int: The sum of the even factors.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is less than or equal to zero.
    """
    # Step 1: Input Validation

    # Check if the input is of integer type
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer, got {type(number).__name__}")

    # Check if the number is positive
    # Factors are traditionally defined for positive integers.
    if number <= 0:
        raise ValueError(f"Input must be a positive integer greater than 0, got {number}")

    # Step 2: Find all factors of the number
    all_factors = _find_factors(number)

    # Step 3: Filter for even factors
    even_factors = []
    for factor in all_factors:
        if _is_even(factor):
            even_factors.append(factor)

    # Step 4: Calculate the sum
    final_sum = _sum_even_items(even_factors)

    return final_sum