def count_unset_bits(number: int) -> int:
    """
    Counts the number of unset bits (bits with value 0) in the binary representation
    of a given non-negative integer.

    The count is performed over the range of bits from the most significant bit (MSB)
    of the number down to the least significant bit (LSB), which is bit 0.
    Bits higher than the MSB are not considered in this specific implementation,
    as the standard interpretation for such problems usually limits the scope to
    the bits required to represent the number itself.

    If the input number is zero, the function considers it to have 0 unset bits
    within its own bit representation (since it requires no bits to represent).
    However, mathematically, an integer 0 is represented as ...0000.
    Based on the provided assertions and standard problem constraints for this
    type of question, we assume the scope is the minimal bit-width required
    to represent the non-negative integer n, excluding leading infinite zeros.

    For n = 0: 
        Binary representation is '0'. 
        There are no unset bits counted because the single bit '0' is the number itself?
        Wait, let's re-evaluate based on assertions.
        If n=2 (binary 10), MSB is bit 1. Range is bit 1, bit 0.
        Bits: 1, 0. 
        Unset: bit 0. Count = 1. Matches assert.

        If n=4 (binary 100), MSB is bit 2. Range is bit 2, bit 1, bit 0.
        Bits: 1, 0, 0.
        Unset: bit 1, bit 0. Count = 2. Matches assert.

        If n=6 (binary 110), MSB is bit 2. Range is bit 2, bit 1, bit 0.
        Bits: 1, 1, 0.
        Unset: bit 0. Count = 1. Matches assert.

        Therefore, the logic is: Find the position of the highest set bit (MSB).
        Count all bits from that position down to 0 that are 0.

        Edge case: n = 0.
        There is no set bit. The loop for finding MSB will not execute or handle differently.
        If there are no set bits, how many unset bits?
        Based on the pattern, if there are no set bits, the set of bits to consider is empty?
        Or does it imply 0 unset bits?
        Given n=0, binary is 0. No bits are "active" in the sense of defining the width.
        Let's assume for n=0, the count is 0.
    """

    # Input validation: Ensure the number is a non-negative integer.
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer, received type {type(number).__name__}")

    if number < 0:
        raise ValueError(f"Input must be a non-negative integer, received negative value: {number}")

    # Special case: Handle zero explicitly.
    # Based on the logic derived from assertions (counting 0s within the bit-width of the number),
    # the number 0 does not have a defined "width" of set bits to establish a range.
    # Thus, we return 0.
    if number == 0:
        return 0

    # Initialize a counter for the unset bits.
    unset_bit_count = 0

    # Determine the total number of bits we need to examine.
    # We examine bits from the Most Significant Bit (MSB) down to Bit 0 (LSB).
    # The MSB is the highest bit index that has a value of 1.
    # The total count of bits to inspect is (MSB_position + 1).

    # Strategy to find the position of the MSB:
    # We can start checking from a reasonable upper bound or iterate bit by bit.
    # Since we need to be defensive and explicit, we will iterate from bit 0 upwards
    # until we find the highest set bit.

    current_bit_position = 0

    # Flag to track if we have found the MSB.
    msb_found = False

    # We iterate to find the MSB. 
    # For efficiency, we could calculate log2, but a loop is explicit and handles large integers robustly
    # without floating point inaccuracies.
    # We loop while the current bit is 0 and we haven't exceeded a safe limit, 
    # but actually we just loop until we find a 1 or pass a limit?
    # Better approach: Loop until the bit at current_position is 1.

    # However, for very large numbers, a loop might be slow if we start from 0.
    # Let's iterate from 0 upwards until we find the first 1 (the MSB in the context of the number's width).
    # Wait, if we iterate from 0, we find the LSB first. We need the MSB (highest index).
    # So we iterate from 0 upwards. We stop when we find the highest bit that is 1?
    # No, the number is finite. We can check bits up to the bit length of the number.
    # In Python, n.bit_length() returns the number of bits required to represent an integer in binary,
    # excluding the sign and leading zeros.
    # For n=6 (110), bit_length is 3. This means bits at indices 0, 1, 2.
    # Index 2 is the MSB.

    # Let's use the built-in bit_length for robustness and efficiency, but explain it.
    # total_bits_to_check = n.bit_length()
    # This is O(1) in Python effectively as it returns the length of the binary string representation minus '0b'.

    total_bits_to_check = number.bit_length()

    # If total_bits_to_check is 0, it means the number is 0, which we handled above.
    # So total_bits_to_check is at least 1.

    # Now, iterate through each bit position from 0 to total_bits_to_check - 1.
    # Check if the bit at that position is 0 (unset) and increment the counter.

    for bit_index in range(total_bits_to_check):
        # Extract the bit at 'bit_index'.
        # We can use bitwise AND with (1 << bit_index).
        # If the result is non-zero, the bit is 1 (set).
        # If the result is zero, the bit is 0 (unset).

        is_bit_set = (number & (1 << bit_index)) != 0

        # Explicitly check for unset bit.
        if not is_bit_set:
            unset_bit_count += 1

    return unset_bit_count