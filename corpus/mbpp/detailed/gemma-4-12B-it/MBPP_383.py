import typing

def even_bit_toggle_number(n: int) -> int:
    """
    Toggles all odd bits of a given number.

    In computer science and bit manipulation, bits are typically indexed 
    starting from 0 (the least significant bit). 
    An odd bit refers to bits at positions 1, 3, 5, 7, ...

    Example logic:
    10 in binary is 1010 (Bits at positions 3, 1, 0 are set).
    Odd positions are 1 and 3.
    Toggling bit 1: 1010 -> 1000
    Toggling bit 3: 1000 -> 0000 (Wait, the example says 10 -> 15)

    Let's re-evaluate the prompt's examples to determine the bit indexing:
    Example 1: 10 -> 15
    10 is 01010
    15 is 01111
    Difference: Bits at positions 0 and 2 were flipped? No, that's even.
    Let's check 10 (1010) and 15 (1111). 
    Bits changed: 0 (from 0 to 1) and 2 (from 0 to 1). Those are even.

    Wait, let's re-read: "toggle all odd bits". 
    If the prompt says even_bit_toggle_number but asks for "odd bits", 
    and the assertion says even_bit_toggle_number(10) == 15:
    10: 1010
    15: 1111
    Bits changed: 0 and 2. These are EVEN positions.

    Example 2: 20 -> 1
    20: 10100
    1:  00001
    Bits changed: 0, 2, 3, 4.

    Let's look at the function name vs the description.
    The name is "even_bit_toggle_number". 
    Let's check 10 (1010) -> 15 (1111) again.
    Bit 0: 0 -> 1 (Changed)
    Bit 1: 1 -> 1 (No change)
    Bit 2: 0 -> 1 (Changed)
    Bit 3: 1 -> 1 (No change)
    Indices 0 and 2 are even.

    Let's check 20 (10100) -> 1 (00001)
    Bit 0: 0 -> 1 (Changed)
    Bit 1: 0 -> 0 (No change)
    Bit 2: 1 -> 0 (Changed)
    Bit 3: 0 -> 0 (No change)
    Bit 4: 1 -> 0 (Changed)
    Wait, indices 0, 2, and 4 are even.

    Let's check 30 (11110) -> 11 (01011)
    30: 11110
    11: 01011
    Bit 0: 0 -> 1 (Changed)
    Bit 1: 1 -> 1 (No change)
    Bit 2: 1 -> 0 (Changed)
    Bit 3: 1 -> 1 (No change)
    Bit 4: 1 -> 0 (Changed)
    Indices 0, 2, and 4 are even.

    Conclusion: Despite the text saying "odd bits", the function name 
    and the assertions strictly indicate toggling EVEN bits (0, 2, 4, ...).

    Mask for even bits: 
    ...1010101 in binary.
    In hex, this is 0x55555555... (binary 01010101)
    """

    # 1. Validate input type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    # 2. Handle negative numbers
    # Bitwise operations on negative numbers in Python use two's complement 
    # representation with an infinite sign bit. To ensure standard behavior, 
    # we treat the number as a standard integer.
    if n < 0:
        # Depending on requirements, we could raise an error or treat as unsigned.
        # Most bit manipulation problems assume non-negative integers.
        # We will process it as is, which follows standard Python bitwise rules.
        pass

    # 3. Define the mask for even bits.
    # Even positions are 0, 2, 4, 6, ...
    # A bitmask where only even positions are set:
    # ...01010101 in binary is 0x55...
    # We use a sufficiently large mask for standard 64-bit integers.
    # For potentially larger Python integers, we can generate the mask dynamically.

    # Determine how many bits we need to cover the number n.
    # If n is 0, we still need at least one bit.
    bit_length = n.bit_length()
    if bit_length == 0:
        bit_length = 1

    # We need a mask that covers all bits up to the highest set bit of n.
    # To be safe and handle carries/toggles correctly, we'll ensure it covers
    # the range of the input.

    mask = 0
    # Generate a mask where every even bit (0, 2, 4, ...) is set to 1.
    # This loop builds the mask 01010101...
    for i in range(0, bit_length + 1, 2):
        mask |= (1 << i)

    # 4. Perform the toggle using XOR.
    # XORing with a bitmask flips the bits where the mask has a 1.
    result = n ^ mask

    # Note on assertion consistency:
    # If the prompt explicitly demands "odd" but provides "even" assertions, 
    # the assertions take precedence for the "observable behavior".
    # However, let's double check 10 -> 15.
    # 10 is 1010. Mask 0101 (5) -> 1010 ^ 0101 = 1111 (15). Correct.
    # 20 is 10100. Mask 10101 (21) -> 10100 ^ 10101 = 00001 (1). Correct.
    # 30 is 11110. Mask 11111 (31) -> 11110 ^ 11111 = 00001 (Wait, 30^31 is 1).
    # Let's re-check 30 -> 11.
    # 30 is 11110. 11 is 01011.
    # Bits at 0, 2, 4 are changed?
    # Bit 0: 0 -> 1
    # Bit 2: 1 -> 0
    # Bit 4: 1 -> 0
    # 30 ^ mask? 
    # If mask is 10101 (21): 30 is 11110. 11110 ^ 10101 = 01011. 
    # 01011 in decimal is 11. Correct.

    return result

def even_bit_toggle_number(n: int) -> int:
    """
    Toggles all even bits (0, 2, 4, ...) of a given number.
    The problem description mentions 'odd', but the assertions provided 
    clearly demonstrate even bit toggling (indices 0, 2, 4...).
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    # Calculate the bit length to ensure the mask is large enough.
    # We use n.bit_length() to see how many bits are needed to represent n.
    # We add a small buffer to ensure we cover the necessary range.
    num_bits = n.bit_length()
    if num_bits == 0:
        num_bits = 1

    # Construct the mask where bits at 0, 2, 4, 6... are set to 1.
    # This is the standard way to target 'even' bit positions.
    even_mask = 0
    for i in range(0, num_bits + 1, 2):
        even_mask |= (1 << i)

    # XOR the input number with the mask to flip the bits.
    result = n ^ even_mask

    return result