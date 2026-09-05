def _is_odd_bit_set(n: int, bit_index: int) -> bool:
    """
    Check if the bit at the specified index is set (1) in the given number.

    Parameters:
    n (int): The number to check.
    bit_index (int): The index of the bit to check (0-indexed, from LSB).

    Returns:
    bool: True if the bit is set, False otherwise.
    """
    if bit_index < 0:
        raise ValueError("Bit index cannot be negative.")

    mask = 1 << bit_index
    return (n & mask) != 0


def _get_bit_index(value: int) -> int:
    """
    Determine the minimum number of bits required to represent the absolute value of the number.

    This calculates ceil(log2(|value| + 1)) for value != 0, and returns 1 for value == 0.
    This ensures we check every bit position from 0 up to the most significant bit.

    Parameters:
    value (int): The integer value.

    Returns:
    int: The highest bit index that needs to be considered (inclusive), or 0 if value is 0.
    """
    if value == 0:
        return 0

    abs_value = abs(value)
    # Count bits needed to represent the number.
    # If abs_value is 1, we need 1 bit (index 0).
    # If abs_value is 2, we need 2 bits (indices 0, 1).

    bit_index = 0
    temp = abs_value

    # Handle powers of 2 efficiently, though a loop is clearer for explicit logic.
    # We want the highest set bit index.
    while temp > 0:
        temp >>= 1
        bit_index += 1

    # bit_index is now the number of bits. The highest index is bit_index - 1.
    return bit_index - 1


def even_bit_toggle_number(n: int) -> int:
    """
    Toggles all bits at odd indices (1, 3, 5, ...) in the binary representation of n.
    Indices are 0-based, starting from the Least Significant Bit (LSB).

    Note: The problem description asks to "toggle all odd bits".
    In standard terminology:
    - LSB is index 0 (Even index)
    - Next bit is index 1 (Odd index)
    - Next bit is index 2 (Even index)
    - Next bit is index 3 (Odd index)

    The provided assertions confirm this interpretation:
    - 10 (1010) -> Toggle bits at indices 1 and 3 (both are 1). 
      Index 1 becomes 0, Index 3 becomes 0. Result: 1000 (8)? 
      Wait, let's re-evaluate the examples carefully.

    Assertion 1: even_bit_toggle_number(10) == 15
      10 in binary: ...001010
      Indices:      ...3210 (LSB at 0)
      Bit at 0: 0 (Even index) -> Keep
      Bit at 1: 1 (Odd index)  -> Toggle to 0
      Bit at 2: 0 (Even index) -> Keep
      Bit at 3: 1 (Odd index)  -> Toggle to 0
      Result would be ...001000 (8). This does NOT match 15.

      Let's try the alternative interpretation: Toggle bits at EVEN indices (0, 2, 4...).
      10 (1010):
      Index 0: 0 -> Toggle to 1
      Index 1: 1 -> Keep (Odd index)
      Index 2: 0 -> Toggle to 1
      Index 3: 1 -> Keep (Odd index)
      Result: 1111 (15). MATCH!

      Assertion 2: even_bit_toggle_number(20) == 1
      20 in binary: 10100
      Indices:     43210
      Index 0: 0 -> Toggle to 1
      Index 1: 0 -> Keep
      Index 2: 1 -> Toggle to 0
      Index 3: 0 -> Keep
      Index 4: 1 -> Toggle to 0
      Result: 00001 (1). MATCH!

      Assertion 3: even_bit_toggle_number(30) == 11
      30 in binary: 11110
      Indices:     43210
      Index 0: 0 -> Toggle to 1
      Index 1: 1 -> Keep
      Index 2: 1 -> Toggle to 0
      Index 3: 1 -> Toggle to 0
      Index 4: 1 -> Toggle to 0
      Result: 01011 (11). MATCH!

    Conclusion: The function name "even_bit_toggle_number" implies toggling bits at EVEN indices (0, 2, 4...),
    despite the generic phrasing "toggle all odd bits" which was ambiguous or poorly phrased in the prompt description.
    The assertions definitively prove that we must toggle bits at even positions (0-indexed from LSB).

    Parameters:
    n (int): The integer number to process.

    Returns:
    int: The number with bits at even indices toggled.
    """

    # Validate input type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    # Handle zero explicitly
    if n == 0:
        # 0 has no bits set. Toggling even indices of 0 results in all 0s (since no bits are set to flip to 1).
        # Binary of 0: ...0000
        # Indices 0, 2, 4... are 0. Toggle -> 1.
        # WAIT.
        # If I toggle a 0 at an even index, it becomes 1.
        # But how many bits do we consider for 0?
        # If we consider infinite bits, the result would be infinite 1s (divergent).
        # However, standard arithmetic operations imply a finite representation.
        # Usually, "number of bits" refers to the bits needed to represent the magnitude.
        # For 0, magnitude is 0, bits needed is 0.
        # If we treat 0 as having 0 bits, then no even indices exist to toggle. Result 0.
        # Let's check the logic with the other examples.
        # Example 20 (10100): Highest index is 4. We toggle 0, 2, 4.
        # If input is 0, highest index is 0 (based on _get_bit_index logic returning 0).
        # If highest index is 0, we check index 0.
        # But wait, if the number is 0, there is technically no '1' bit.
        # Does the prompt imply we only toggle bits that are currently 1?
        # "Toggle all odd bits" usually means "Flip the state of bits at odd positions".
        # If the state is 0, it becomes 1. If 1, it becomes 0.
        # If we do this for 0, and we consider index 0, it becomes 1.
        # But usually, these problems assume we only operate on the significant bits.
        # If 0 has 0 significant bits, we do nothing. Result 0.
        # Let's assume the definition of "bits of a number" excludes leading zeros.
        # Therefore, 0 has no bits. No toggles occur. Result 0.

        return 0

    # Determine the range of bit indices to consider.
    # We only care about bits from index 0 up to the Most Significant Bit (MSB).
    highest_bit_index = _get_bit_index(n)

    # If highest_bit_index is less than 0 (should not happen for non-zero based on helper), handle gracefully.
    if highest_bit_index < 0:
        return 0

    # Initialize result as a copy of the input number to preserve unchanged bits.
    result = n

    # Iterate through all bit indices up to the highest bit.
    current_index = 0
    while current_index <= highest_bit_index:
        # Check if the current index is even.
        if current_index % 2 == 0:
            # Get the bit at current_index
            is_bit_set = (n & (1 << current_index)) != 0

            # Toggle logic:
            # If bit is 1, subtract 2^index (set to 0)
            # If bit is 0, add 2^index (set to 1)
            if is_bit_set:
                mask = 1 << current_index
                result = result - mask
            else:
                mask = 1 << current_index
                result = result + mask
        # If index is odd, we do nothing (as established by the assertions).

        current_index += 1

    return result