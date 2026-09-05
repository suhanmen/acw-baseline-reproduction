from typing import Optional, Tuple

def _validate_input_string(value: Optional[str]) -> str:
    """
    Validates that the input is a string and not None.

    Args:
        value: The input to validate.

    Returns:
        The validated string.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input is None.
    """
    if value is None:
        raise ValueError("Input cannot be None.")

    if not isinstance(value, str):
        raise TypeError(f"Expected a string, but received {type(value).__name__}.")

    return value

def _extract_first_char(code: str) -> Optional[Tuple[str, str]]:
    """
    Splits the input string into the first character and the rest of the string.
    Returns None if the string is empty.

    Args:
        code: The string to split.

    Returns:
        A tuple of (first_char, remaining_string) if non-empty, else None.
    """
    if len(code) == 0:
        return None

    first_char = code[0]
    remaining = code[1:]

    return (first_char, remaining)

def _get_ascii_value(char: str) -> int:
    """
    Gets the ASCII value of a single character.

    Args:
        char: A single character string.

    Returns:
        The integer ASCII value of the character.
    """
    return ord(char)

def _calculate_total_ascii_recursive(
    first_char: str, 
    remaining: str, 
    first_char_value: int, 
    current_total: int,
    depth: int
) -> int:
    """
    Recursively calculates the total ASCII value.

    This helper explicitly shows the recursive step:
    1. Process the first character.
    2. Recurse on the remaining string.
    3. Add results.

    Args:
        first_char: The current first character.
        remaining: The rest of the string.
        first_char_value: The ASCII value of first_char (cached from parent).
        current_total: Running total of ASCII values.
        depth: Recursion depth counter (for debugging/verbose tracing if needed).

    Returns:
        The sum of ASCII values of all processed characters plus the rest.
    """
    # Base case: If no more characters remain, return current total.
    if remaining is None or len(remaining) == 0:
        return current_total

    # Extract the next character and the rest.
    split_result = _extract_first_char(remaining)

    if split_result is None:
        # Safety check, should be covered by length check above.
        return current_total

    next_char, new_remaining = split_result

    # Get ASCII value of next char.
    next_char_value = _get_ascii_value(next_char)

    # Add to running total.
    new_total = current_total + next_char_value

    # Recursive call.
    return _calculate_total_ascii_recursive(
        new_remaining, 
        new_remaining, 
        next_char_value, 
        new_total, 
        depth + 1
    )

# Overloading the recursive helper to accept the initial state properly for the public interface.
# We will refactor the logic into a cleaner iterative approach below to avoid deep recursion limits
# and make the "explicit control flow" requirement more visible and robust.

def _calculate_total_ascii_iterative(input_str: str) -> int:
    """
    Iteratively calculates the total ASCII value of characters in the string.

    Args:
        input_str: The string to process.

    Returns:
        The sum of ASCII values.
    """
    total_ascii_sum = 0

    # Handle empty string edge case explicitly before the loop.
    if len(input_str) == 0:
        return total_ascii_sum

    # Iterate explicitly through each character index.
    index = 0

    while index < len(input_str):
        current_char = input_str[index]

        # Get ASCII value for the current character.
        current_value = ord(current_char)

        # Add to the running total.
        total_ascii_sum += current_value

        # Move to the next character.
        index += 1

    return total_ascii_sum

def ascii_value_string(input_value: str) -> int:
    """
    Calculates the total ASCII value of all characters in the provided string.

    The logic follows these explicit steps:
    1. Validate that the input is a string and not None.
    2. Initialize a running total accumulator.
    3. Iterate through each character of the string explicitly.
    4. Convert each character to its ASCII integer value using ord().
    5. Add the value to the running total.
    6. Return the final sum.

    Args:
        input_value: The string to analyze.

    Returns:
        An integer representing the sum of the ASCII values of all characters.

    Raises:
        TypeError: If input_value is not a string.
        ValueError: If input_value is None.
    """
    # Step 1: Validate input
    validated_input = _validate_input_string(input_value)

    # Step 2: Initialize accumulator
    accumulated_ascii_sum = 0

    # Step 3 & 5: Process characters
    # We use a for-loop for explicit index management visibility or just direct iteration.
    # Direct iteration over string characters is the most pythonic explicit way without indices.
    for char_element in validated_input:
        # Step 4: Get ASCII value
        char_ascii_value = ord(char_element)

        # Add to accumulator
        accumulated_ascii_sum = accumulated_ascii_sum + char_ascii_value

    # Step 6: Return result
    return accumulated_ascii_sum