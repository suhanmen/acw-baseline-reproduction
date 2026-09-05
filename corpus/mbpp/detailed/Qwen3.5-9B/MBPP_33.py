def decimal_To_Binary(n: int) -> str:
    """
    Converts a decimal integer to its binary string representation.

    This function handles positive integers, zero, and negative integers.
    Negative integers are represented in two's complement form with an 
    infinite leading 1s, but for practical output, it returns the sign 
    and the magnitude's binary representation prefixed with '-'.

    Parameters:
    n (int): The decimal integer to convert.

    Returns:
    str: The binary representation of the decimal number.

    Raises:
    TypeError: If the input is not an integer.
    """

    # Step 1: Validate the input type
    if not isinstance(n, int):
        raise TypeError(f"Expected an integer, got {type(n).__name__}")

    # Step 2: Handle the special case of zero
    if n == 0:
        return "0"

    # Step 3: Handle negative numbers
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n  # Work with the absolute value

    # Step 4: Perform the division by 2 algorithm to extract binary digits
    binary_digits = []
    current_number = n

    while current_number > 0:
        remainder = current_number % 2
        quotient = current_number // 2
        binary_digits.append(str(remainder))
        current_number = quotient

    # Step 5: Reverse the list of digits because the least significant bit comes first
    binary_digits.reverse()

    # Step 6: Join the list into a single string
    binary_string = "".join(binary_digits)

    # Step 7: Add the negative sign if the original number was negative
    if is_negative:
        binary_string = "-" + binary_string

    return binary_string