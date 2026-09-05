from typing import Union

def count_set_bits(number: Union[int, float, str]) -> int:
    """
    Counts the number of set bits (1s) in the binary representation of a given integer.

    This function implements a defensive approach:
    1. Validates the input type.
    2. Handles the conversion of floats and strings to integers safely.
    3. Filters out negative numbers (as negative numbers have infinite set bits in 2's complement).
    4. Uses Brian Kernighan's Algorithm for efficiency: repeatedly flips the least significant set bit
       to 0 and increments a counter until the number becomes 0.

    Args:
        number: The input value to be evaluated. Expected to be convertible to a non-negative integer.

    Returns:
        int: The count of set bits in the binary representation of the input number.

    Raises:
        TypeError: If the input cannot be converted to a non-negative integer.
        ValueError: If the converted integer is negative.
    """

    # Step 1: Input Validation - Check Type
    # Although we support conversion later, raw strings or complex objects should be caught early if they don't fit criteria.
    if isinstance(number, str):
        # If it is a string, attempt to convert. If not a valid integer representation, raise TypeError.
        try:
            number = int(number)
        except ValueError:
            raise TypeError(f"String input '{number}' is not a valid integer representation.")
    elif isinstance(number, float):
        # Check for NaN or Infinity first
        if number != number:  # NaN check
            raise ValueError("Float input cannot be NaN.")
        if number == float('inf') or number == float('-inf'):
            raise ValueError("Float input cannot be infinite.")

        # Convert float to int
        # We cast directly, but will check negativity later
        number = int(number)

        # Check for precision loss warning scenario (e.g., 0.9999 -> 0, 1.0001 -> 1)
        # For strict mathematical correctness in production, one might check if abs(number - original) > epsilon,
        # but for counting bits, the integer value is the source of truth.
    elif isinstance(number, int):
        pass  # Already an integer, proceed
    else:
        raise TypeError(f"Unsupported input type: {type(number).__name__}. Expected int, float, or str.")

    # Step 2: Value Validation - Ensure Non-Negative
    # Binary representation for negative numbers in two's complement is infinite in length conceptually.
    # Therefore, we only count bits for non-negative integers.
    if number < 0:
        raise ValueError(f"Negative numbers are not supported. Input: {number}")

    # Step 3: Handle Zero Edge Case
    # Zero has no set bits. The algorithm below works for zero naturally (loop condition fails immediately),
    # but we explicitly handle it for clarity in the logic flow.
    if number == 0:
        return 0

    # Step 4: Count Set Bits using Brian Kernighan's Algorithm
    # Principle: n & (n - 1) unsets the rightmost set bit of n.
    # We repeat this until n becomes 0.

    bit_count = 0
    current_value = number

    while current_value > 0:
        # Identify the least significant set bit and remove it
        # Example: 
        #   current_value = 6 (binary: 110)
        #   current_value - 1 = 5 (binary: 101)
        #   current_value & (current_value - 1) = 4 (binary: 100)
        #   One '1' was removed.

        current_value = current_value & (current_value - 1)

        # Increment the counter
        bit_count += 1

    return bit_count