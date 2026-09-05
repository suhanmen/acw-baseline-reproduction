from typing import Any

def _is_positive_integer(value: Any) -> bool:
    """
    Check if the given value is a positive integer (strictly greater than zero).

    Args:
        value: The value to check.

    Returns:
        True if value is an integer and greater than zero, False otherwise.
    """
    if not isinstance(value, int):
        return False
    return value > 0

def _validate_input(value: Any, name: str) -> None:
    """
    Validate that the input is a positive integer.

    If the input is invalid, raises a TypeError with a descriptive message.
    This ensures robustness against non-integer inputs, zero, and negative numbers
    where the problem might imply strict positive integer constraints for certain
    edge cases (like empty digits or leading zeros in specific contexts, though
    mathematically integers handle negatives).

    Args:
        value: The value to validate.
        name: The name of the argument for the error message.

    Raises:
        TypeError: If the value is not a positive integer.
    """
    if not _is_positive_integer(value):
        raise TypeError(
            f"{name} must be a positive integer. "
            f"Received: {value!r} (type: {type(value).__name__})"
        )

def _get_unit_digit(number: int) -> int:
    """
    Extract the unit (last) digit of a positive integer.

    For a positive integer, the unit digit can be obtained by taking the number
    modulo 10.

    Args:
        number: A positive integer.

    Returns:
        The unit digit (0-9) of the number.
    """
    return number % 10

def multiply(a: int, b: int) -> int:
    """
    Complete the function that takes two integers and returns 
    the product of their unit digits.

    Although the docstring says "Assume the input is always valid", the defensive
    coding standard requires explicit validation to catch logical errors early
    and provide clear feedback. We will assume "valid" means positive integers
    based on the context of "unit digits" typically implying standard positive
    integer representation in such algorithmic puzzles, and handling negatives
    as per the mathematical definition (e.g., -15 has unit digit 5).

    However, to strictly follow "defensive, production-grade code" and "validate
    inputs", we check for integer type. The examples include negative numbers,
    so we will accept any integer but handle negative values by taking the absolute
    value of the unit digit extraction logic (since -15 % 10 is 5 in Python,
    which matches the expected result of 20 for 14 * 5).

    The requirement "Handle edge cases explicitly... zero / negative numbers"
    implies we must decide how to treat them.
    - Example: multiply(14,-15) -> 20. 
      Unit digit of 14 is 4. Unit digit of -15 is 5 (mathematically).
      4 * 5 = 20.
      In Python, -15 % 10 results in 5.
      So we can simply use modulo 10 on the absolute value or just the number
      if we rely on Python's modulo behavior for negatives yielding positive remainders.
      Let's verify: -15 % 10 -> 5. -14 % 10 -> 6. This works perfectly for Python.
      However, for zero: 0 % 10 -> 0.

    Steps:
    1. Validate that both inputs are integers.
    2. Extract the unit digit for 'a'.
    3. Extract the unit digit for 'b'.
    4. Calculate the product.
    5. Return the result.

    Note on "positive integer" constraint in _validate_input: 
    The examples show negative numbers (-15). Therefore, we should NOT restrict
    inputs to positive integers only. We must accept any integer (including 0 and negatives).
    We will adjust the validation to accept all integers (isinstance int) and handle
    the calculation safely.

    Revised Validation Logic for Final Implementation:
    - Check if inputs are of type `int`.
    - Do not restrict to > 0 because of the negative example.
    - Handle 0 naturally (unit digit is 0).
    - Handle negatives naturally using Python's modulo operator which returns
      a positive remainder for positive modulus.
    """

    # Step 1: Validate inputs are integers
    if not isinstance(a, int):
        raise TypeError(f"Argument 'a' must be an integer. Received: {type(a).__name__}")
    if not isinstance(b, int):
        raise TypeError(f"Argument 'b' must be an integer. Received: {type(b).__name__}")

    # Step 2: Extract unit digit for 'a'
    # Python's modulo operator handles negative numbers correctly for this purpose:
    # e.g., -15 % 10 == 5, -14 % 10 == 6, 14 % 10 == 4, 0 % 10 == 0
    unit_digit_a = a % 10

    # Step 3: Extract unit digit for 'b'
    unit_digit_b = b % 10

    # Step 4: Calculate the product
    product = unit_digit_a * unit_digit_b

    # Step 5: Return the result
    return product