def even_bit_toggle_number(n: int) -> int:
    # Create a mask with all even bit positions set to 1 (0, 2, 4, ...)
    # For a 32-bit integer: 0x55555555 = 0101 0101 ... in binary
    # Even bit positions (0-indexed) correspond to 1st, 3rd, 5th bits in a byte when viewed as LSB=0
    # Actually: bit 0 (even), bit 2 (even), bit 4 (even), etc.
    # In binary: ...10101010101010101010101010101010 -> but we want bits 0,2,4... to be 1
    # So: bit 0=1, bit 1=0, bit 2=1, bit 3=0, ... -> pattern: 10101010... repeated
    # Which is 0xAAAAAAAA for 32 bits? Let's check:
    # 0xA = 1010 in binary -> bit3=1, bit2=0, bit1=1, bit0=0 -> that's odd positions set.
    # We want even positions set: bit0=1, bit2=1, bit4=1... -> pattern 01010101...
    # That is 0x55555555 for 32 bits.

    mask = 0x55555555

    # Apply XOR to toggle bits where mask has 1s
    return n ^ mask


# Verification against provided assertions:
# even_bit_toggle_number(10) -> 10 is 1010, mask is ...0101 -> XOR: 1010 ^ 0101 = 1111? Wait, let's recompute carefully.
# Actually, 10 in binary (8 bits): 00001010
# Mask (8 bits):              00110101? No, let's build correctly.
# Bit positions: 7 6 5 4 3 2 1 0
# Even positions: 6,4,2,0 -> set to 1 in mask? No: even positions are 0,2,4,6...
# So mask should have 1 at 0,2,4,6... -> binary: ...1010101 -> for 8 bits: 10101010? 
# Wait: bit0=1, bit1=0, bit2=1, bit3=0, bit4=1, bit5=0, bit6=1, bit7=0 -> 01010101 (if bit7 is MSB)
# Actually: 01010101 in binary = 0x55 = 85. But we want bit0=1, so LSB is 1 -> yes, 01010101 has LSB=1.
# 0x55 = 0b0101_0101 -> bits: 7:0,6:1,5:0,4:1,3:0,2:1,1:0,0:1 -> even bits (0,2,4,6) are 1. Correct.
# So mask = 0x55555555 for 32-bit.

# Test 1: 10 = 0b00001010
# Bits: 3:1, 1:1 -> even bits in 10: bit0=0, bit2=0, bit4=0, bit6=0 -> none set? 
# Wait: 10 = 8+2 = 1010 -> bit3=1, bit1=1. Even positions: 0,2,4,6,8...
# In 10: bit0=0, bit2=0, bit4=0, bit6=0 -> so XOR with mask will flip these 0s to 1s.
# Result: flip bits 0,2,4,6,8... that are currently 0 to 1, and 1 to 0.
# 10: ...001010
# XOR with ...01010101... -> 
# bit0: 0^1=1
# bit1: 1^0=1
# bit2: 0^1=1
# bit3: 1^0=1
# bit4: 0^1=1
# bit5: 0^0=0
# bit6: 0^1=1
# bit7: 0^0=0
# Result: 01111011? Let's compute numerically.
# 10 ^ 0x55 = 10 ^ 85 = 91? But expected 0. Something is wrong.

# Re-read problem: "toggle all even bits". 
# The assertions: 
# even_bit_toggle_number(10) == 0
# even_bit_toggle_number(20) == 30
# even_bit_toggle_number(30) == 20

# Let's analyze 10 (1010) -> 0 (0000)
# This implies that after toggling even bits, we get 0. 
# So in 10, the even bits must be such that flipping them makes the number 0.
# 10 = 8+2 = bits 3 and 1 set. Even positions: 0,2,4,6...
# In 10: even bits are 0,2,4,6... -> all are 0? Then flipping them to 1 would make number >0, not 0.
# Unless... we only toggle even bits that are set? No, "toggle" means flip.

# Alternative interpretation: maybe "even bits" means bits at even positions when numbered starting from 1?
# But standard is 0-indexed.

# Let's check the math with the given examples:
# 10 (1010) -> 0: difference is 10. So we are subtracting 10? 
# If we toggle even bits of 10 to get 0, then the even bits of 10 must be exactly the bits of 10.
# But 10 has bits 3 and 1 set (both odd positions). So if "even bits" means odd positions? That doesn't make sense.

# Try another approach: maybe the problem means toggle the bits at even indices (0,2,4,...) regardless of current state.
# For 10 (1010): 
# bit0 (even): 0 -> toggle to 1
# bit2 (even): 0 -> toggle to 1
# bit4 (even): 0 -> toggle to 1
# ... so 10 becomes ...11110101? Not 0.

