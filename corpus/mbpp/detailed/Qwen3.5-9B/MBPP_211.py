def count_Num(n: int) -> int:
    """
    Counts the number of integers in the range [0, 2^n - 1] (inclusive)
    where both the 0-th bit (least significant bit) and the n-th bit are set.

    This function interprets the problem as finding how many numbers x exist
    such that:
      0 <= x < 2**n
      (x & 1) == 1   (0-th bit is set)
      (x >> n) & 1 == 1 (n-th bit is set)

    Note: For n=0, the range is [0, 0]. The 0-th bit check and 0-th bit check
    are the same. However, the problem assertions suggest n>=1 for meaningful
    "0-th and n-th" distinction, but we handle n=0 logically:
      Range: [0, 2^0 - 1] = [0, 0].
      x = 0. Binary: ...0000.
      0-th bit is 0. n-th bit (0-th) is 0.
      Count = 0.
    But let's look at assertions:
      count_Num(2) == 1: Range [0, 3]. Numbers with bit 0 and bit 2 set.
        0: 000 (No)
        1: 001 (Bit 0 yes, Bit 2 no)
        2: 010 (Bit 0 no, Bit 2 no)
        3: 011 (Bit 0 yes, Bit 2 no) -> Wait, 3 is 11 in binary. Bit 0 is 1. Bit 1 is 1. Bit 2 is 0.
        So for n=2, range is 0..3. Max bit index is 1. Bit 2 is always 0. Count should be 0?

    Let's re-read the assertions carefully.
    assert count_Num(2) == 1
    assert count_Num(3) == 2
    assert count_Num(1) == 1

    Hypothesis 1: The problem means numbers from 1 to 2^n? Or maybe the bits are 1-indexed?
    If bits are 1-indexed:
      n=1: Range [1, 2]. Check bit 1 and bit 1? Or bit 0 and bit 1?
      Usually "0-th and n-th" means indices 0 and n.

    Let's try to reverse engineer from assertions.
    n=1: Result 1. Range [0, 1].
      x=0: 00. Bit 0=0, Bit 1=0.
      x=1: 01. Bit 0=1, Bit 1=0.
      Neither satisfies "Bit 0 and Bit 1 set". 
      Unless the range is different. Maybe [1, 2^n]? 
      If range is [1, 2]: 
        x=1 (01): Bit 0=1, Bit 1=0.
        x=2 (10): Bit 0=0, Bit 1=1.
        Still 0.

    Hypothesis 2: Maybe the problem implies "0-th bit" and "n-th bit" where n is the input,
    but the range is actually up to some larger number? No, "nth" usually defines the constraint size.

    Hypothesis 3: Maybe the indices are 1-based in the problem statement context?
      "0-th and n-th" -> maybe they mean the 1st bit and (n+1)-th bit?
      Or maybe "0-th" means LSB and "n-th" means the bit at position n.

    Let's look at n=2, result=1.
    If we consider numbers up to 2^(n+1) - 1?
    Range [0, 7]. Check bit 0 and bit 2.
    Numbers with bit 0 set: 1, 3, 5, 7.
    Numbers with bit 2 set: 4, 5, 6, 7.
    Intersection (bit 0 AND bit 2): 5 (101). Count = 1.
    This matches assert count_Num(2) == 1.

    Let's check n=3, result=2.
    Range [0, 15]. Check bit 0 and bit 3.
    Bit 0 set: 1, 3, 5, 7, 9, 11, 13, 15.
    Bit 3 set (value 8): 8, 9, 10, 11, 12, 13, 14, 15.
    Intersection: 9 (1001), 11 (1011), 13 (1101), 15 (1111).
    Count = 4.
    But assertion says count_Num(3) == 2.
    So the range [0, 2^(n+1)-1] is incorrect for n=3.

    Let's re-evaluate n=3, result=2 with range [0, 2^n - 1] = [0, 7].
    Check bit 0 and bit 3.
    In range [0, 7], bit 3 is always 0 (max value 7 is 0111).
    Count would be 0. Assertion says 2.

    Maybe the problem is: Count numbers from 1 to n?
    n=2: Count in [1, 2] where bit 0 and bit 2 set? Impossible.

    Alternative interpretation:
    Maybe "n-th bit" refers to the bit at index (n-1) if using 1-based counting for "n-th"?
    If n=2, check bit 0 and bit 1 (since 2nd bit is index 1).
    Range? If range is 0 to 2^n-1 (which is 3):
      0: 00 (No)
      1: 01 (Bit 0 yes, Bit 1 no)
      2: 10 (Bit 0 no, Bit 1 yes)
      3: 11 (Bit 0 yes, Bit 1 yes) -> Count 1. Matches n=2.
    If n=3, check bit 0 and bit 2 (3rd bit is index 2).
    Range 0 to 7 (2^3-1).
      0: 000 (No)
      1: 001 (Bit 0 yes, Bit 2 no)
      2: 010 (Bit 0 no, Bit 2 no)
      3: 011 (Bit 0 yes, Bit 2 no)
      4: 100 (Bit 0 no, Bit 2 yes)
      5: 101 (Bit 0 yes, Bit 2 yes) -> YES
      6: 110 (Bit 0 no, Bit 2 yes)
      7: 111 (Bit 0 yes, Bit 2 yes) -> YES
      Count = 2. Matches n=3.
    If n=1, check bit 0 and bit 0 (1st bit is index 0).
    Range 0 to 1.
      0: 0 (No)
      1: 1 (Bit 0 yes, Bit 0 yes) -> YES
      Count = 1. Matches n=1.

    Conclusion:
    The problem asks for the count of numbers in the range [0, 2^n - 1] (or possibly [1, 2^n-1] but 0 fails anyway)
    such that the 0-th bit (LSB) and the (n-1)-th bit (the most significant bit within the n bits) are set.
    Essentially, we are looking for numbers in the range [0, 2^n - 1] where:
      (x & 1) == 1  AND  (x >> (n-1)) & 1 == 1.

    Let's verify the logic mathematically.
    Range: 0 to 2^n - 1. Total 2^n numbers.
    Condition 1: LSB (bit 0) is 1. This cuts the space in half. 2^(n-1) numbers.
    Condition 2: MSB (bit n-1) is 1. Since we are in range [0, 2^n-1], the MSB being 1 means the number is in [2^(n-1), 2^n - 1].
    Intersection:
      We need LSB=1 AND MSB=1.
      MSB=1 implies numbers are of form 1xxxx... (n bits).
      LSB=1 implies numbers are of form ...x1.
      So we need 1xx...x1.
      The middle (n-2) bits can be anything.
      Number of free bits = n - 2.
      Total count = 2^(n-2).

    Check n=2: 2^(2-2) = 2^0 = 1. Matches.
    Check n=3: 2^(3-2) = 2^1 = 2. Matches.
    Check n=1: 2^(1-2) = 2^-1 = 0.5? 
      Wait, for n=1, the "MSB" is bit 0. The "LSB" is bit 0.
      We need bit 0 set.
      Range [0, 1].
      x=1 (binary 1): Bit 0 is 1. Bit 0 (as MSB) is 1. Count 1.
      Formula 2^(n-2) fails for n=1.

    Why does n=1 work manually?
    Range [0, 1].
    x=1. Binary '1'. 
    Bit 0 is 1.
    Bit n-1 = Bit 0 is 1.
    Intersection is just {1}. Count 1.
    My formula derivation assumed n >= 2 to have distinct MSB and LSB positions.
    If n=1, MSB index = 0, LSB index = 0. They are the same.
    Condition: (x & 1) == 1 AND (x & 1) == 1 => (x & 1) == 1.
    Count in [0, 1] where x is odd: 1 (number 1).

    So the logic is:
    If n == 0:
       Range [0, 0]. Check bit 0 and bit -1? 
       Problem says "0-th and n-th". If n=0, it's bit 0 and bit 0.
       x=0. Bit 0 is 0. Count 0.
       But based on pattern n=1->1, n=2->1, n=3->2.
       If n=0, range [0, 0]. x=0. Bit 0 is 0. Count 0.

    General Algorithm:
    1. Validate n is a non-negative integer.
    2. Define range_upper = 2**n. Iterate x from 0 to range_upper - 1.
    3. Check if (x & 1) is true.
    4. Check if (x >> (n - 1)) & 1 is true. 
       Special case: if n=1, shift by 0.
       Special case: if n=0, shift by -1? 
       If n=0, condition is bit 0 and bit 0.
       Let's handle n=0 separately or ensure shift logic works.
       In Python, x >> -1 raises ValueError? No, x >> -1 is valid?
       Actually, in Python, negative shift count raises ValueError: negative shift count.
       So n=0 needs special handling.

    However, the mathematical pattern for n >= 1 seems to be:
      Count = 2^(n-2) if n > 1
      Count = 1 if n == 1
      Count = 0 if n == 0

    Wait, let's re-verify n=1 with the shift logic.
    n=1. Check bit 0 and bit 0.
    x in [0, 1].
    x=1: bit 0 is 1. (1 >> 0) & 1 is 1.
    Count 1. Correct.

    So the code can be:
    Iterate 0 to 2^n - 1.
    Check conditions.

    But wait, is iterating 2^n too slow for large n?
    The problem asks to write a function satisfying assertions. It doesn't specify constraints on n.
    "Production-grade" usually implies efficiency.
    We can compute the result mathematically.

    Case n=0:
      Range [0, 0]. x=0.
      Bit 0: 0.
      Bit 0 (n-th): 0.
      Count 0.
    Case n=1:
      Range [0, 1].
      x=1 satisfies.
      Count 1.
    Case n>=2