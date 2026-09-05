def decimal_to_octal(number: int) -> str:
    """
    Convert a decimal integer to its octal string representation.

    This function handles:
    - Positive integers
    - Zero
    - Negative integers

    Parameters:
    number (int): The decimal integer to convert.

    Returns:
    str: The octal representation of the decimal number.

    Raises:
    TypeError: If the input is not an integer.
    ValueError: If the input is not a valid integer (e.g., None, float, string).
    """

    # --- Step 1: Input Validation ---

    # Check if the input is None
    if number is None:
        raise ValueError("Input cannot be None.")

    # Check if the input is an integer type. 
    # Note: bool is a subclass of int in Python, so we explicitly exclude it.
    if not isinstance(number, int):
        raise TypeError(f"Expected an integer, but got {type(number).__name__}.")

    # Check if the input is a boolean (since bool is an int subclass)
    # While technically integers, converting booleans to octal is ambiguous in this context.
    if isinstance(number, bool):
        raise TypeError("Boolean values are not accepted as input.")

    # --- Step 2: Handle the Zero Case Explicitly ---
    # If the number is zero, the octal representation is simply "0".
    # This is a base case to simplify the main conversion loop.
    if number == 0:
        return "0"

    # --- Step 3: Determine Sign and Work with Absolute Value ---
    # We need to preserve the sign of the original number for the final result.
    is_negative = number < 0

    # Work with the absolute value of the number for the modulo/division loop.
    current_number = abs(number)

    # --- Step 4: Perform Base Conversion (Decimal to Octal) ---
    # We will build the octal string digit by digit using integer division and modulo.

    octal_digits = []

    # Loop until the number is fully reduced to zero
    while current_number > 0:
        # Step 4a: Calculate the remainder when divided by 8.
        # This gives us the least significant octal digit.
        remainder = current_number % 8

        # Step 4b: Convert the numeric remainder (0-7) to its character representation.
        # We map 0->'0', 1->'1', ..., 7->'7'.
        digit_char = str(remainder)

        # Step 4c: Store this digit.
        # We append to a list for O(1) insertion at the beginning later.
        octal_digits.append(digit_char)

        # Step 4d: Update the number by integer division by 8.
        # This shifts to the next most significant digit.
        current_number = current_number // 8

    # --- Step 5: Assemble the Octal String ---
    # The digits were collected from least significant to most significant.
    # We need to reverse the list to get the correct order.
    octal_digits.reverse()

    # Join the list of characters into a single string.
    octal_string = "".join(octal_digits)

    # --- Step 6: Handle Negative Numbers ---
    # If the original number was negative, prepend a minus sign.
    if is_negative:
        octal_string = "-" + octal_string

    return octal_string