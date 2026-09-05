from typing import Union

def binary_to_decimal(binary_input: int) -> int:
    """
    Converts a binary number (represented as an integer) to its 
    decimal (base-10) equivalent.

    Args:
        binary_input (int): An integer representing a binary number 
                             (e.g., 1011 for eleven).

    Returns:
        int: The decimal representation of the input binary number.

    Raises:
        ValueError: If the input contains digits other than 0 or 1.
        TypeError: If the input is not an integer.
    """
    # Input Validation: Ensure the input is an integer type
    if not isinstance(binary_input, int):
        raise TypeError(f"Input must be an integer, received {type(binary_input).__name__}")

    # Handle edge case: Negative numbers are not standard binary representations
    if binary_input < 0:
        raise ValueError("Binary representation cannot be negative.")

    # Handle edge case: Zero
    if binary_input == 0:
        return 0

    # Convert the integer to a string to iterate over each bit
    binary_str = str(binary_input)

    # Variable to store the final decimal result
    decimal_result = 0

    # Variable to track the current power of 2 (starts at 2^0)
    # We determine the power based on the position from the right (index)
    # Example: In '1011', the rightmost '1' is at position 0 (2^0)
    length_of_string = len(binary_str)

    for index, char in enumerate(binary_str):
        # Check if the character is a valid binary digit
        if char != '1' and char != '0':
            raise ValueError(f"Invalid binary digit detected: '{char}'. "
                             "Input must only contain 0s and 1s.")

        # Determine the current bit value
        bit_value = 1 if char == '1' else 0

        # Calculate the exponent for the current position
        # The rightmost character in the string is at index (length - 1)
        # Its exponent is 0.
        # The leftmost character is at index 0.
        # Its exponent is (length - 1).
        exponent = length_of_string - 1 - index

        # Calculate the value contributed by this bit
        # e.g., bit 1 at position 3 is 1 * (2^3) = 8
        place_value = bit_value * (2 ** exponent)

        # Accumulate into the final result
        decimal_result += place_value

    return decimal_result

if __name__ == "__main__":
    # These assertions verify the logic against the provided requirements
    assert binary_to_decimal(100) == 4
    assert binary_to_decimal(1011) == 11
    assert binary_to_decimal(1101101) == 109