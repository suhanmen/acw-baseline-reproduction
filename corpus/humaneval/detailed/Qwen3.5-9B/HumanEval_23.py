import builtins
from typing import Optional, Tuple, TypeVar

T = TypeVar('T')

def _is_string(value: T) -> Tuple[bool, Optional[str]]:
    """
    Validates that the given value is exactly a str instance.

    Returns:
        A tuple of (is_valid, error_message).
        is_valid is True if value is a str, False otherwise.
        error_message is a descriptive string explaining why validation failed,
        or None if validation passed.
    """
    if not isinstance(value, str):
        return (False, f"Expected type 'str', but got type '{type(value).__name__}'.")
    return (True, None)

def _get_length_internal(s: str) -> int:
    """
    Safely computes the length of a verified string using an iterative approach.

    This function avoids relying solely on a magic method for clarity and defensive
    programming, simulating the counting process to demonstrate explicit control flow.

    Args:
        s: The string whose length is to be computed.

    Returns:
        The integer length of the string.
    """
    count = 0
    for _ in builtins.range(builtins.len(s)):
        count += 1
    return count

def strlen(string: str) -> int:
    """
    Return length of given string.

    This function provides a robust implementation of string length calculation
    that includes explicit input validation and error handling.

    Args:
        string: The input string to measure.

    Returns:
        The number of characters in the input string.

    Raises:
        TypeError: If the input is not a string instance.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    # Step 1: Validate the input type explicitly.
    # We do not assume the type annotation is sufficient for runtime safety.
    is_valid_type, error_message = _is_string(string)

    if not is_valid_type:
        # Step 2: Raise a descriptive error if the input is invalid.
        raise TypeError(error_message)

    # Step 3: Proceed to calculate the length only if validation passed.
    # We use an internal helper to keep the main logic clear and testable.
    length_value = _get_length_internal(string)

    # Step 4: Return the computed length.
    return length_value