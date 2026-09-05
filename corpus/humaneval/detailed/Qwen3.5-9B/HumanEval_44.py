def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """

    # Helper function to validate the base argument
    def _validate_base(b: int) -> None:
        """Check if the base is a valid positive integer less than 10."""
        if not isinstance(b, int):
            raise TypeError(f"Base must be an integer, got {type(b).__name__}")
        if b <= 0:
            raise ValueError(f"Base must be a positive integer greater than 0, got {b}")
        if b >= 10:
            raise ValueError(f"Base must be less than 10 as per problem constraints, got {b}")

    # Helper function to perform the base conversion logic
    def _convert_to_base(value: int, b: int) -> str:
        """
        Recursively converts a non-negative integer to a string in a specific base.

        Args:
            value: The integer value to convert (must be >= 0).
            b: The base to convert to (assumed valid and > 1).

        Returns:
            A string representing the number in the specified base.
        """
        # Base case: if the value is 0, return '0' immediately
        if value == 0:
            return "0"

        # Base case for recursion: if value is less than base, it's a single digit
        if value < b:
            return str(value)

        # Recursive step:
        # 1. Get the remainder (the least significant digit in the new base)
        current_digit = value % b
        # 2. Get the value without the least significant digit
        remaining_value = value // b
        # 3. Recursively convert the remaining value
        converted_part = _convert_to_base(remaining_value, b)
        # 4. Concatenate the converted part with the current digit
        return converted_part + str(current_digit)

    # Step 1: Validate inputs
    if not isinstance(x, int):
        raise TypeError(f"x must be an integer, got {type(x).__name__}")

    _validate_base(base)

    # Step 2: Handle negative numbers
    # We will determine the sign first, then work with the absolute value
    is_negative = False
    if x < 0:
        is_negative = True
        abs_x = -x
    else:
        abs_x = x

    # Step 3: Perform the conversion on the absolute value
    # Handle the specific case of zero explicitly to avoid returning '-' if x was -0 (though -0 == 0 in Python)
    if abs_x == 0:
        return "0"

    # Call the conversion helper
    result_part = _convert_to_base(abs_x, base)

    # Step 4: Reconstruct the final string
    if is_negative:
        final_result = "-" + result_part
    else:
        final_result = result_part

    return final_result