import math
from typing import List

def is_even_number(n: int) -> bool:
    """
    Checks if a given integer is even.

    Args:
        n: The integer to check.

    Returns:
        True if the number is even, False otherwise.
    """
    return n % 2 == 0

def get_all_factors(number: int) -> List[int]:
    """
    Finds all positive integer factors of a given number.

    Args:
        number: The integer to find factors for.

    Returns:
        A list of all unique factors of the number.
    """
    factors = []

    # Handle the edge case of numbers less than 1
    if number < 1:
        return factors

    # We iterate up to the square root of the number to find factors efficiently.
    # For every 'i' that divides 'number', both 'i' and 'number / i' are factors.
    limit = int(math.isqrt(number))

    for i in range(1, limit + 1):
        if number % i == 0:
            factors.append(i)

            # Check if the quotient is different from the divisor to avoid 
            # duplicating the square root in the case of perfect squares.
            quotient = number // i
            if quotient != i:
                factors.append(quotient)

    # Sort the factors for deterministic behavior, though not strictly necessary for summation.
    factors.sort()
    return factors

def sumofFactors(number: int) -> int:
    """
    Calculates the sum of all even factors of a given integer.

    Args:
        number: The integer to evaluate.

    Returns:
        The sum of all even factors.

    Raises:
        ValueError: If the input is not an integer.
        TypeError: If the input is not of type int.
    """
    # Input Validation: Ensure the input is an integer.
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer. Received: {type(number).__name__}")

    # Handle negative numbers or zero.
    # Factors are typically defined for positive integers in this context.
    # If number is 0, it has infinite factors; if negative, we treat it by its absolute value.
    if number == 0:
        # Mathematically, 0 has infinite factors, but for this logic, 
        # we treat it as having no sum of even factors or return 0.
        return 0

    # Work with the absolute value to handle negative integers.
    working_number = abs(number)

    # Step 1: Retrieve all factors of the absolute value of the input.
    all_factors = get_all_factors(working_number)

    # Step 2: Filter the list to keep only even factors.
    even_factors = []
    for factor in all_factors:
        if is_even_number(factor):
            even_factors.append(factor)

    # Step 3: Calculate the sum of the filtered list.
    result_sum = sum(even_factors)

    return result_sum