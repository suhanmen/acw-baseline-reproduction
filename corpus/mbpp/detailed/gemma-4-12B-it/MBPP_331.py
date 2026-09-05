import math

def count_unset_bits(n: int) -> int:
    """
    Counts the number of unset bits (0s) in the binary representation 
    of a given integer.

    The function considers the binary representation starting from the 
    most significant bit (MSB) that is set to 1 down to the least 
    significant bit. 

    Example: 
    - 2 is binary 10. There is one 0. Result = 1.
    - 4 is binary 100. There are two 0s. Result = 2.
    - 6 is binary 110. There is one 0. Result = 1.

    Note: For input 0, the binary representation is "0", which has zero
    unset bits based on the logic of standard bit counting for positive 
    integers, but usually, 0 is treated as having no bits if we only 
    count up to the highest set bit. Based on the test cases provided, 
    we count zeros between the MSB and the LSB.
    """
    # --- Input Validation ---
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received {type(n).__name__}")

    # The problem implies positive integers based on the provided assertions.
    # If n is negative, binary representation is typically two's complement,
    # which is infinite or depends on bit-width. We will treat negative 
    # inputs as invalid for this specific count.
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # --- Edge Case: Zero ---
    # If the input is 0, there are no set bits.
    # Depending on interpretation, this could be 0 or 1.
    # Given the assertions (2->1, 4->2, 6->1), the logic is 
    # (Total bits in the number's significant range) - (Set bits).
    if n == 0:
        return 0

    # --- Logic ---
    # Step 1: Find the position of the most significant bit (MSB).
    # For example, if n = 4 (100), the MSB is at index 2 (0-indexed).
    bit_length = n.bit_length()

    # Step 2: Count the number of set bits (1s).
    # We can do this by iterating through the bits or using bit_count() in Python 3.10+
    # To remain compatible and explicit, we will manually count.
    set_bits_count = 0
    temp_n = n
    while temp_n > 0:
        # Check if the last bit is 1
        if temp_n & 1 == 1:
            set_bits_count += 1
        # Shift right by 1 bit
        temp_n = temp_n >> 1

    # Step 3: Calculate the number of unset bits.
    # The number of bits used to represent n is n.bit_length().
    # For example, 4 is 100 (3 bits). Set bits = 1. Unset bits = 3 - 1 = 2.
    # For 6 is 110 (3 bits). Set bits = 2. Unset bits = 3 - 2 = 1.
    # For 2 is 10 (2 bits). Set bits = 1. Unset bits = 2 - 1 = 1.
    total_bits_used = bit_length
    unset_bits_count = total_bits_used - set_bits_count

    return unset_bits_count