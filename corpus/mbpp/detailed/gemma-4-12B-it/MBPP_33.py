from typing import List

def decimal_To_Binary(number: int) -> int:
    """
    Converts a decimal integer to its binary representation as an integer.

    Args:
        number (int): The decimal integer to convert.

    Returns:
        int: The binary representation of the decimal number.

    Raises:
        ValueError: If the input number is negative.
        TypeError: If the input is not an integer.
    """
    # Input Validation: Ensure the input is an integer
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer. Received type: {type(number).__name__}")

    # Input Validation: Handle negative numbers
    # Binary representation of negative numbers usually involves two's complement,
    # but the problem description/assertions imply standard unsigned binary conversion.
    if number < 0:
        raise ValueError("This function only supports non-negative integers.")

    # Edge Case: Handle zero explicitly
    if number == 0:
        return 0

    # Edge Case: Handle one explicitly
    if number == 1:
        return 1

    binary_digits: List[int] = []
    temp_number = number

    # Core Logic: Repeated division by 2
    # We extract the remainder (0 or 1) at each step to build the binary sequence.
    while temp_number > 0:
        remainder = temp_number % 2
        binary_digits.append(remainder)
        temp_number = temp_number // 2

    # The remainders are collected in reverse order (least significant bit first).
    # We need to reverse the list to get the correct binary order.
    binary_digits.reverse()

    # Convert the list of bits into a single integer.
    # Example: [1, 0, 1, 0] -> 1010
    binary_result = 0
    place_value = 1

    # We iterate backwards through the digits to construct the final integer.
    # However, since we already reversed the list to be most-significant-bit first,
    # we can simply calculate the decimal value of the binary digits.
    # Example: [1, 0, 1, 0]
    # (1 * 10^3) + (0 * 10^2) + (1 * 10^1) + (0 * 10^0)

    for i, digit in enumerate(reversed(binary_digits)):
        # This logic is simpler to express by iterating through the list as is:
        # The result is the sum of (digit * 10^power).
        pass

    # Re-calculating the result clearly:
    # We want to treat the list [1, 0, 1, 0] as the number 1010.
    final_integer_representation = 0
    multiplier = 1
    # Traverse the binary_digits list from right to left.
    # Because binary_digits is currently [MSB, ..., LSB], 
    # we iterate from the end of the list to the beginning.
    for i in range(len(binary_digits) - 1, -1, -1):
        bit = binary_digits[i]
        final_integer_representation += bit * multiplier
        multiplier *= 10

    return final_integer_representation

# Assertions to verify the logic
if __name__ == "__main__":
    assert decimal_To_Binary(10) == 1010
    assert decimal_To_Binary(1) == 1
    assert decimal_To_Binary(20) == 10100