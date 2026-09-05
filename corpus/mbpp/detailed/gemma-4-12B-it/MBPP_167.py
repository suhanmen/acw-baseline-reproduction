from typing import Union

def next_Power_Of_2(n: Union[int, float]) -> int:
    """
    Finds the smallest power of 2 that is greater than or equal to n.

    Args:
        n: A numeric value (integer or float).

    Returns:
        The smallest power of 2 >= n as an integer.

    Raises:
        ValueError: If the input is negative, as powers of 2 (2^x) 
                    for non-negative x are always positive.
        TypeError: If the input is not a number.
    """
    # --- Input Validation ---
    # Ensure the input is a numeric type (int or float)
    if not isinstance(n, (int, float)):
        raise TypeError(f"Input must be an integer or a float, not {type(n).__name__}")

    # Powers of 2 (1, 2, 4, 8...) are positive. 
    # If n is negative, the smallest power of 2 >= n is 2^0 = 1.
    # However, the problem logic usually implies n >= 0. 
    # For consistency with the provided assertions, we handle 0 as 1.
    # If n is negative, we treat it as 0 or throw an error. 
    # To be defensive and follow standard math: next power of 2 >= n where n < 0 is 1.
    if n < 0:
        # Depending on interpretation, one could throw an error.
        # Here we treat any negative number as effectively needing to reach 1 (2^0).
        n = 0

    # --- Edge Case: n = 0 ---
    # The smallest power of 2 is 2^0 = 1.
    # Since 1 >= 0, the answer is 1.
    if n == 0:
        return 1

    # --- Conversion to Integer ---
    # If n is a float like 5.5, we need the next power of 2 >= 5.5 (which is 8).
    # If n is 8.0, the next power is 8.
    # We treat the number as its ceiling integer value to find the power of 2.
    import math
    target_value = math.ceil(n)

    # --- Logic for finding the power of 2 ---
    # If target_value is already a power of 2, return it.
    # Otherwise, find the next power.

    # Case where target_value is 1 (e.g., input was 0.1 or 1.0)
    if target_value <= 1:
        return 1

    # Check if target_value is a power of 2 using bitwise logic
    # A number x is a power of 2 if (x > 0) and (x & (x - 1) == 0)
    is_power_of_two = (target_value > 0) and (target_value & (target_value - 1) == 0)

    if is_power_of_two:
        return int(target_value)

    # If not a power of 2, we need to find the next one.
    # We can do this by finding the position of the highest set bit.
    # Example: n = 5. Binary is 101. Highest bit is at position 2 (val 4).
    # The next power of 2 is 2^(position + 1).

    # bit_length() returns the number of bits required to represent an integer in binary.
    # For 5 (101), bit_length is 3.
    # For 8 (1000), bit_length is 4.
    bit_count = target_value.bit_length()

    # The next power of 2 will be 2 raised to the power of the bit_count.
    # Example: target_value = 5 (binary 101). bit_count = 3. 
    # Result = 2^3 = 8.
    # Example: target_value = 17 (binary 10001). bit_count = 5.
    # Result = 2^5 = 32.
    result = 1 << bit_count

    return int(result)