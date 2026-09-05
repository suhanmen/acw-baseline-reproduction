from typing import Union

def decimal_to_octal(decimal_number: int) -> int:
    """
    Converts a non-negative decimal integer to its octal (base-8) representation.

    The return value is an integer where each digit represents the octal place value.
    For example, decimal 10 becomes octal 12 (1*8 + 2*1).

    Args:
        decimal_number (int): The non-negative decimal integer to convert.

    Returns:
        int: The octal representation as an integer.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative integer.
    """
    # 1. Input Validation: Check if the input is an integer type
    if not isinstance(decimal_number, int):
        raise TypeError(f"Input must be an integer. Received: {type(decimal_number)}")

    # 2. Input Validation: Check if the input is non-negative
    # Octal representation for negative numbers usually involves a sign, 
    # but standard conversion functions for these assertions assume non-negative.
    if decimal_number < 0:
        raise ValueError("Decimal number must be non-negative.")

    # 3. Edge Case: Zero
    # The octal representation of 0 is 0.
    if decimal_number == 0:
        return 0

    # 4. Conversion Logic
    # We will use the repeated division method to extract octal digits.
    # The remainder of division by 8 gives the least significant digit.

    octal_digits = []
    temp_number = decimal_number

    while temp_number > 0:
        # Calculate the remainder when dividing by 8
        remainder = temp_number % 8

        # Store the remainder (this is the current octal digit)
        octal_digits.append(remainder)

        # Perform integer division to move to the next place value
        temp_number = temp_number // 8

    # 5. Construct the final result
    # The digits were collected in order of least significant to most significant.
    # We need to reverse them to construct the final integer correctly.
    octal_digits.reverse()

    final_octal_value = 0
    place_value = 1

    # We iterate backwards through the digits to rebuild the integer.
    # Example: digits [1, 2] for decimal 10
    # result = (2 * 1) + (1 * 8) = 10? No, the logic above built 
    # the list as [2, 1] initially, then reversed to [1, 2].
    # To convert the list [1, 2] to the integer 12:
    # We iterate through the reversed list and multiply by powers of 10.

    # Re-evaluating construction:
    # If list is [1, 2], the desired result is 12 (one-two).
    # This means the list represents digits from most significant to least significant.

    # Correct logic for reconstructing the integer from the list [1, 2]:
    # Result = (1 * 10^1) + (2 * 10^0)

    # Re-calculating based on the logic used in step 4/5:
    # Let's use a more explicit construction method.

    octal_string_result = ""
    # Since we reversed 'octal_digits', index 0 is the most significant digit.
    # Example: 10 -> remainder 2, then remainder 1. List: [2, 1]. Reversed: [1, 2].
    for digit in octal_digits:
        octal_string_result += str(digit)

    # Convert the string of octal digits to a decimal-looking integer.
    # This preserves the "12" format requested by the assertions.
    return int(octal_string_result)

# Validation of the specific assertions provided in the problem:
if __name__ == "__main__":
    # Test Case 1: 10 -> 12
    # 10 / 8 = 1 remainder 2. 1 / 8 = 0 remainder 1. Result: 12.
    assert decimal_to_octal(10) == 12

    # Test Case 2: 2 -> 2
    # 2 / 8 = 0 remainder 2. Result: 2.
    assert decimal_to_octal(2) == 2

    # Test Case 3: 33 -> 41
    # 33 / 8 = 4 remainder 1. 4 / 8 = 0 remainder 4. Result: 41.
    assert decimal_to_octal(33) == 41