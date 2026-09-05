def even_bit_toggle_number(number: int) -> int:
    """
    Toggles all even-indexed bits (0-indexed from the right, i.e., least significant bit)
    of the given integer number.

    Bit positions are 0-indexed starting from the right (LSB).
    Even positions: 0, 2, 4, 6, ...
    Odd positions: 1, 3, 5, 7, ...

    Toggling means: if the bit is 0, make it 1; if it is 1, make it 0.

    Edge cases handled:
    - Negative numbers (using two's complement representation logic via masking)
    - Zero
    - Large integers (within Python's arbitrary precision limits)

    Args:
        number (int): The integer to process.

    Returns:
        int: The integer with all even-positioned bits toggled.

    Raises:
        TypeError: If the input is not an integer.
    """

    # Validate input type explicitly
    if not isinstance(number, int):
        raise TypeError(f"Expected an integer, got {type(number).__name__}")

    # Step 1: Create a mask for all even positions up to a reasonable limit.
    # Since integers in Python are arbitrary precision, we need a mask that covers
    # enough bits to handle the input number. However, the problem implies a fixed set of bits
    # or an infinite stream of zeros above the MSB.
    # Let's construct a mask where bits at even positions (0, 2, 4...) are 1,
    # and odd positions (1, 3, 5...) are 0.
    # Since we don't know the upper bound of bits in a user's perspective for an "infinite" integer,
    # we must assume the operation applies to the binary representation of the number.
    # BUT, looking at the assertions:
    # 10 (1010) -> 0 (0000) : Bits at 0, 2, 4...
    #    Bit 0 (1) -> 0
    #    Bit 1 (0) -> stays 0 (odd)
    #    Bit 2 (1) -> 0
    #    Bit 3 (0) -> stays 0 (odd)
    # 20 (10100) -> 30 (11110)
    #    Bits: 4(1), 3(0), 2(1), 1(0), 0(0)
    #    Toggle even (0, 2, 4):
    #    Bit 0: 0 -> 1
    #    Bit 2: 1 -> 0
    #    Bit 4: 1 -> 0
    #    Result so far: ...00010 = 2? Wait.
    #    Let's re-examine 20 to 30.
    #    20 = 16 + 4 = 10100 binary.
    #    30 = 16 + 8 + 4 + 2 = 11110 binary.
    #    Changes:
    #    Bit 0: 0 -> 1 (0 + 1 = 1)
    #    Bit 1: 0 -> 1 (Wait, 30 has bit 1 set. 20 had bit 1 unset. Did we toggle bit 1? No.)
    #    Let's look closer at 20 (10100) vs 30 (11110).
    #    Indices: 4 3 2 1 0
    #    20      1 0 1 0 0
    #    30      1 1 1 1 0
    #    Differences at indices: 1, 2, 3.
    #    This contradicts "toggle only even bits" if we assume a standard infinite zero-padded integer.
    #    Unless... the problem implies a specific number of bits or a specific mask pattern derived from the examples.
    #    
    #    Re-evaluating the examples strictly:
    #    Ex 1: 10 (1010) -> 0 (0000)
    #    Ex 2: 20 (10100) -> 30 (11110)
    #    Ex 3: 30 (11110) -> 20 (10100)
    #    
    #    Hypothesis A: Toggle bits at indices 0, 2, 4, 6... relative to the right.
    #    Check 10 (1010):
    #      idx 0: 0 -> toggle to 1
    #      idx 1: 1 -> keep
    #      idx 2: 0 -> toggle to 1
    #      idx 3: 1 -> keep
    #      Result: 1011 (11). Expected 0. FAIL.
    #    
    #    Hypothesis B: Maybe the problem considers 1-based indexing?
    #    "Even bits" usually means even positions. 
    #    Let's look at the mapping again.
    #    10 -> 0. 10 is 1010. To get 0, ALL bits must become 0.
    #    20 -> 30. 20 is 10100. 30 is 11110.
    #    30 -> 20. 30 is 11110. 20 is 10100.
    #    
    #    Let's try to reverse engineer the mask from 10 -> 0.
    #    If 10 (1010) becomes 0 (0000), then bits 1 and 3 must have been toggled? Or bits 0 and 2?
    #    If we toggle 0 and 2:
    #      1010 (bits 3,2,1,0)
    #      Toggle 0 (0->1), Toggle 2 (1->0).
    #      Result: 1001 (9). Not 0.
    #    If we toggle 1 and 3:
    #      Toggle 1 (1->0), Toggle 3 (1->0).
    #      Result: 0000 (0). MATCH!
    #    
    #    Let's check this "Toggle Odd Positions (1, 3, 5...)" hypothesis against other examples.
    #    Ex 2: 20 (10100) -> 30 (11110)
    #    Indices: 4 3 2 1 0
    #    Values:  1 0 1 0 0
    #    Target:  1 1 1 1 0
    #    Differences at: 1, 2, 3.
    #    If we toggle odd positions (1, 3, 5...):
    #      Pos 1 (val 0) -> 1.
    #      Pos 3 (val 0) -> 1.
    #      Result so far: ...11010 (26).
    #      Expected: 30 (11110).
    #      Missing bit 2. Bit 2 is even. It wasn't toggled in this hypothesis.
    #      But 20->30 requires bit 2 to change (1->1? No, 20 has bit 2 set (4), 30 has bit 2 set (4). Wait.)
    #      Let's re-calculate binary for 20 and 30 carefully.
    #      20 = 16 + 4 = 10100_2. (Bits at 4 and 2 are 1. Bits 3,1,0 are 0).
    #      30 = 16 + 8 + 4 + 2 = 11110_2. (Bits at 4,3,2,1 are 1. Bit 0 is 0).
    #      Comparison 20 vs 30:
    #        Bit 4: 1 vs 1 (Same)
    #        Bit 3: 0 vs 1 (Changed 0->1) -> Odd index.
    #        Bit 2: 1 vs 1 (Same)
    #        Bit 1: 0 vs 1 (Changed 0->1) -> Odd index.
    #        Bit 0: 0 vs 0 (Same)
    #      So 20 -> 30 only changes bits 1 and 3. These are ODD indices.
    #      
    #    Let's re-calculate 10 vs 0.
    #    10 = 1010_2 (Bits 3, 1 are 1).
    #    0 = 0000_2.
    #    Changes:
    #      Bit 3: 1 -> 0 (Odd index)
    #      Bit 1: 1 -> 0 (Odd index)
    #      Bits 0, 2: 0 -> 0 (Even indices, unchanged)
    #      
    #    Let's re-calculate 30 vs 20.
    #    30 = 11110_2 (Bits 4, 3, 2, 1).
    #    20 = 10100_2 (Bits 4, 2).
    #    Changes:
    #      Bit 3: 1 -> 0 (Odd index)
    #      Bit 1: 1 -> 0 (Odd index)
    #      
    #    Conclusion from examples: The operation is actually **toggling all ODD bits** (indices 1, 3, 5...).
    #    However, the problem statement says "toggle all even bits".
    #    Is it possible the problem uses 1-based indexing for "even bits"?
    #    If bit positions are 1, 2, 3, 4... (LSB is position 1).
    #    Then "even bits" would be positions 2, 4, 6... which correspond to 0-indexed 1, 3, 5...
    #    This matches our finding!
    #    
    #    Definition for solution:
    #    - Use 1-based indexing for the bit positions (1st bit, 2nd bit, etc.).
    #    - Toggle bits at even positions (2nd, 4th, 6th... from the right).
    #    - In 0-indexed terms (LSB=0), these are indices 1, 3, 5, 7...
    #    
    #    Let's verify the logic with this definition:
    #    Mask needed: 1 at indices 1, 3, 5... (0-indexed).
    #    Pattern: 01010101... (starting from LSB).
    #    Binary: ...01010101
    #    Hex pattern for infinite mask: 0x55555555...
    #    
    #    Algorithm:
    #    result = number XOR mask
    #    where mask has 1s at odd indices (0-indexed).

    # Step 2: Generate a mask with 1s at odd indices (0-indexed) and 0s at even indices.
    # We need a mask that is at least as wide as the number.
    # Since Python handles arbitrary precision, we can generate a mask dynamically
    # or use a sufficiently large constant if the problem domain is fixed (32-bit/64-bit).
    # Given the examples are small, but Python ints are unlimited, we should construct the mask based on the bit length of the number.
    # However, if the number is 0, we still need to handle it.

    # To be safe and handle arbitrary size numbers correctly:
    # We can construct a mask with 1s at positions 1, 3, 5... up to the bit length of the input number.
    # Actually, the XOR operation only affects bits that exist or are set in the mask.
    # If we use a mask that is 1 at all odd positions indefinitely, it will toggle bits that are 0 in the number to 1 (creating new 1s), 
    # which might not be desired if the number is treated as a fixed-width value.
    # But usually in such puzzles, "toggle" implies flipping existing bits within the relevant range.
    # If the problem implies an infinite stream of zeros, toggling them to ones would change the number significantly.
    # Looking at 10 -> 0: 
    #   10 is 1010. Bits above index 3 are 0.
    #   If we have an infinite mask of 10101..., indices 5, 7, 9... are 1.
    #   Those bits in 10 are 0. If we toggle them, they become 1.
    #   10 (1010 0000...) -> toggle 1,3,5,7...