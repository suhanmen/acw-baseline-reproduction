def _is_odd_position(bit_position: int) -> bool:
    """
    Determines if a given bit position is odd (1-based indexing for human logic, 
    but implemented with 0-based indexing where index i corresponds to 2^i).

    In standard binary representation:
    - Position 0 (2^0 = 1) -> Even position index -> Keep as is
    - Position 1 (2^1 = 2) -> Odd position index -> Set to 1
    - Position 2 (2^2 = 4) -> Even position index -> Keep as is
    - Position 3 (2^3 = 8) -> Odd position index -> Set to 1

    This function returns True if the bit at the given 0-based index corresponds
    to an odd mathematical position (1st, 3rd, 5th... which are indices 0, 2, 4... 
    in 0-based counting) OR if the problem implies setting bits at odd indices (1, 3, 5...).

    Let's analyze the examples to determine the exact rule:
    10 (binary 1010) -> 15 (binary 1111)
       Bits at indices: 3 2 1 0
       Values:         1 0 1 0
       Result:         1 1 1 1
       Changes:
         Index 1 (value 0 -> 1): Index 1 is ODD.
         Index 2 (value 1 -> 1): Index 2 is EVEN. Kept.
         Index 3 (value 1 -> 1): Index 3 is ODD. Kept.

    20 (binary 10100) -> 21 (binary 10101)
       Bits at indices: 4 3 2 1 0
       Values:         1 0 1 0 0
       Result:         1 0 1 0 1
       Changes:
         Index 0 (value 0 -> 1): Index 0 is EVEN.
         Wait, let's re-evaluate based on the pattern.

    Let's look at the binary representation again carefully.
    10 = 0b1010. Bits set at indices 3 and 1.
    15 = 0b1111. Bits set at indices 3, 2, 1, 0.
    The missing bit in 10 compared to 15 is at index 2 and index 0.
    10 = 1*8 + 0*4 + 1*2 + 0*1.
    15 = 1*8 + 1*4 + 1*2 + 1*1.
    The bits that were 0 and became 1 are at index 0 and index 2.
    Indices 0 and 2 are EVEN numbers.

    20 = 0b10100. Bits set at indices 4 and 2.
    21 = 0b10101. Bits set at indices 4, 2, and 0.
    The bit that was 0 and became 1 is at index 0.
    Index 0 is EVEN.

    30 = 0b11110. Bits set at indices 4, 3, 2, 1.
    31 = 0b11111. Bits set at indices 4, 3, 2, 1, 0.
    The bit that was 0 and became 1 is at index 0.
    Index 0 is EVEN.

    Hypothesis: The problem asks to set all bits at EVEN indices (0, 2, 4...) to 1.
    The term "odd bits" in the problem description might refer to the value of the power of 2 
    being odd (i.e., 2^0=1 is odd, 2^2=4 is even, this doesn't fit) or it's a trick in naming.
    However, usually "odd bits" could mean bits at odd positions (1, 3, 5...).
    If we set odd positions (1, 3, 5...):
      10 (1010) -> bits at 1 and 3 are already set. Result should be 10. But expected is 15.
      So it's not odd positions.

    If we set even positions (0, 2, 4...):
      10 (1010): bit at 0 is 0 -> set to 1. bit at 2 is 1 -> keep. bit at 4 is 0 -> set to 1?
      Let's check 10 -> 15.
      10 = 1010 (binary). 
      Indices: 3(1), 2(0), 1(1), 0(0).
      Target 15 = 1111.
      Indices: 3(1), 2(1), 1(1), 0(1).
      Changes: Index 2 (was 0, became 1), Index 0 (was 0, became 1).
      Indices changed: 0, 2. These are EVEN indices.

      20 = 10100.
      Indices: 4(1), 3(0), 2(1), 1(0), 0(0).
      Target 21 = 10101.
      Indices: 4(1), 3(0), 2(1), 1(0), 0(1).
      Changes: Index 0 (was 0, became 1).
      Index 0 is EVEN.

      30 = 11110.
      Indices: 4(1), 3(1), 2(1), 1(1), 0(0).
      Target 31 = 11111.
      Indices: 4(1), 3(1), 2(1), 1(1), 0(1).
      Changes: Index 0 (was 0, became 1).
      Index 0 is EVEN.

    Conclusion: The requirement is to ensure all bits at EVEN indices (0, 2, 4, ...) are set to 1.
    The phrase "set all odd bits" in the prompt likely refers to the resulting bits 
    having the property of the number 1 (which is odd) at even positions, or it is simply 
    a misnomer in the problem statement where "odd bits" actually means "even positions".
    Regardless of the name, the transformation logic derived from the assertions is:
    Set bit at index i to 1 if i is even.

    Algorithm:
    1. Create a mask where bits at even indices (0, 2, 4...) are 1 and others are 0.
    2. OR the input number with this mask.

    How to create the mask?
    We can construct a mask by shifting 1 left by 0, 2, 4... up to the bit length of the number.
    OR we can observe a pattern:
    0, 2, 4, 6... correspond to powers 2^0, 2^2, 2^4... -> 1, 4, 16...
    Sum = 1 + 4 + 16 + 64 + ...
    This is a geometric series with ratio 4.
    Alternatively, we can just iterate through bits up to the maximum bit length of the input.

    Let's refine the "mask" generation to be safe and explicit.
    We need to determine the number of bits in the input to know the range.
    Then we construct a mask where bit i is 1 if i % 2 == 0.
    Finally, return input | mask.

    Edge cases:
    - Input is 0: 0 (binary 0). Max bits 1? Or 0? 
      If input is 0, bit length is 0? No, usually considered 1 bit (just 0). 
      If we process 0, even indices set: index 0 -> 1. Result 1.
      Is 0 -> 1 correct? The problem doesn't specify 0, but logically yes.
      However, standard bit_length of 0 is 0. We should handle 0 explicitly or ensure loop covers index 0.
      If bit_length is 0, loop doesn't run, mask is 0, result 0. This might be wrong if 0 should become 1.
      Let's assume standard behavior: if number is 0, we might want to treat it as having at least 1 bit position?
      Actually, 0 in binary is ...000. There are no set bits.
      The instruction "set all odd bits" (interpreted as even indices) for 0 means setting index 0 to 1.
      So 0 -> 1.
      To handle this, we can assume a mask of at least covering index 0.
      Or simpler: The problem constraints say "given number". 
      Let's check the constraints of typical bit manipulation problems.
      Usually, we iterate up to the bit length of the number.
      If n=0, bit_length is 0.
      If we strictly follow "up to bit_length", we get 0.
      But if the rule is "ensure even positions are 1", 0 (pos 0) is an even position.
      So 0 should become 1.
      We will handle n=0 as a special case or ensure our mask generation considers index 0 even if length is 0.
      Actually, a robust way is to assume the number exists in a space where position 0 is valid.
      Let's add a check: if n is 0, return 1? Or is 0 a valid input where we do nothing?
      Given "set all odd bits" (even indices), index 0 is an even index.
      If the number is 0, it has a 0 at index 0. It should become 1.
      So 0 -> 1.

    - Negative numbers: The problem examples are positive. 
      Python handles negative numbers with infinite leading 1s in two's complement.
      "Set all odd bits" on negative numbers would set infinite bits to 1?
      That would result in a very large negative number (still negative) or overflow logic?
      In Python, integers have arbitrary precision.
      If input is -1 (all 1s), result is -1.
      If input is -2 (...111110). Even indices 0, 2, 4... are 1, 1, 1... (already set).
      Wait, -2 is ...111110. Index 0 is 0. Index 2 is 1.
      So index 0 should be set. -2 | 1 = -1.
      However, the problem examples are strictly positive. 
      We will add validation to reject negative numbers to keep behavior predictable and consistent 
      with the "bit pattern" examples provided, or handle them by noting that setting bits 
      on negative numbers affects the sign bit (infinite loop of 1s).
      Given the examples are 10, 20, 30, I will restrict input to non-negative integers.

    - Non-integers: Validate type.
    - Non-integers (float, str, etc.): Raise TypeError.
    - Negative integers: Raise ValueError.
"""

def odd_bit_set_number(n: int) -> int:
    """
    Sets all bits at even positions (0, 2, 4, ...) to 1 for the given non-negative integer.

    Note: The problem statement refers to "odd bits", but the examples indicate that
    the operation is to ensure bits at even indices (0-based) are set to 1.
    Example: 10 (1010) -> 15 (1111). Indices 0 and 2 were 0, became 1. Both are even indices.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The integer with all even-positioned bits set to 1.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    # Validate type explicitly
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    # Validate range explicitly
    if n < 0:
        raise ValueError(f"Input must be a non-negative integer, got {n}")

    # Handle the specific edge case of 0 explicitly to ensure index 0 is considered
    # 0 has bit_length 0, but logically index 0 should be set if we follow the "even index" rule.
    # However, if n=0, the loop based on bit_length(0)=0 will not execute.
    # Let's verify the requirement for 0 again.
    # If the rule is "set bits at even indices", and 0 exists at index 0, then 0 -> 1.
    # But if we interpret the number as having no bits set, maybe no change?
    # Given the ambiguity, and the fact that 0 is a degenerate case, 
    # let's look at the pattern of "set odd bits"