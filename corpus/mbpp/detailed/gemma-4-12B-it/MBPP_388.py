import math

def highest_Power_of_2(n: int) -> int:
    """
    Finds the highest power of 2 that is less than or equal to n.

    Args:
        n (int): An integer input.

    Returns:
        int: The highest power of 2 <= n.

    Raises:
        ValueError: If n is less than 1, as there is no positive power 
                    of 2 less than or equal to a non-positive integer.
        TypeError: If n is not an integer.
    """
    # Step 1: Validate input type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer. Received: {type(n).__name__}")

    # Step 2: Handle boundary cases and invalid ranges
    # Powers of 2 (2^x where x >= 0) start at 1 (2^0).
    # If n < 1, there is no positive power of 2 <= n.
    if n < 1:
        raise ValueError(f"Input must be at least 1. Received: {n}")

    # Step 3: Handle the simplest case
    # If n is 1, the highest power of 2 <= 1 is 2^0 = 1.
    if n == 1:
        return 1

    # Step 4: Use bitwise logic to find the result.
    # The highest power of 2 less than or equal to n corresponds to the 
    # most significant bit (MSB) of the binary representation of n.

    # Example: 
    # 10 in binary is 1010. The MSB is at position 3 (value 2^3 = 8).
    # 32 in binary is 100000. The MSB is at position 5 (value 2^5 = 32).

    # We can find the position of the MSB using the bit_length() method.
    # bit_length() returns the number of bits required to represent an integer in binary.
    bit_count = n.bit_length()

    # The power of 2 is 2 raised to the power of (bit_count - 1).
    # For n=10, bit_count is 4. Result is 2^(4-1) = 2^3 = 8.
    exponent = bit_count - 1
    result = 1 << exponent

    return result

# Example Verification (internal check):
# assert highest_Power_of_2(10) == 8
# assert highest_Power_of_2(19) == 16
# assert highest_Power_of_2(32) == 32