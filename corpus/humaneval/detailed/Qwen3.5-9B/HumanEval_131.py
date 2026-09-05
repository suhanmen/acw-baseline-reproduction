from typing import Optional, Union
from functools import reduce
import math


def _is_digit_character(char: str) -> bool:
    """
    Check if a single character is a valid decimal digit.

    Args:
        char: A single character string to check.

    Returns:
        True if the character is '0' through '9', False otherwise.
    """
    return char.isdigit()


def _extract_digit_value(char: str) -> Optional[int]:
    """
    Convert a single digit character to its integer value.

    Args:
        char: A single digit character string.

    Returns:
        The integer value of the digit (0-9), or None if the character
        is not a valid digit.
    """
    if not _is_digit_character(char):
        return None
    return int(char)


def _is_odd_number(number: int) -> bool:
    """
    Determine if an integer is odd.

    Args:
        number: The integer to check.

    Returns:
        True if the number is odd, False otherwise.
    """
    return number % 2 != 0


def _convert_integer_to_string(number: int) -> str:
    """
    Convert a positive integer to its string representation without sign.

    Args:
        number: A positive integer.

    Returns:
        A string containing the decimal digits of the number.
    """
    # We use string formatting to ensure we get the canonical decimal representation
    return str(number)


def _compute_product_of_numbers(numbers: list[int]) -> int:
    """
    Compute the product of a list of integers.

    Args:
        numbers: A list of integers to multiply.

    Returns:
        The product of all integers in the list.
        If the list is empty, returns 1 (multiplicative identity).
    """
    if not numbers:
        return 1

    result = 1
    for num in numbers:
        result *= num
    return result


def _contains_odd_digit(digit_values: list[int]) -> bool:
    """
    Check if a list of digit values contains at least one odd number.

    Args:
        digit_values: A list of integers representing digit values (0-9).

    Returns:
        True if at least one digit is odd, False otherwise.
    """
    for digit in digit_values:
        if _is_odd_number(digit):
            return True
    return False


def digits(n: int) -> int:
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Step 1: Validate input type
    if not isinstance(n, int):
        raise TypeError(
            f"Input must be an integer, but received type '{type(n).__name__}'"
        )

    # Step 2: Validate input value range
    # The problem specifies a "positive integer".
    if n <= 0:
        raise ValueError(
            f"Input must be a positive integer (greater than 0), but received: {n}"
        )

    # Step 3: Convert the integer to a string to access individual digits
    number_string = _convert_integer_to_string(n)

    # Step 4: Validate that the string representation consists only of digits
    # (This is technically redundant if input is a valid positive int,
    # but serves as a defensive check against unexpected internal states)
    if not number_string:
        raise ValueError("Input integer resulted in an empty string representation.")

    for char in number_string:
        if not _is_digit_character(char):
            raise ValueError(
                f"Invalid character found in integer representation: '{char}'"
            )

    # Step 5: Extract individual digit characters from the string
    digit_characters = list(number_string)

    # Step 6: Convert digit characters to integer values
    digit_values = []
    for char in digit_characters:
        value = _extract_digit_value(char)
        if value is None:
            # This should theoretically not be reached given prior validation
            raise ValueError(f"Failed to convert valid digit character to value: '{char}'")
        digit_values.append(value)

    # Step 7: Filter the list to keep only odd digits
    odd_digit_values = []
    for value in digit_values:
        if _is_odd_number(value):
            odd_digit_values.append(value)

    # Step 8: Determine the result based on whether any odd digits were found
    if not odd_digit_values:
        # If the list of odd digits is empty, return 0 as per requirements
        return 0

    # Step 9: Compute the product of the odd digits
    product_result = _compute_product_of_numbers(odd_digit_values)

    return product_result