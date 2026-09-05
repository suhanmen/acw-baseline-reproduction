def even_bit_toggle_number(n: int) -> int:
    """
    Toggles all even bits of a given number.
    In bit positions (starting from 0), even bits are 0, 2, 4, 6, ...
    The mask for even bits is 10101010... in binary.
    For a 32-bit integer, this mask is 0x55555555.
    For a 64-bit integer, it is 0x5555555555555555.
    Since Python integers have arbitrary precision, we need a way to 
    generate a mask that covers all possible even bits of the input number.
    """
    # A mask where all even bits are 1.
    # Since we need to toggle, we use XOR with a mask of all 1s at even positions.
    # The pattern 0x5 is 0101 in binary. 
    # To cover the number, we can calculate the necessary mask size.

    if n == 0:
        # Technically, 0 has an infinite number of even bits as 0.
        # However, for practical purposes in these tests, we toggle 
        # bits within the range of the number's magnitude or a standard 32/64 bit range.
        # Based on the test cases:
        # 10 (1010) -> toggle even bits (0, 2) -> (1010 ^ 0101) = 1111 (15)? 
        # Wait, the assertions say:
        # 10 (1010) -> 0. 10 is 1010. Even bits are at positions 0 and 2.
        # Bits:  3 2 1 0
        # Val:   1 0 1 0
        # Mask:  0 1 0 1  (even bits are 2 and 0)
        # 1010 ^ 0101 = 1111 (15). This doesn't match 0.

        # Let's re-evaluate "even bits". 
        # If positions are 1-indexed: 1, 2, 3, 4...
        # If "even bits" refers to the indices 0, 2, 4... 
        # Let's check 10 (1010) -> 0. 
        # 1010 ^ XXXX = 0000 => Mask must be 1010.
        # 1010 has bits at positions 3 and 1 set. These are ODD indices.
        # This means the problem defines "even bits" as bits at indices 1, 3, 5...
        # OR it defines "even bits" as bits at indices 0, 2, 4... but 10 is 1010 
        # and the result is 0, meaning bits 3 and 1 were toggled.
        # Let's re-read: "toggle all even bits".
        # If bits are 1-indexed: 1, 2, 3, 4...
        # Bit 1 is 2^0, Bit 2 is 2^1, Bit 3 is 2^2, Bit 4 is 2^3.
        # Even bits are 2, 4, 6... which correspond to indices 1, 3, 5...
        # Let's check 20 (10100). Bits are at 4, 2. (Index 4 and 2).
        # Indices 1, 3, 5... are the even bits (2nd, 4th, 6th...).
        # 20 is 10100. Even bits are indices 1, 3, 5...
        # Mask for indices 1, 3, 5... is ...101010.
        # 20 (10100) ^ 101010 (in binary) = 10100 ^ 101010.
        # This logic is confusing. Let's try a simpler pattern.
        pass

    # Let's re-examine the test cases:
    # 10 (1010) -> 0.  XOR with 1010 (binary) results in 0.
    # 20 (10100) -> 30 (11110). 10100 ^ 11110 = 01010 (10).
    # Wait, 10100 ^ 11110 = 01010. 
    # Let's try XORing 20 (10100) with a mask of even bits (indices 0, 2, 4...):
    # Mask: ...10101 (0x5555...)
    # 20 (10100) ^ ...10101 = 11111 (31)? No.

    # Let's try XORing with odd bits (indices 1, 3, 5...):
    # Mask: ...01010 (0xAAA...)
    # 10 (1010) ^ 1010 = 0000 (0). Correct!
    # 20 (10100) ^ 101010 = 00000? No.

    # Let's try XORing with even bits as 0, 2, 4... but "even" refers to the 1-based position.
    # Position 1 (2^0), Position 2 (2^1), Position 3 (2^2), Position 4 (2^3)
    # Even positions: 2, 4, 6... -> indices 1, 3, 5...
    # Mask for indices 1, 3, 5... is 0xAAAAAAAA...
    # 10 (1010) ^ 1010 (0xAA) = 0. Correct.
    # 20 (10100) ^ 101010 (0xAA) = 10100 ^ 101010 = 000010... no.
    # 20 is 10100. 0xAA is ...10101010.
    # 10100 ^ 101010 = 000010? No, bitwise XOR:
    # 20:      010100
    # Mask:    101010
    # Result:  111110 (which is 62). Still not 30.

    # Let's try index 0, 2, 4... (0x5555...)
    # 10 (1010) ^ 0101 = 1111 (15)
    # 20 (10100) ^ 010101 = 11111 (31)

    # Wait! Let's try 30 -> 20.
    # 30 is 11110. 20 is 10100.
    # 11110 ^ 10100 = 01010 (10).
    # So in all cases, the XOR mask is 10 (1010).
    # But 10 is the value for n=10? That's not a general rule.
    # Let's look at the masks again.
    # 10 (1010) -> 0. Mask = 1010.
    # 20 (10100) -> 30 (11110). Mask = 10100 ^ 11110 = 01010 (10).
    # 30 (11110) -> 20 (10100). Mask = 11110 ^ 10100 = 01010 (10).
    # In all three cases, the XOR mask is 10 (binary 1010).
    # Binary 1010 means bits at indices 1 and 3 are toggled.
    # These are the even positions (2nd and 4th bits).

    # If the rule is "Toggle all even bits", and the even positions are 2, 4, 6...
    # the indices are 1, 3, 5, 7...
    # The mask for indices 1, 3, 5, 7... is 0xAAAAAAAA...
    # 10 (00001010) ^ 0xAA = 1010 ^ 1010 = 0000. Correct.
    # 20 (00010100) ^ 0xAA = 10100 ^ 101010 = 111110 (62)? 
    # Wait, 0xAA is ...10101010.
    # 20 is 10100.
    #   010100 (20)
    # ^ 101010 (0xAA)
    # = 111110 (62)

    # Let's try "even bits" as indices 0, 2, 4...
    # Mask is 0x5555...
    # 10 (1010) ^ 0x55 = 1010 ^ 0101 = 1111 (15)
    # 20 (10100) ^ 0x55 = 10100 ^ 010101 = 11111 (31)
    # 30 (11110) ^ 0x55 = 11110 ^ 010101 = 10101 (21)

    # Re-calculating 20 -> 30.
    # 20 is 10100. 30 is 11110.
    # 10100 ^ 11110 = 01010.
    # This means bits 1 and 3 were toggled.
    # 30 is 11110. 20 is 10100.
    # 11110 ^ 10100 = 01010.
    # So the mask is always 01010 (10).
    # 10 is 1010.
    # In both cases, the mask is "1010" or "01010".
    # These are the bits at indices 1 and 3. 
    # The problem says "toggle ALL even bits".
    # If we assume "even bits" are bits at positions 0, 2, 4, 6...
    # and the numbers are small, let's check:
    # 10 (1010): Even bits are at pos 0 and 2. 
    # Bits at 0 and 2 are 0 and 1.
    # Toggling them: bit 0 becomes 1, bit 2 becomes 0.
    # 1010 -> 1101 (13). Not 0.

    # What if "even bits" means bits that are even numbers? 
    # (No, that doesn't make sense).
    # What if the bit numbering starts from 1?
    # Bit 1 (2^0), Bit 2 (2^1), Bit 3 (2^2), Bit 4 (2^3)
    # Even bits: Bit 2, Bit 4, Bit 6...
    # These are indices 1, 3, 5...
    # Mask: 10101010... (0xAA)
    # 10 (1010) ^ 1010 = 0. Correct!
    # 20 (10100) ^ 101010 = 10100 ^ 101010 = 111110 (62).
    # Wait, 20 in binary is 10100. The bits are:
    # Pos: 5 4 3 2 1
    # Val: 1 0 1 0 0
    # Even bits: 2, 4. 
    # Values at these positions are: Pos 2 is 0, Pos 4 is 0.
    # Toggling them: Pos 2 becomes 1, Pos