from typing import Tuple, Union

def _is_digit_even(digit_char: str) -> bool:
    """
    Determines if a single character representing a digit is even.

    Args:
        digit_char: A single character string representing a digit (e.g., '0', '5').

    Returns:
        True if the digit is even, False otherwise.
    """
    try:
        digit_value = int(digit_char)
    except ValueError:
        # This should not happen if the caller guarantees digit characters
        return False

    return digit_value % 2 == 0

def _extract_digits(n: int) -> list:
    """
    Extracts all digits from an integer as a list of strings.
    Handles negative numbers by ignoring the sign.

    Args:
        n: An integer.

    Returns:
        A list of strings, each representing a digit of the number.
    """
    # Handle zero explicitly to ensure it returns ['0'] and not an empty list
    if n == 0:
        return ['0']

    # Convert absolute value to string to remove negative sign
    # Using absolute value ensures -12 becomes "12"
    number_string = str(abs(n))

    # Convert each character to a list element
    digits_list = list(number_string)

    return digits_list

def _count_evens_and_odds(digits: list) -> Tuple[int, int]:
    """
    Counts the number of even and odd digits in a list of digit characters.

    Args:
        digits: A list of strings, where each string is a single digit.

    Returns:
        A tuple (even_count, odd_count).
    """
    even_count = 0
    odd_count = 0

    for digit_char in digits:
        # Validate that we are processing a digit character
        if not digit_char.isdigit():
            raise ValueError(f"Invalid digit character encountered: '{digit_char}'")

        is_even = _is_digit_even(digit_char)

        if is_even:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)

def even_odd_count(num: int) -> Tuple[int, int]:
    """
    Given an integer, return a tuple that has the number of even and odd digits respectively.

    This function validates the input type, handles negative numbers by ignoring the sign,
    processes each digit to determine if it is even or odd, and counts the occurrences.

    Args:
        num: An integer input.

    Returns:
        A tuple (even_count, odd_count) where even_count is the number of even digits
        and odd_count is the number of odd digits.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is not a valid finite integer.

    Examples:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
        even_odd_count(0) ==> (1, 0)
    """
    # Step 1: Input Validation
    # Check if the input is an instance of int
    if not isinstance(num, int):
        raise TypeError(f"Input must be an integer, got {type(num).__name__}")

    # Check for NaN (though int type usually excludes float, it's safe to check for infinity if mixed)
    # Note: In Python, int cannot be NaN or Inf, but explicit check doesn't hurt if input was loose
    # However, since we checked isinstance(num, int), num cannot be float('nan') or float('inf').

    # Step 2: Extract Digits
    digits = _extract_digits(num)

    # Step 3: Count Evens and Odds
    even_count, odd_count = _count_evens_and_odds(digits)

    # Step 4: Return Result
    return (even_count, odd_count)