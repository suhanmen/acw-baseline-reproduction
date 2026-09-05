def _create_mask_for_even_bits() -> int:
    """
    Creates a bitmask where all bits at even positions (0, 2, 4, ...) are set to 1,
    and all bits at odd positions (1, 3, 5, ...) are set to 0.

    The mask is constructed by starting with 1 (bit 0 set) and repeatedly shifting
    left by 2 and OR-ing with the current result.

    This loop effectively builds the pattern:
    0011 0011 0011 0011 ... (binary)

    Returns:
        An integer representing the mask with even bits set.
    """
    mask = 1

    # We loop 32 times because standard Python integers can grow arbitrarily large,
    # but for a 32-bit context (typical in many system problems), this is sufficient.
    # However, since the problem doesn't specify a bit-width limit, we rely on the
    # fact that for any finite input N, we only care about bits up to the most significant
    # bit of N. But to handle the "set all even bits" generally without infinite loops,
    # we can construct a mask large enough to cover standard integer sizes or iterate
    # until the mask stops changing within reasonable bounds.
    # A robust approach for "all even bits" implies an infinite sequence of 1s at even positions
    # theoretically, but in practice, we align with the bit-length of the input number.
    # Let's generate a mask that covers up to 64 bits (standard for 64-bit integers)
    # to handle any reasonable input. If the input is larger, the logic naturally extends.

    for _ in range(64):
        mask = mask | (mask << 2)

        # Optimization: If the mask has become all 1s at the positions we care about
        # (i.e., shifting left no longer introduces new 1s relevant to the input size),
        # we could stop. However, for a pure mathematical "all even bits" function 
        # without a specific bit-width constraint on the input, we should ideally match
        # the bit length of the input. But creating a static large mask is efficient.
        # To be strictly correct for arbitrary large inputs, we might need to adjust based on input.
        # But the mask generation pattern converges quickly for 64 iterations.
        # Let's stick to a sufficient number of iterations for standard usage.

    return mask

def _get_bit_length_for_mask(value: int) -> int:
    """
    Calculates the number of bits required to represent the value 'value'.
    This is used to construct a mask that is exactly large enough to cover
    the bits of the input number, avoiding infinite growth for extremely large numbers.

    Returns:
        The bit length as an integer.
    """
    if value <= 0:
        return 0
    return value.bit_length()

def _construct_mask_for_input(input_value: int) -> int:
    """
    Constructs a mask tailored to the bit length of the input_value.
    This mask will have 1s at all even positions (0-indexed) up to the most significant bit
    of input_value, and 0s at odd positions.

    Args:
        input_value: The number whose bit length determines the mask size.

    Returns:
        A mask with even bits set to 1 and odd bits set to 0, sized appropriately.
    """
    if input_value <= 0:
        # For 0 or negative numbers (in terms of unsigned interpretation for bit length),
        # we return a mask of zeros or handle logically based on bit length.
        # Since bit_length() returns 0 for 0, the loop range will be empty.
        return 0

    num_bits = _get_bit_length_for_mask(input_value)

    # Start with bit 0 set (1)
    mask = 1

    # Iterate to fill even positions up to num_bits
    # We need enough iterations to cover the highest bit index.
    # The highest bit index is (num_bits - 1).
    # If num_bits is, say, 5 (bits 0,1,2,3,4), we need to ensure bit 4 is set if it's even.
    # The loop runs until we have covered the necessary range.
    # A safe upper bound is ceil(num_bits / 2) iterations.

    iterations = (num_bits + 1) // 2

    for _ in range(iterations):
        mask = mask | (mask << 2)

    return mask

