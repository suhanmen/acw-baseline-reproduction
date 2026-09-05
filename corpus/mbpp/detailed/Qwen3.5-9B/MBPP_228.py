def _validate_input(n: int, start_bit: int, end_bit: int) -> None:
    """
    Validates that the input parameters are integers and that
    the start_bit is less than or equal to end_bit.

    Raises:
        TypeError: If any argument is not an integer.
        ValueError: If start_bit is greater than end_bit.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Parameter 'n' must be an integer, got {type(n).__name__}")
    if not isinstance(start_bit, int) or isinstance(start_bit, bool):
        raise TypeError(f"Parameter 'start_bit' must be an integer, got {type(start_bit).__name__}")
    if not isinstance(end_bit, int) or isinstance(end_bit, bool):
        raise TypeError(f"Parameter 'end_bit' must be an integer, got {type(end_bit).__name__}")

    if start_bit > end_bit:
        raise ValueError(f"Parameter 'start_bit' ({start_bit}) cannot be greater than 'end_bit' ({end_bit})")


def _check_bit_set(number: int, bit_index: int) -> bool:
    """
    Checks if the bit at the specific zero-indexed position is set (1).
    Uses bitwise AND with a shifted 1.

    Returns:
        True if the bit is set (1), False otherwise.
    """
    mask = 1 << bit_index
    return (number & mask) != 0


def _check_all_bits_set(number: int, start_bit: int, end_bit: int) -> bool:
    """
    Iterates through the specified bit range [start_bit, end_bit] inclusive.
    Checks if every single bit in this range is set to 1.

    Returns:
        True if all bits in the range are set, False otherwise.
    """
    # Iterate from start_bit to end_bit inclusive
    for current_bit in range(start_bit, end_bit + 1):
        if not _check_bit_set(number, current_bit):
            # If even one bit is 0, the condition "all bits are set" fails
            return False
    return True


def all_Bits_Set_In_The_Given_Range(n: int, start_bit: int, end_bit: int) -> bool:
    """
    Checks whether all the bits are set (equal to 1) in the given range 
    [start_bit, end_bit] of the integer n.

    The problem description asks to check if bits are "unset" in the title,
    but the provided assertions clearly demonstrate that the function must
    return True only when bits are "set" (1). For example:
      - all_Bits_Set_In_The_Given_Range(4,1,2) -> 4 is '100' in binary.
        Bit 2 is 1, Bit 1 is 0. Wait, let's re-examine the assertions.

        Assertion 1: all_Bits_Set_In_The_Given_Range(4,1,2) == True
        4 in binary is ...00100.
        Indices: 0->0, 1->0, 2->1.
        Range [1, 2] means we check index 1 and index 2.
        Index 1 is 0. Index 2 is 1.
        If the range is [1, 2], bits are 0 and 1. Not all are set.
        However, if the range is interpreted as [start, end] inclusive...
        Let's check 17: binary 10001. Indices 0 and 4 are 1. Indices 1,2,3 are 0.
        Assertion 2: all_Bits_Set_In_The_Given_Range(17,2,4) == True.
        Range [2, 4] includes indices 2, 3, 4.
        Bit 4 is 1. Bit 3 is 0. Bit 2 is 0.
        This assertion fails if we interpret "all bits set" literally for 17.

        Let's re-read the title vs assertions carefully.
        Title: "check whether all the bits are unset"
        Assertions:
          4 (100) with range 1-2 returns True.
          17 (10001) with range 2-4 returns True.
          39 (100111) with range 4-6 returns False.

        Let's analyze 4 (binary 100):
          Bit 0: 0
          Bit 1: 0
          Bit 2: 1
          If range is [1, 2]: Bits are 0, 1.
          If the function returns True, it implies something specific.
          Maybe the question implies checking if bits are UNSET (0)?
          If so:
            4 (100): Range [1,2] -> Bit 1 is 0, Bit 2 is 1. Not all unset. Result should be False.
            But assertion says True.

        Let's reconsider the binary representation and indices.
        Perhaps the indices are 1-based?
        4 (decimal) = 100 (binary).
        If 1-based:
          Pos 1: 0
          Pos 2: 0
          Pos 3: 1
          Range [1, 2] -> Bits at pos 1 and 2. Both are 0.
          Condition "All bits are unset" (0) would be TRUE.

        Let's check 17 (decimal) = 10001 (binary).
        1-based positions:
          1: 1
          2: 0
          3: 0
          4: 0
          5: 1
        Range [2, 4]: Positions 2, 3, 4. All are 0.
        Condition "All bits are unset" (0) would be TRUE.
        This matches the assertion!

        Let's check 39 (decimal) = 100111 (binary).
        1-based positions:
          1: 1
          2: 1
          3: 1
          4: 0
          5: 0
          6: 1
        Range [4, 6]: Positions 4, 5, 6.
        Values: Pos 4 is 0, Pos 5 is 0, Pos 6 is 1.
        Condition "All bits are unset" (0) -> False because Pos 6 is 1.
        This matches the assertion (returns False)!

        Conclusion: The problem title says "unset", and the data confirms we are looking for bits to be 0.
        However, the parameter names in the assertions (like `all_Bits_Set...`) are confusingly named compared to the logic required.
        The logic required by the assertions is: "Check if all bits in the 1-based range [start_bit, end_bit] are 0 (unset)."

        Wait, standard programming convention is 0-based indexing. 
        If I use 0-based indexing on 4 (100):
          Indices 0, 1, 2. Values 0, 0, 1.
          Assertion 1: n=4, start=1, end=2. Range [1, 2].
          Index 1 is 0. Index 2 is 1.
          If checking for "unset" (0): Index 2 is 1, so result False.
          But assertion says True.

        If I use 0-based indexing on 17 (10001):
          Indices 0, 1, 2, 3, 4. Values 1, 0, 0, 0, 1.
          Assertion 2: n=17, start=2, end=4. Range [2, 4].
          Index 2 is 0. Index 3 is 0. Index 4 is 1.
          If checking for "unset" (0): Index 4 is 1, so result False.
          But assertion says True.

        The ONLY way these assertions pass with "unset" logic is if the indexing is 1-based.
        OR, the problem statement has a typo in the function name or logic, and it actually wants to check for "set" bits, but the inputs provided in the prompt text are inconsistent with the name "all_Bits_Set".

        Let's try the "All Bits Set" logic with 0-based indexing again, maybe I misread the binary.
        4 = 100. Indices: 0(0), 1(0), 2(1).
        Range [1, 2]: Bit 1 is 0, Bit 2 is 1. Not all set.

        Is it possible the problem considers the bits excluding the most significant bit? No, that's non-standard.

        Let's reconsider the "All Bits Unset" logic with 0-based indexing but different interpretation of "range".
        Maybe range is (start, end) exclusive?
        4 (100), range (1, 2) -> index 1 only. Bit 1 is 0. Unset? Yes.
        17 (10001), range (2, 4) -> indices 2, 3. Bits are 0, 0. Unset? Yes.
        39 (100111), range (4, 6) -> indices 4, 5. Bits are 0, 1. Unset? No (bit 5 is 1).
        This works perfectly for 0-based indexing with EXCLUSIVE end.

        Let's re-verify 39 (100111) with 0-based indexing.
        Binary: 100111
        Index:  543210
        Value:  100111

        Assertion 3: n=39, start=4, end=6.
        If exclusive end: Range [4, 5].
        Index 4 is 1.
        Index 5 is 0.
        Wait, 39 = 32 + 4 + 2 + 1 = 100111.
        Index 0: 1
        Index 1: 1
        Index 2: 1
        Index 3: 0
        Index 4: 0
        Index 5: 1

        Let's recount 39.
        39 = 32 (2^5) + 7 (2^2 + 2^1 + 2^0).
        So bits set are 5, 2, 1, 0.
        Binary: 100111.
        Pos: 5 4 3 2 1 0
        Val: 1 0 0 1 1 1

        Check "All Bits Unset" logic with EXCLUSIVE end (Python style slicing):
        Case 39, 4, 6: Range [4, 5). Indices 4 only.
        Index 4 value is 0.
        Is it unset? Yes.
        Result should be True.
        But Assertion says False.

        Okay, let's try INCLUSIVE end with 0-based indexing, but checking for "SET" (1)?
        Case 4, 1, 2: Indices 1, 2. Values 0, 1. All set? No. (Asserts True).

        Let's try INCLUSIVE end with 1-based indexing, checking for "SET" (1)?
        4 (100) -> 1-based: 1:0, 2:0, 3:1.
        Range [1, 2]: Bits 1, 2. Values 0, 0. All set? No.

        Let's go back to the most robust interpretation: 
        The problem statement title says "unset". The assertions imply we are checking if bits are UNSET (0).
        The mapping that makes assertions 1, 2, 3 true is:
        1. n=4 (100), range [1, 2] -> True.
           If 1-based: Bits 1, 2 are 0, 0. All 0? Yes.
        2. n=17 (10001), range [2, 4] -> True.
           If 1-based: Bits 2, 3, 4 are 0, 0, 0. All 0? Yes.
        3. n=39 (100111), range [4, 6] -> False.
           If 1-based: Bits 4, 5, 6.
           Binary 39: 100111 (6 bits).
           1-based indices mapping:
             Pos 6: 1
             Pos 5: 0
             Pos 4: 0
             Pos 3: 1
             Pos 2: 1
             Pos 1: 1
           Range [4, 6]: Pos 4 (0), Pos 5 (0), Pos 6 (1).
           Are all 0? No, Pos 6 is 1. Result False.

        This mapping (1-based indexing, checking if bits are 0/unset)