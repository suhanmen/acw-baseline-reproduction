from typing import List

def count_With_Odd_SetBits(n: int) -> int:
    """
    Calculates the number of integers from 0 up to and including n 
    (inclusive) that have an odd number of set bits (1s) in their 
    binary representation.

    Args:
        n (int): The upper bound (inclusive) of the range of integers.

    Returns:
        int: The count of integers in [0, n] with an odd number of set bits.

    Raises:
        ValueError: If n is a negative integer.
        TypeError: If n is not an integer.
    """
    # --- Input Validation ---
    # Ensure the input is of the correct type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received {type(n).__name__}")

    # Ensure the input is non-negative as the problem implies a range [0, n]
    if n < 0:
        raise ValueError(f"Input must be a non-negative integer, received {n}")

    # --- Core Logic ---
    # We need to iterate through every integer from 0 to n.
    # For each integer, we count how many '1' bits are in its binary form.
    # If that count is odd, we increment our result counter.

    total_count_with_odd_bits = 0

    # Iterate through the range [0, n]
    for current_number in range(n + 1):
        # Calculate the number of set bits (population count)
        set_bits_count = _get_set_bits_count(current_number)

        # Check if the number of set bits is odd
        # A number is odd if the remainder when divided by 2 is 1
        is_odd = (set_bits_count % 2 != 0)

        if is_odd:
            total_count_with_odd_bits += 1

    return total_count_with_odd_bits

def _get_set_bits_count(num: int) -> int:
    """
    Helper function to count the number of set bits (1s) in 
    the binary representation of a non-negative integer.

    This uses the Brian Kernighan's algorithm or a standard bit shift 
    approach for clarity.
    """
    count = 0
    # We create a local copy to work with to avoid any side effects 
    # (though ints are immutable in Python).
    temp_num = num

    # Standard bit manipulation: 
    # While the number is greater than 0, shift right and check the LSB.
    while temp_num > 0:
        # If the least significant bit is 1, increment count
        if temp_num & 1 == 1:
            count += 1
        # Right shift to process the next bit
        temp_num = temp_num >> 1

    return count

# Note: The problem asks for the count of integers from 0 up to n.
# Example Trace: 
# count_With_Odd_SetBits(5)
# 0: 000 (0 bits) - even
# 1: 001 (1 bit)  - odd (count=1)
# 2: 010 (1 bit)  - odd (count=2)
# 3: 011 (2 bits) - even
# 4: 100 (1 bit)  - odd (count=3)
# 5: 101 (2 bits) - even
# Wait, the assertion says count_With_Odd_SetBits(5) == 3.
# My manual trace for 5:
# 0 (0), 1 (1), 2 (1), 3 (2), 4 (1), 5 (2)
# Odd counts are at 1, 2, and 4. Total = 3. Correct.

# Example Trace:
# count_With_Odd_SetBits(10)
# 0:0, 1:1*, 2:1*, 3:2, 4:1*, 5:2, 6:2, 7:3*, 8:1*, 9:2, 10:2
# Wait, let's re-check 7 and 10:
# 7 is 111 (3 bits) -> odd
# 8 is 1000 (1 bit) -> odd
# 9 is 1001 (2 bits) -> even
# 10 is 1010 (2 bits) -> even
# Odd bits: 1, 2, 4, 7, 8. Total = 5. Correct.

# Example Trace:
# count_With_Odd_SetBits(15)
# 0:0, 1:1*, 2:1*, 3:2, 4:1*, 5:2, 6:2, 7:3*, 8:1*, 9:2, 10:2, 11:3*, 12:2, 13:3*, 14:3*, 15:4
# Odd bits: 1, 2, 4, 7, 8, 11, 13, 14. Total = 8. Correct.