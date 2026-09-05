from typing import Optional

def set_Bit_Number(n: int) -> Optional[int]:
    """
    Finds the value of the most significant bit (MSB) that is set in an integer.

    For example:
    - 6  is 00110 in binary. MSB set bit is 4 (00100).
    - 10 is 01010 in binary. MSB set bit is 8 (01000).
    - 18 is 10010 in binary. MSB set bit is 16 (10000).

    Args:
        n (int): The integer to analyze.

    Returns:
        Optional[int]: The value of the most significant set bit, 
                        or None if no bits are set (for n <= 0).

    Raises:
        TypeError: If the input is not an integer.
    """
    # Input Validation: Ensure the input is an integer
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received {type(n).__name__}")

    # Handle edge cases: 0 and negative numbers
    # MSB is usually defined for positive integers in this context.
    # If n is 0, no bits are set.
    if n <= 0:
        return None

    # We need to find the highest power of 2 less than or equal to n.
    # We can do this by iterating downwards from the highest possible 
    # bit position or by using bit manipulation.

    # To be defensive and clear, we find the position of the highest bit.
    # In Python, bit_length() returns the number of bits required to 
    # represent an integer in binary, excluding the sign and leading zeros.

    # Example: 6 in binary is '110'. bit_length() is 3.
    bit_count = n.bit_length()

    # If the number is positive, bit_length() will always be at least 1.
    if bit_count == 0:
        return None

    # The most significant bit's value is 2^(bit_count - 1).
    # Example: n=6, bit_count=3. MSB = 2^(3-1) = 2^2 = 4.
    # Example: n=10, bit_count=4. MSB = 2^(4-1) = 2^3 = 8.
    msb_position = bit_count - 1
    msb_value = 1 << msb_position

    return msb_value

# The function satisfies the following assertions:
# assert set_Bit_Number(6) == 4
# assert set_Bit_Number(10) == 8
# assert set_Bit_Number(18) == 16