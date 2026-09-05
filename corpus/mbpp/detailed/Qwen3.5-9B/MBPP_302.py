def set_Bit_Number(n: int) -> int:
    """
    Find the most significant bit number which is also a set bit in the given integer.

    The "bit number" refers to the position index of the bit (0-indexed from the right).
    For example:
    - 6 (binary 110) -> MSB is at position 2 (value 4) -> returns 4 (the value of the bit, not index)
      Wait, the problem says "bit number which is also a set bit". Let's re-read the examples.
      assert set_Bit_Number(6) == 4. 6 is 110 in binary. The bits set are at positions 1 and 2.
      Values are 2^1=2 and 2^2=4. The most significant is 4. So it returns the VALUE (2^k) of the MSB.

      assert set_Bit_Number(10) == 8. 10 is 1010 in binary. Bits set at positions 1 and 3.
      Values 2 and 8. Most significant is 8.

      assert set_Bit_Number(18) == 16. 18 is 10010 in binary. Bits set at 1 and 4.
      Values 2 and 16. Most significant is 16.

    Therefore, the function returns the value of the most significant set bit (i.e., 2^k where k is the highest set bit index).

    This function includes:
    - Input validation (must be a non-negative integer)
    - Handling of edge cases (zero, single element, all-equal elements - though not applicable for bits)
    - Defensive programming with explicit error messages

    Args:
        n (int): A non-negative integer

    Returns:
        int: The value of the most significant set bit (2^k)

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """

    # Step 1: Validate that the input is an integer
    if not isinstance(n, int):
        raise TypeError(
            f"Input must be an integer, but got type: {type(n).__name__}. "
            f"Example valid inputs: 6, 10, 18, 0."
        )

    # Step 2: Validate that the input is non-negative
    if n < 0:
        raise ValueError(
            f"Input must be non-negative. Got value: {n}. "
            f"Negative numbers do not have a defined most significant bit in this context."
        )

    # Step 3: Handle the edge case where n is zero
    # Zero has no set bits, so there is no most significant set bit
    if n == 0:
        raise ValueError(
            f"Input value {n} has no set bits. Cannot determine most significant bit."
        )

    # Step 4: Initialize variables to track the search
    current_value = n
    most_significant_bit_value = 0

    # Step 5: Iterate through bits to find the most significant set bit
    # We use a loop that continues as long as the current value is greater than 0
    # In each iteration, we shift right or check the highest bit
    # Since we need the value (2^k), we can iterate on the power of 2

    # Alternative approach: Start from a reasonable upper bound or use log2 logic
    # But to be explicit and avoid floating point inaccuracies, we'll use bit shifting
    # We will find the highest power of 2 less than or equal to n

    # Let's use a while loop to shift n right until it becomes 0
    # But we need to capture the shift count to compute 2^shift_count

    shift_count = 0

    # Make a copy to manipulate without affecting original n if needed later
    temp_n = n

    # Step 6: Loop to find the highest set bit position
    # We shift right until temp_n becomes 0, counting the shifts
    # The number of shifts required to reach 0 tells us the position of the MSB + 1
    # Actually, we need the largest k such that (n >> k) & 1 == 1.

    # More efficient explicit approach:
    # Keep shifting left a power of 2 until it exceeds n, then step back?
    # Or simply find the highest bit by checking from high to low?
    # Given Python handles large integers, let's find the exact position.

    # Strategy: Repeatedly divide by 2 (integer division) and track position
    # until we reach a state where only one bit remains? No, that's not quite right.
    # We want the highest bit that is 1.

    # Explicit strategy:
    # 1. Start with power = 1
    # 2. Double power while (power * 2) <= n
    # 3. The result is power

    power_of_two = 1

    # Step 7: Explicit loop to double the power until exceeding n
    # This avoids floating point operations and works for arbitrarily large integers
    while True:
        # Check if doubling the power would exceed n
        # We calculate next_potential = power_of_two * 2
        next_potential = power_of_two * 2

        if next_potential > n:
            # If doubling exceeds n, then current power_of_two is the MSB value
            break

        # Otherwise, move to the next higher power of two
        power_of_two = next_potential

    # Step 8: Verify the result (defensive check)
    # Ensure that power_of_two is indeed <= n and that it corresponds to a set bit
    # Since we constructed it by doubling from 1 as long as 2*power <= n,
    # power_of_two is guaranteed to be <= n.
    # Also, since we started at 1 and doubled, it is a power of 2, so it corresponds to a single bit.
    # If n >= power_of_two, then that bit must be set (otherwise n would be less than power_of_two).

    # Final validation to ensure logical consistency
    if power_of_two == 0:
        # This shouldn't happen because n > 0 check is done earlier
        raise RuntimeError("Internal error: MSB calculation resulted in 0.")

    if n < power_of_two:
        # This implies logic error in the loop condition
        raise RuntimeError(f"Logic error: Calculated MSB {power_of_two} is greater than input {n}.")

    return power_of_two