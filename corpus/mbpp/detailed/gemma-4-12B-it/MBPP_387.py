import string

def even_or_odd(hex_string: str) -> str:
    """
    Determines whether a given hexadecimal string represents an even or odd number.

    The parity of a hexadecimal number is determined solely by its last digit.
    If the last digit represents an even value, the entire number is even.
    Otherwise, it is odd.

    Args:
        hex_string (str): A string representing a hexadecimal number.
                          Can contain digits 0-9 and letters A-F (case-insensitive).

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.

    Raises:
        ValueError: If the input string is empty or contains non-hexadecimal characters.
    """
    # 1. Validate Input Type
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string.")

    # 2. Handle empty string case
    if not hex_string.strip():
        raise ValueError("Input string cannot be empty.")

    # 3. Clean the string (remove whitespace)
    hex_string = hex_string.strip()

    # 4. Define valid hexadecimal characters
    # We include both lowercase and uppercase for robustness
    valid_chars = set(string.hexdigits)

    # 5. Validate that every character in the string is a valid hex digit
    for char in hex_string:
        if char not in valid_chars:
            raise ValueError(f"Invalid character found in hex string: '{char}'")

    # 6. Identify the last character
    # The parity of any positional number system base B is determined by the 
    # parity of the last digit (provided B is even). 
    # Since 16 is even, we only need to check the final digit.
    last_char = hex_string[-1]

    # 7. Convert the last character to its integer value
    # We use a mapping or int(x, 16) to get the numeric value of the hex digit.
    try:
        # int(char, 16) handles '0'-'9', 'a'-'f', and 'A'-'F' correctly.
        last_digit_value = int(last_char, 16)
    except ValueError:
        # This should theoretically not be reached due to the validation step above
        raise ValueError("Failed to convert the last character to a hexadecimal integer.")

    # 8. Check parity
    # A number is even if the remainder when divided by 2 is zero.
    is_even = (last_digit_value % 2 == 0)

    # 9. Return result
    if is_even:
        return "Even"
    else:
        return "Odd"

# The following assertions check the logic against the provided test cases.
if __name__ == "__main__":
    # Testing provided cases
    # "AB3454D" -> D is 13 (Odd)
    assert even_or_odd("AB3454D") == "Odd"

    # "ABC" -> C is 12 (Even)
    assert even_or_odd("ABC") == "Even"

    # "AAD" -> D is 13 (Odd)
    assert even_or_odd("AAD") == "Odd"