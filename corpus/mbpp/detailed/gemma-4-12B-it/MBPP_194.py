def octal_To_Decimal(octal_num: int) -> int:
    """
    Converts an octal (base-8) number represented as an integer into 
    its decimal (base-10) equivalent.

    Args:
        octal_num (int): An integer representing an octal number.

    Returns:
        int: The decimal representation of the input octal number.

    Raises:
        ValueError: If the input contains digits outside the range [0, 7].
        TypeError: If the input is not an integer.
    """
    # Validate input type
    if not isinstance(octal_num, int):
        raise TypeError(f"Input must be an integer, received {type(octal_num).__name__}")

    # Handle the case of zero explicitly
    if octal_num == 0:
        return 0

    # Handle negative numbers (Assuming the problem treats negative octals 
    # as the negative of their positive counterparts)
    is_negative = False
    working_num = octal_num
    if working_num < 0:
        is_negative = True
        working_num = abs(working_num)

    # Convert the number to a string to iterate through digits
    # This handles numbers of any length (e.g., 100_octal -> 64_decimal)
    octal_str = str(working_num)

    decimal_value = 0
    num_digits = len(octal_str)

    # Iterate through the string to calculate the decimal value
    # Example: 25 (octal)
    # Position 0: '2' at power 1 (8^1)
    # Position 1: '5' at power 0 (8^0)
    for index, char in enumerate(octal_str):
        digit_char = char

        # Validate that the character is a valid octal digit
        if not ('0' <= digit_char <= '7'):
            raise ValueError(f"Invalid octal digit '{digit_char}' found in input.")

        # Convert character to integer
        digit_value = int(digit_char)

        # Calculate the power of 8 based on the position from the right
        # Power is (length - 1 - current_index)
        exponent = num_digits - 1 - index
        power_of_eight = 8 ** exponent

        # Calculate the contribution of this digit to the final total
        digit_contribution = digit_value * power_of_eight

        # Accumulate the result
        decimal_value += digit_contribution

    # Re-apply the sign if the original input was negative
    if is_negative:
        decimal_value = -decimal_value

    return decimal_value

# The following assertions verify the logic
if __name__ == "__main__":
    # Test cases provided in the prompt
    assert octal_To_Decimal(25) == 21
    assert octal_To_Decimal(30) == 24
    assert octal_To_Decimal(40) == 32

    # Additional edge cases
    assert octal_To_Decimal(0) == 0
    assert octal_To_Decimal(7) == 7
    assert octal_To_Decimal(10) == 8
    assert octal_To_Decimal(100) == 64
    assert octal_To_Decimal(-10) == -8