def even_bit_set_number(n: int) -> int:
    """
    Sets all even bits (0-indexed: 0, 2, 4, ...) of the given number n to 1.
    Odd bits (1, 3, 5, ...) remain unchanged.

    Examples:
        n = 10 (binary 1010)
        Bits at indices: 3(1), 2(0), 1(0), 0(1)
        Even indices: 0, 2.
        Current values at even indices: bit 0 is 1, bit 2 is 0.
        Result: bit 2 becomes 1 -> 1110 (binary) = 14. 
        WAIT. Let's re-verify the problem statement examples.

        Problem Assert: even_bit_set_number(10) == 10
        10 in binary: 1010.
        Indices: 3->1, 2->0, 1->0, 0->1.
        Even indices are 0 and 2.
        Current: bit 0 is 1, bit 2 is 0.
        If we set even bits to 1: bit 0 stays 1, bit 2 becomes 1.
        Result: 1110 (binary) = 14.
        But the assertion says 10.

        Let's re-read the binary of 10.
        10 = 8 + 2 = 1010.
        Positions: 3 (value 8), 2 (value 4), 1 (value 2), 0 (value 1).
        Bit 0: 0 (Value 1) -> Wait, 10 is ...1010.
        Rightmost is bit 0.
        10 / 2 = 5 rem 0 -> Bit 0 is 0.
        5 / 2 = 2 rem 1 -> Bit 1 is 1.
        2 / 2 = 1 rem 0 -> Bit 2 is 0.
        1 / 2 = 0 rem 1 -> Bit 3 is 1.
        So 10 is 1010 in binary.
        Bit 0: 0.
        Bit 1: 1.
        Bit 2: 0.
        Bit 3: 1.

        Even bits are at indices 0 and 2.
        Current state: Bit 0 is 0, Bit 2 is 0.
        If we SET even bits to 1:
        Bit 0 becomes 1.
        Bit 2 becomes 1.
        New bits: 1 (bit 3), 1 (bit 2), 1 (bit 1), 1 (bit 0).
        Binary: 1111 = 15.

        This contradicts the assertion: assert even_bit_set_number(10) == 10.

        Let's re-evaluate the interpretation of "even bits".
        Maybe it means bits with value even? No, that's "even numbers".
        Maybe it means the positions where the bit represents an even power of 2? (Which is standard 0, 2, 4).

        Let's look at the second example:
        assert even_bit_set_number(20) == 30
        20 in binary: 10100.
        Bit 0: 0
        Bit 1: 0
        Bit 2: 1 (Value 4)
        Bit 3: 0
        Bit 4: 1 (Value 16)

        Even positions: 0, 2, 4.
        Current values: Bit 0=0, Bit 2=1, Bit 4=1.
        Set even positions to 1:
        Bit 0 -> 1
        Bit 2 -> 1 (unchanged)
        Bit 4 -> 1 (unchanged)
        Resulting binary: 11101.
        Value: 16 + 8 + 4 + 1 = 29.
        Assertion says 30.

        This suggests my understanding of the bit positions or the operation is flawed.
        Let's reconsider the standard bit indexing.
        Usually, bit 0 is the least significant.

        Is it possible the problem considers 1-based indexing for "even"?
        If 1-based:
        10 (1010):
        Pos 1 (val 1): 0
        Pos 2 (val 2): 1
        Pos 3 (val 4): 0
        Pos 4 (val 8): 1
        Even positions: 2, 4.
        Set them to 1. They are already 1. Result 10. Matches!

        20 (10100):
        Pos 1 (val 1): 0
        Pos 2 (val 2): 0
        Pos 3 (val 4): 1
        Pos 4 (val 8): 0
        Pos 5 (val 16): 1
        Even positions: 2, 4.
        Set them to 1:
        Pos 2 (was 0) -> 1. Adds 2.
        Pos 4 (was 0) -> 1. Adds 8.
        Original: 16 + 4 = 20.
        New: 16 + 8 + 4 + 2 = 30. Matches!

        30 (11110):
        Pos 1: 0
        Pos 2: 1
        Pos 3: 1
        Pos 4: 1
        Pos 5: 1
        Even positions: 2, 4.
        They are already 1. Result 30. Matches!

        Conclusion: The problem uses 1-based indexing for bit positions.
        "Even bits" means bits at positions 2, 4, 6, 8... (where position 1 is the LSB).
        These correspond to powers of 2: 2^1, 2^3, 2^5... i.e., 2, 8, 32...
        Standard 0-indexed terms: bits at indices 1, 3, 5...

        So the task is: Set all odd-indexed bits (0, 2, 4...) to 1? 
        No, standard 0-indexed bit 1, 3, 5... are the ones we need to set.
        Let's verify:
        Standard index 1 (value 2) -> 1-based pos 2 (even).
        Standard index 3 (value 8) -> 1-based pos 4 (even).

        So the mask should have 1s at standard indices 1, 3, 5, 7...
        And 0s at standard indices 0, 2, 4...

        Let's re-verify with 10 (1010):
        Indices: 3(1), 2(0), 1(1), 0(0).
        Target indices to set: 1, 3.
        Index 1 is already 1. Index 3 is already 1. Result 10. Correct.

        Let's re-verify with 20 (10100):
        Indices: 4(1), 3(0), 2(1), 1(0), 0(0).
        Target indices to set: 1, 3.
        Index 1 is 0 -> set to 1.
        Index 3 is 0 -> set to 1.
        New bits: 4(1), 3(1), 2(1), 1(1), 0(0).
        Binary: 11110.
        Value: 16 + 8 + 4 + 2 = 30. Correct.

        Logic Update:
        We need a mask where bits at 0-indexed positions 1, 3, 5, ... are 1.
        Bits at 0-indexed positions 0, 2, 4, ... are 0.
        Pattern: 0101 0101 0101 ... (binary)

        Implementation plan:
        1. Create a mask with pattern 010101...
        2. Apply this mask to the input number using bitwise OR.

        Creating the 0101... mask:
        Start with 2 (binary 10, which is bit 1 set).
        Loop: mask = mask | (mask << 2).
        Example trace:
        Init: 2 (0...