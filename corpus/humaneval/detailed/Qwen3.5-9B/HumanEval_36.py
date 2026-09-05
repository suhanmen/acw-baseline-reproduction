import re
from typing import List, Set

def _count_sevens_in_number(number: int) -> int:
    """
    Counts the number of times the digit 7 appears in the decimal representation of a given non-negative integer.
    Returns 0 if the number is 0 (which has no digit 7).
    """
    if number < 0:
        raise ValueError(f"Number cannot be negative: {number}")

    if number == 0:
        return 0

    number_str = str(number)
    return number_str.count('7')


def _get_relevant_numbers(n: int) -> List[int]:
    """
    Generates a list of integers strictly less than n that are divisible by 11 or 13.
    """
    relevant_numbers: List[int] = []

    # Handle edge case where n is non-positive
    if n <= 0:
        return relevant_numbers

    # We iterate from 1 up to n-1
    current: int = 1
    limit: int = n - 1

    while current <= limit:
        if current % 11 == 0 or current % 13 == 0:
            relevant_numbers.append(current)
        current += 1

    return relevant_numbers


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Input Validation
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received type: {type(n).__name__}")

    # Handle boundary case: n <= 0
    # There are no positive integers less than or equal to 0.
    if n <= 0:
        return 0

    # Step 1: Identify all valid integers (divisible by 11 or 13 and less than n)
    relevant_numbers: List[int] = _get_relevant_numbers(n)

    # Step 2: Count occurrences of the digit 7 in each identified number
    total_sevens_count: int = 0
    seven_count_for_number: int = 0

    for number in relevant_numbers:
        seven_count_for_number = _count_sevens_in_number(number)
        total_sevens_count += seven_count_for_number

    return total_sevens_count