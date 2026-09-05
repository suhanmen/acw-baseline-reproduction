from typing import List

def decimal_to_binary(n: int) -> str:
    """
    Converts a non-negative decimal integer to its binary representation
    as a string.

    Args:
        n (int): The decimal integer to convert.

    Returns:
        str: The binary representation of the integer.

    Raises:
        ValueError: If the input is a negative number.
        TypeError: If the input is not an integer.
    """
    # --- Input Validation ---

    # Check if input is an integer
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer. Received: {type(n).__name__}")

    # Check if input is non-negative
    if n < 0:
        raise ValueError(f"Decimal number must be non-negative. Received: {n}")

    # --- Edge Case Handling ---

    # The binary representation of 0 is '0'
    if n == 0:
        return "0"

    # --- Conversion Logic ---

    # We will build the binary string by repeatedly taking the remainder 
    # when dividing by 2.
    binary_digits: List[str] = []

    # Use a local variable to preserve the original 'n' if needed,
    # though here we can just reassign 'n'.
    current_value = n

    while current_value > 0:
        # Calculate the remainder (this will be 0 or 1)
        remainder = current_value % 2

        # Convert the remainder to a string and add to our list
        # We append it to the end, meaning the last bit calculated
        # will be at the end of the list.
        binary_digits.append(str(remainder))

        # Perform integer division to move to the next bit
        current_value = current_value // 2

    # --- Final Assembly ---

    # Because we appended remainders as we found them (from least 
    # significant bit to most significant bit), we must reverse the 
    # list before joining.
    binary_digits.reverse()

    # Join the list of strings into a single result string
    binary_string = "".join(binary_digits)

    return binary_string

if __name__ == "__main__":
    # Test cases provided in the prompt
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(18) == '10010'
    assert decimal_to_binary(7) == '111'

    # Additional edge cases
    assert decimal_to_binary(0) == '0'
    assert decimal_to_binary(1) == '1'
    assert decimal_to_binary(2) == '10'