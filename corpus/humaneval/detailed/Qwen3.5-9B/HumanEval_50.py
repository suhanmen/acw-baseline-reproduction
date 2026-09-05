import string
import re

def _validate_alpha_string(input_str: str, operation_context: str = "input") -> str:
    """
    Validates that the input string contains only lowercase alphabetic characters.
    Raises a ValueError if validation fails.

    Args:
        input_str: The string to validate.
        operation_context: A description of the operation (for error messages).

    Returns:
        The validated string if successful.

    Raises:
        ValueError: If the string is empty or contains non-alphabetic characters.
    """
    if not isinstance(input_str, str):
        raise TypeError(f"The '{operation_context}' must be a string, not {type(input_str).__name__}.")

    if not input_str:
        raise ValueError(f"The '{operation_context}' cannot be an empty string.")

    # Check for empty after stripping? No, per requirements we treat empty as invalid edge case
    # unless specified otherwise, but the problem implies valid alphabet operations.
    # Let's assume empty string is a valid edge case for length 0 processing, 
    # but our validation logic below will catch it if we require non-empty.
    # However, looking at the one-liner, empty string returns empty string.
    # We should allow empty string to pass through gracefully as it's a valid degenerate case.
    # But the requirement says "Validate the inputs and deal with invalid ones explicitly".
    # Is empty string invalid? Usually no. Is non-alpha invalid? Yes.

    non_alpha_chars = [char for char in input_str if not char.isalpha()]

    if non_alpha_chars:
        invalid_char_set = set(non_alpha_chars)
        raise ValueError(
            f"The '{operation_context}' contains invalid characters: {invalid_char_set}. "
            f"Only lowercase alphabetic characters (a-z) are permitted."
        )

    # Note: The original one-liner assumes lowercase. If uppercase or mixed appears, 
    # ord() logic breaks because 'A' is 65 and 'a' is 97. 
    # The one-liner: chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a"))
    # If ch = 'A' (65): 65 + 5 - 97 = -27. -27 % 26 = 23. 23 + 97 = 120 ('x'). 
    # This would wrap 'A' into 'x'. This is likely unintended for a standard alphabet shift 
    # which usually implies strictly lowercase 'a'-'z'.
    # Given the strict nature of the problem and the presence of ord("a"), 
    # we enforce strict lowercase input.

    return input_str

def _shift_character(char: str, shift_amount: int) -> str:
    """
    Shifts a single lowercase alphabetic character by a specified amount.

    Args:
        char: A single lowercase alphabetic character.
        shift_amount: The integer amount to shift (positive or negative).

    Returns:
        The shifted character.

    Raises:
        ValueError: If the input character is not a lowercase letter.
        TypeError: If inputs are not of expected types.
    """
    if not isinstance(char, str) or len(char) != 1:
        raise TypeError(f"Character must be a string of length 1, got {type(char).__name__}.")

    # Double check lowercase constraint here for robustness
    if not ('a' <= char <= 'z'):
        raise ValueError(f"Character '{char}' is not a lowercase alphabetic letter.")

    base = ord("a")

    # Calculate raw position
    current_pos = ord(char) - base

    # Apply shift and handle wrap-around using modulo 26
    # Modulo handles negative numbers correctly in Python (e.g., -1 % 26 = 25)
    shifted_pos = (current_pos + shift_amount) % 26

    # Convert back to ASCII character
    return chr(shifted_pos + base)

def decode_shift(s: str) -> str:
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function reverses the encoding process by shifting every character by -5.
    It includes robust validation and explicit error handling for invalid inputs.

    Args:
        s: The encoded string containing only lowercase alphabetic characters.

    Returns:
        The decoded string with original characters restored.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input is empty or contains non-alphabetic characters.
    """
    # Explicit validation step
    _validate_alpha_string(s, operation_context="input")

    # Define shift amount for decoding (inverse of +5)
    decode_offset = -5

    # Handle the empty string case explicitly as an edge case
    if not s:
        return s

    decoded_chars = []

    # Iterate through each character with explicit variable naming
    for char in s:
        try:
            shifted_char = _shift_character(char, decode_offset)
            decoded_chars.append(shifted_char)
        except (ValueError, TypeError) as e:
            # In a strict defensive system, we might re-raise or log, 
            # but since we validate upfront, this shouldn't happen unless validation logic changes.
            # Re-raising to preserve error context is best practice here.
            raise e

    # Join characters back into a string explicitly
    return "".join(decoded_chars)