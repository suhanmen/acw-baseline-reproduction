import math

def even_bit_toggle_number(num: int) -> int:
    """
    Toggles all even bits of a given integer.

    Bit positions are 0-indexed, starting from the least significant bit (LSB).
    Even positions are 0, 2, 4, 6, ...

    The function uses the XOR operator (^) to toggle bits.
    A bit is toggled if the corresponding bit in the mask is 1.
    To toggle even bits (0, 2, 4, ...), we need a mask where:
    - Bit 0 is 1
    - Bit 1 is 0
    - Bit 2 is 1
    - Bit 3 is 0
    - ... and so on.

    The binary representation of this mask is 01010101... which is 
    hexadecimal 0x55555555...
    """

    # Input Validation:
    # Ensure the input is an integer.
    if not isinstance(num, int):
        raise ValueError(f"Input must be an integer. Received: {type(num)}")

    # Handle negative numbers. 
    # Standard bit manipulation in Python handles negative numbers 
    # via two's complement representation (infinite sign extension).
    # However, typically "toggle even bits" refers to a 32-bit or 64-bit 
    # context. For the provided assertions, standard positive integers are used.
    if num < 0:
        # We can proceed with the XOR logic, but it might produce 
        # counter-intuitive results for negative numbers due to infinite bits.
        # For the sake of a robust library function, we keep it but 
        # note the behavior.
        pass

    # To handle numbers of arbitrary size, we need to construct a mask
    # that has 1s at every even position up to the highest bit of the number.
    # Or, more simply, we can use a mask that covers a standard 64-bit range.
    # Given the assertions:
    # 10 is 1010 (Binary). Even bits are positions 0 and 2.
    # Position 0 is 0, Position 2 is 0. 
    # Toggling 0->1 and 0->1 gives 1111 (15)? No, wait.
    # Let's re-check assertions:
    # 10 (1010) -> result 0.
    # This means bits at positions 1 and 3 (odd) remained the same?
    # Let's re-evaluate:
    # 10 is:
    # Bit 3: 1
    # Bit 2: 0
    # Bit 1: 1
    # Bit 0: 0
    # Even bits are 0 and 2.
    # If we toggle even bits (0 and 2):
    # Bit 0: 0 becomes 1
    # Bit 2: 0 becomes 1
    # Result: 1111 (15).

    # Wait, the assertion says even_bit_toggle_number(10) == 0.
    # Let's look at the bits of 10 again: 1010.
    # If result is 0, it means bits at 1 and 3 were flipped.
    # 1010 -> 0101 (which is 5) -> No.
    # Let's check 20 (10100):
    # Bit 4: 1
    # Bit 3: 0
    # Bit 2: 1
    # Bit 1: 0
    # Bit 0: 0
    # Even bits are 0, 2, 4.
    # Toggling even bits:
    # Bit 0: 0 -> 1
    # Bit 2: 1 -> 0
    # Bit 4: 1 -> 0
    # Result bits: 00001 (1). 
    # But assertion says even_bit_toggle_number(20) == 30.
    # 30 is 11110.
    # Let's re-read: "toggle all even bits".
    # Some definitions count bit positions starting from 1 (LSB = 1).
    # If Bit 1 is the first bit, then even bits are 2, 4, 6...
    # Let's test Bit 1 = LSB:
    # 10: 1010
    # Bit 1: 0
    # Bit 2: 1
    # Bit 3: 0
    # Bit 4: 1
    # Even bits are 2 and 4.
    # Toggle Bit 2: 1 -> 0
    # Toggle Bit 4: 1 -> 0
    # Result: 0010 (2). Still not 0.

    # Let's try the other way: "Even bits" means bits at indices 0, 2, 4... 
    # but the assertion results suggest that bit 0 is the most significant bit? No.
    # Let's look at 30 -> 20.
    # 30 = 11110
    # 20 = 10100
    # Bits changed: bit at index 2 (value 4) and bit at index 4 (value 16)?
    # 11110 XOR 10100 = 01010 (which is 10).
    # No, 30 XOR 20 = 10.
    # If 30 becomes 20, the bits that changed are the ones where 30 and 20 differ.
    # 30: 1 1 1 1 0
    # 20: 1 0 1 0 0
    # Difference: bits at indices 1 and 3.
    # If bits at 1 and 3 are toggled, then "even bits" must mean bits at 
    # odd positions if we start counting from 0? No, that's confusing.

    # Let's try again. 10 -> 0.
    # 10 is 1010.
    # 0 is 0000.
    # Toggled bits are at positions 1 and 3.
    # 20 -> 30.
    # 20 is 10100.
    # 30 is 11110.
    # Toggled bits are at positions 1 and 3.
    # 30 -> 20.
    # 30 is 11110.
    # 20 is 10100.
    # Toggled bits are at positions 1 and 3.

    # Conclusion: "Even bits" in this specific problem's context means bits 
    # at positions 1, 3, 5, 7... (where position 0 is the LSB).
    # Wait, 1, 3, 5, 7 are ODD positions. 
    # Is it possible the problem considers the first bit (LSB) to be position 1?
    # If position 1 is LSB, then even positions are 2, 4, 6, 8...
    # Let's test:
    # 10 (1010). Positions (from LSB=1): 4,3,2,1.
    # Even positions are 2 and 4.
    # Bit 2 is 1, Bit 4 is 1.
    # Toggle them: Bit 2 becomes 0, Bit 4 becomes 0.
    # 1010 -> 0000. Result 0. MATCHES!
    # 20 (10100). Positions: 5,4,3,2,1.
    # Even positions are 2 and 4.
    # Bit 2 is 1, Bit 4 is 0.
    # Toggle them: Bit 2 becomes 0, Bit 4 becomes 1.
    # 10100 -> 11100 (which is 28)? No, 30 is 11110.
    # 20 is 10100. Bit 2 is 1, Bit 4 is 0. 
    # Toggling them gives 11000 (24). Still not 30.

    # Let's re-examine 20 -> 30.
    # 20 = 010100 (in 6 bits)
    # 30 = 011110 (in 6 bits)
    # Xor = 001010. Bits 1 and 3 were toggled (where LSB is 0).
    # 10 -> 0.
    # 10 = 01010
    # 0  = 00000
    # Xor = 01010. Bits 1 and 3 were toggled.
    # 30 -> 20.
    # 30 = 011110
    # 20 = 010100
    # Xor = 001010. Bits 1 and 3 were toggled.

    # In all three cases, the bits at positions 1, 3, 5... were toggled.
    # This means "even bits" refers to positions 2, 4, 6... if LSB is 1.
    # Wait. 1, 3, 5 are ODD. 2, 4, 6 are EVEN.
    # If LSB is position 0, then 1, 3, 5 are ODD.
    # If LSB is position 1, then 2, 4, 6 are EVEN.

    # So "toggle all even bits" means toggle positions 2, 4, 6... 
    # where LSB is index 1.
    # This is equivalent to toggling bits at indices 1, 3, 5... 
    # where LSB is index 0.

    # Let's check the mask for indices 1, 3, 5, 7...
    # Binary: ...101010
    # Hex: 0xAAAAAAAA

    # Let's check 10 again with 0xAAAAAAAA.
    # 10 is 0...01010.
    # 0xAAAAAAAA is 10101010...
    # 10 ^ 0xAAAAAAAA:
    # The last 4 bits of 0xAAAAAAAA are 1010.
    # 1010 ^ 1010 = 0000. Correct!

    # Let's check 20:
    # 20 is 10100.
    # Last 5 bits of 0xAAAAAAAA are 01010.
    # 10100 ^ 01010:
    #   10100
    # ^ 01010
    # -------
    #   11110 (which is 30). Correct!

    # Let's check 30:
    # 30 is 11110.
    # Last 5 bits of 0xAAAAAAAA are 01010.
    # 11110 ^ 01010:
    #   11110
    # ^ 01010
    # -------
    #   10100 (which is 20). Correct!

    # The pattern is clearly toggling bits at indices 1, 3, 5, 7, ...
    # This is achieved by XORing with a mask of 10101010... (0xAAAAAAAA).

    # To make it work for integers of any size (larger than 32 bits),
    # we need to generate a mask that has 1s at every odd position 
    # up to the highest bit of the number.

    if num == 0:
        # 0 has no bits set. Toggling 1,3,5... does nothing.
        # However, a mask of 0xAAAAAAAA would still result in 0xAAAAAAAA.
        # The problem implies we only toggle bits within the range of the number?
        # Or a standard bit width? The assertions are small.
        # If num is 0, and we toggle bits 1, 3, 5... 
        # usually, "toggle" implies we only care about the existing width.
        # But 10 -> 0 means the bits at 1 and 3 were "cleared" (1->0) 
        # or "set" (0->1).
        # If the input is 0, and we XOR with 0xAAAAAAAA,