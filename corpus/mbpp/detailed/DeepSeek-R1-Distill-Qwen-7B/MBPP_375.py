def round_num(number, multiple):
    """
    Rounds the given number to the nearest multiple of a specific number.

    Args:
        number: The number to be rounded.
        multiple: The multiple to which the number should be rounded.

    Returns:
        The rounded number.

    Raises:
        ValueError: If the multiple is zero or if either input is not an integer.
    """
    # Validate inputs
    if not isinstance(number, int) or not isinstance(multiple, int):
        raise ValueError("Both number and multiple must be integers.")
    if multiple == 0:
        raise ValueError("Multiple cannot be zero.")

    # Calculate the nearest multiple
    rounded_number = multiple * round(number / multiple)

    return rounded_number

# Example usage
print(round_num(4722, 10))   # Expected output: 4720
print(round_num(1111, 5))    # Expected output: 1110
print(round_num(219, 2))     # Expected output: 218