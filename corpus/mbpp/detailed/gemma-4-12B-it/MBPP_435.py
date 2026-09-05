import math

def last_Digit(number: int) -> int:
    """
    Calculates the last digit of a given integer.

    The function handles positive integers, negative integers (returning 
    the absolute last digit), and zero. It includes robust input validation 
    to ensure the provided value is an integer.

    Args:
        number (int): The integer for which to find the last digit.

    Returns:
        int: The last digit of the number (always 0-9).

    Raises:
        TypeError: If the input is not an integer.
    """

    # 1. Input Validation
    # Ensure the input is strictly an integer type to prevent runtime errors
    # with non-numeric types or floats (which might have precision issues).
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer. Received: {type(number).__name__}")

    # 2. Handle the absolute value
    # The "last digit" of -123 is generally considered to be 3.
    # We work with the absolute value to ensure the modulo operation
    # behaves consistently across different programming environments.
    absolute_number = abs(number)

    # 3. Handle the degenerate case of zero
    # While the modulo logic works for 0, being explicit improves readability.
    if absolute_number == 0:
        return 0

    # 4. Extract the last digit
    # The last digit of a decimal number is the remainder when divided by 10.
    # For example:
    # 123 / 10 = 12 remainder 3
    # 25 / 10 = 2 remainder 5
    # 30 / 10 = 3 remainder 0
    last_digit = absolute_number % 10

    # 5. Final Verification
    # Ensure the result is within the expected bounds of a single digit.
    if not (0 <= last_digit <= 9):
        # This part is technically unreachable with % 10 on a positive int,
        # but serves as a defensive programming guard.
        raise ValueError("Calculation error: Resulting digit is out of bounds.")

    return last_digit

# Verification of requirements:
# assert last_Digit(123) == 3
# assert last_Digit(25) == 5
# assert last_Digit(30) == 0