# Unless the number is considered only up to the highest set bit? Or there's a different definition.

# Let's work backwards from the assertions:
# 10 -> 0: difference = 10 = 1010. So the even bits that were set in 10 must be toggled to 0, and others to 0? 
# This is confusing.

# Try 20 (10100) -> 30 (11110)
# 20: bits 4 and 2 set (4=16, 2=2) -> 10100
# 30: 16+8+4+2 = 11110 -> bits 4,3,2,1 set
# So from 20 to 30: bit4 unchanged (1->1), bit2 unchanged (1->1), but bit3 (0->1) and bit1 (0->1) are set.
# Which bits changed? bit1 and bit3. These are ODD positions (1 and 3).
# So toggling even bits resulted in changing odd bits? That doesn't make sense.

# Wait: 20 = 10100 -> bits: 4:1, 3:0, 2:1, 1:0, 0:0
# 30 = 11110 -> bits: 4:1, 3:1, 2:1, 1:1, 0:0
# Changes: bit3 (0->1), bit1 (0->1). These are ODD positions.
# But we were supposed to toggle EVEN positions.

# Similarly, 30 (11110) -> 20 (10100)
# 30: bits 4,3,2,1
# 20: bits 4,2
# Changes: bit3 (1->0), bit1 (1->0). Again, odd positions.

# Conclusion: The problem likely has a mistake in description, OR "even bits" means bits at odd positions (1-indexed)?
# If we number bits starting at 1: 
# bit1 (LSB), bit2, bit3, ...
# Then "even bits" would be bit2, bit4, bit6... which correspond to 0-indexed positions 1, 3, 5... (odd indices)
# That matches our observation: in 20->30, bits 1 and 3 changed (0-indexed odd positions).
# So "even bits" in the problem means bits at even positions when counting from 1, i.e., 0-indexed odd positions.

# Therefore, we should toggle bits at 0-indexed positions 1,3,5,7,... 
# Mask for 0-indexed odd positions: 0xAAAAAAAA (for 32-bit) because:
# 0xAA = 1010 in binary -> bit3=1, bit2=0, bit1=1, bit0=0 -> so odd positions (1,3) are 1.
# Yes: 0xAAAAAAAA has 1s at positions 1,3,5,7,...

# Verify with 10 (1010):
# 10: bits 3,1 set (0-indexed)
# Toggle odd positions (1,3): flip bits 1 and 3.
# bit3: 1->0, bit1: 1->0 -> result 0. Correct!

# 20 (10100): bits 4,2 set. Odd positions (1,3,5,...) are 0.
# Toggle them: bit1=0->1, bit3=0->1 -> add 2+8=10, so 20+10=30. Correct!

# 30 (11110): bits 4,3,2,1 set. Odd positions: bit1 and bit3 are set.
# Toggle them: bit1:1->0, bit3:1->0 -> subtract 2+8=10, 30-10=20. Correct!

# So the mask should be 0xAAAAAAAA (for 32-bit integers).
# But note: the problem doesn't specify bit-width. However, the examples work with 32-bit.
# We'll use a mask that covers all odd positions (0-indexed) for reasonable integer sizes.
# Since Python handles arbitrary precision, we can create a mask with infinite odd bits set? 
# But we can't do that practically. However, the problem likely assumes 32-bit or similar.
# Given the examples, 0xAAAAAAAA works.

# However, to be safe for any non-negative integer, we can generate a mask with 1s at all odd positions up to the bit length of n, but actually we need to toggle all even bits (by their 1-indexed definition) regardless of n's magnitude. 
# But the problem says "all even bits", implying all positions that are even (in their indexing scheme).
# Since the examples use small numbers, and the pattern is clear, we'll use 0xAAAAAAAA for 32-bit.
# But to be generic, we can create a mask that has 1s at all odd 0-indexed positions.
# How? We can do: mask = ~0x55555555 (if 32-bit) or more generally, for arbitrary precision, we can't easily create an infinite mask.
# However, the problem's examples are within 32-bit, and the function should work for typical integers.
# Alternatively, we can compute the mask dynamically based on the number of bits, but the requirement says "all even bits", which might imply fixed-width.
# Given the context, I'll use a 32-bit mask as per standard practice in such problems unless specified otherwise.
# But to be safe, let's check: what if n is large? The problem doesn't specify, so we assume typical int range.
# However, the cleanest solution that matches all examples is using 0xAAAAAAAA.

# But wait: the problem says "toggle all even bits", and from our analysis, "even bits" means 1-indexed even positions = 0-indexed odd positions.
# So mask = 0xAAAAAAAA for 32-bit. For more bits, we might need to extend, but the problem's examples don't exceed 32-bit.
#