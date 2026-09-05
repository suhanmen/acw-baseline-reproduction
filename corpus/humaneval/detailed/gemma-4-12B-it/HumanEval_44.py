import math

def _validate_inputs(x: int, base: int) -> None:
    """
    Validates that the inputs are of the correct type and within 
    the specified constraints for the base conversion logic.
    """
    if not isinstance(x, int):
        raise TypeError(f"Input 'x' must be an integer, got {type(x).__name__}")

    if not isinstance(base, int):
        raise TypeError(f"Input 'base' must be an integer, got {type(base).__name__}")

    # According to the prompt, base numbers are less than 10.
    # Standard positional notation requires base >= 2.
    if base < 2 or base >= 10:
        raise ValueError(f"Base must be between 2 and 9 inclusive. Received: {base}")

def _convert_to_base_string(number: int, base: int) -> str:
    """
    Performs the core conversion logic for a non-negative integer.
    """
    # Handle the zero case explicitly
    if number == 0:
        return "0"

    digits = []
    current_value = number

    while current_value > 0:
        # Find the remainder (the digit in the current position)
        remainder = current_value % base
        digits.append(str(remainder))

        # Update the quotient for the next iteration
        current_value = current_value // base

    # The digits were appended in order of least significant to most significant.
    # We must reverse them to get the standard representation.
    digits.reverse()

    return "".join(digits)

def change_base(x: int, base: int) -> str:
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
    # Step 1: Validate inputs to ensure production-grade robustness
    _validate_inputs(x, base)

    # Step 2: Handle negative numbers
    # Base conversion usually represents the magnitude. 
    # We store the sign and work with the absolute value.
    is_negative = x < 0
    abs_x = abs(x)

    # Step 3: Perform the conversion
    result_string = _convert_to_base_string(abs_x, base)

    # Step 4: Re-attach the negative sign if necessary
    if is_negative:
        return "-" + result_string

    return result_string