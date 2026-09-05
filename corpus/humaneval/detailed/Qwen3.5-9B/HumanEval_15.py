from typing import Optional

def _validate_input(n: int) -> None:
    """
    Validates the input integer n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected an integer, got {type(n).__name__}")

    if n < 0:
        raise ValueError(f"Expected a non-negative integer, got {n}")

def _generate_number_sequence(start: int, end: int) -> list:
    """
    Generates a list of integers starting from 'start' up to and including 'end'.

    Args:
        start: The starting integer.
        end: The ending integer (inclusive).

    Returns:
        A list of integers.

    Raises:
        ValueError: If start is greater than end.
    """
    if start > end:
        raise ValueError(f"Start value {start} cannot be greater than end value {end}")

    sequence = []
    current = start
    while current <= end:
        sequence.append(current)
        current += 1
    return sequence

def _format_sequence(sequence: list) -> str:
    """
    Formats a list of integers into a single string with space delimiters.

    Args:
        sequence: The list of integers to format.

    Returns:
        A string with elements separated by single spaces.
    """
    if not sequence:
        return ""

    string_parts = []
    for number in sequence:
        string_parts.append(str(number))

    return " ".join(string_parts)

def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n: The upper bound integer (inclusive). Must be non-negative.

    Returns:
        A space-delimited string of numbers from 0 to n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
        >>> string_sequence(10)
        '0 1 2 3 4 5 6 7 8 9 10'
    """
    # Step 1: Validate the input explicitly
    _validate_input(n)

    # Step 2: Define the start and end of the sequence
    start_value = 0
    end_value = n

    # Step 3: Generate the sequence of numbers
    # We use a helper to ensure clear logic and potential reuse
    raw_numbers = _generate_number_sequence(start_value, end_value)

    # Step 4: Convert the list of integers to a list of strings
    string_representations = []
    for number in raw_numbers:
        string_representations.append(str(number))

    # Step 5: Join the string representations with a single space
    final_output = " ".join(string_representations)

    return final_output