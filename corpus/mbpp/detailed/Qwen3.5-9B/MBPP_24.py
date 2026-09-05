def validate_binary_string(binary_string: str) -> None:
    """
    Validates that the input string is a valid representation of a binary number.

    A valid binary number:
    - Must not be empty.
    - Must contain only characters '0' and '1'.
    - Must not start with a plus sign (though Python int() handles it, 
      we enforce strict binary format as per problem context).
    - Must not contain any other whitespace or special characters.

    Raises:
        ValueError: If the input string is invalid.
        TypeError: If the input is not a string.
    """
    if not isinstance(binary_string, str):
        raise TypeError(
            f"Input must be a string, but got type '{type(binary_string).__name__}'"
        )

    if len(binary_string) == 0:
        raise ValueError("Input binary string cannot be empty.")

    # Check for any character that is not '0' or '1'
    for index, character in enumerate(binary_string):
        if character not in ('0', '1'):
            raise ValueError(
                f"Character '{character}' at position {index} is not a valid binary digit."
            )

    # Ensure no leading '+' sign unless it's the only character (which would be invalid anyway)
    # though the above loop would catch '+' as invalid. Just a sanity check for clarity.
    if binary_string.startswith('+'):
        raise ValueError("Input binary string must not start with a '+' sign.")

def _process_binary_digit(current_value: int, digit: int, position_power: int) -> int:
    """
    Helper to calculate the contribution of a specific digit to the total decimal value.

    In binary, digits are processed from right to left (least significant to most significant).
    The rightmost digit (index -1) corresponds to 2^0.
    The next (index -2) corresponds to 2^1, and so on.

    Formula: contribution = digit * (2 ** position_power)

    Args:
        current_value: The accumulated decimal value so far (initially 0).
        digit: The current binary digit (0 or 1).
        position_power: The power of 2 corresponding to this position.

    Returns:
        The new accumulated decimal value after including this digit.
    """
    power_of_two = 1 << position_power  # Efficiently calculates 2 ** position_power
    digit_contribution = digit * power_of_two
    new_value = current_value + digit_contribution
    return new_value

def binary_to_decimal(binary_string: str) -> int:
    """
    Converts a string representation of a binary number to its decimal equivalent.

    This function performs manual conversion without using Python's built-in int(string, 2).
    It validates the input strictly, processes each digit explicitly, and handles
    edge cases such as empty strings, invalid characters, and zero.

    Args:
        binary_string: A string consisting only of '0's and '1's representing a binary number.

    Returns:
        The decimal (base-10) integer equivalent of the binary string.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty or contains invalid characters.
    """
    # Step 1: Validate the input explicitly
    validate_binary_string(binary_string)

    # Step 2: Initialize the accumulator for the decimal value
    decimal_value = 0

    # Step 3: Calculate the length of the string to determine positions
    string_length = len(binary_string)

    # Step 4: Iterate through the string from right to left (least significant to most)
    # We track the 'current_index' from the end of the string.
    current_index_from_end = 0

    # Loop through characters in reverse order
    for char in reversed(binary_string):
        # Explicitly convert the character to an integer (0 or 1)
        # Doing this inside the loop ensures we handle the digit extraction clearly.
        digit = int(char)

        # Calculate the power of 2 for the current position
        # Rightmost digit is 2^0, next is 2^1, etc.
        power_of_two = 1 << current_index_from_end

        # Calculate the contribution of this digit
        contribution = digit * power_of_two

        # Add the contribution to the running total
        decimal_value = decimal_value + contribution

        # Increment the position power for the next iteration
        current_index_from_end += 1

    return decimal_value