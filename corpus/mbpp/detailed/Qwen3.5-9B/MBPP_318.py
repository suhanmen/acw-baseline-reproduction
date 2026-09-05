import math
from typing import Union

def max_volume(total_sum: int) -> int:
    """
    Calculates the maximum possible volume of a cuboid where the sum of its
    three side lengths (length, width, height) equals the given total_sum.

    The problem reduces to finding three positive integers (x, y, z) such that:
    1. x + y + z = total_sum
    2. Volume V = x * y * z is maximized.

    Mathematical Insight:
    For a fixed sum, the product of numbers is maximized when the numbers are
    as close to each other as possible (i.e., close to total_sum / 3).

    Since the sum of sides for a valid non-degenerate cuboid must be at least
    3 (minimum sides 1, 1, 1), any sum less than 3 yields a volume of 0.

    Args:
        total_sum (int): The sum of the three side lengths. Must be a non-negative integer.

    Returns:
        int: The maximum volume of the cuboid. Returns 0 if no valid cuboid can be formed
             (e.g., sum < 3).

    Raises:
        TypeError: If the input is not an integer or is negative.
    """

    # Step 1: Input Validation
    # Ensure the input is an integer.
    if not isinstance(total_sum, int):
        raise TypeError(f"Input must be an integer, received: {type(total_sum).__name__}")

    # Ensure the input is non-negative.
    # While negative numbers don't make physical sense for lengths,
    # the type check covers most logic errors, but an explicit check is defensive.
    if total_sum < 0:
        raise ValueError(f"Input must be non-negative, received: {total_sum}")

    # Step 2: Handle degenerate cases where no positive integer cuboid exists.
    # The smallest valid cuboid has sides 1, 1, 1, which sums to 3.
    if total_sum < 3:
        return 0

    # Step 3: Calculate the ideal float distribution.
    # To maximize x*y*z given x+y+z=S, x, y, and z should be as close to S/3 as possible.
    ideal_value = total_sum / 3.0

    # Step 4: Determine the base integer part for all sides.
    # We will distribute the remainder to some of the sides to make them as close as possible.
    base_side = int(math.floor(ideal_value))

    # Step 5: Calculate the remainder to be distributed.
    # This represents how much extra we can add to the sides above the base_side.
    remainder = total_sum - (base_side * 3)

    # Step 6: Generate the optimal side lengths based on the remainder.
    # We want to distribute the 'remainder' (0, 1, or 2) by adding +1 to 'remainder' sides.
    # Since remainder is small (0 to 2), we simply create a list starting with base_side
    # and increment the first 'remainder' elements.

    # Initialize sides with the base value
    side_a = base_side
    side_b = base_side
    side_c = base_side

    # Explicitly add the remainder to specific sides to maximize product.
    # Adding to the smallest numbers first ensures they remain closest to each other.
    # Since all start at base_side, order doesn't matter for addition, 
    # but we do it explicitly for clarity.

    if remainder >= 1:
        side_a += 1
    if remainder >= 2:
        side_b += 1

    # Calculate the third side.
    # Mathematically, side_c must take whatever is left to ensure the sum is exact.
    # In our construction: 
    # Total = (base + r1) + (base + r2) + base 
    #       = 3*base + r1 + r2 + 0
    # We know Total = 3*base + remainder (where remainder = r1 + r2).
    # So the sum is guaranteed to be correct by construction.

    # Step 7: Calculate the volume.
    volume = side_a * side_b * side_c

    # Step 8: Return the result.
    return volume

# --- Verification of Assertions ---
# These are internal checks to ensure the function behaves as requested by the prompt.
# They are not part of the final output block but help confirm logic during development.
if __name__ == "__main__":
    # Test Case 1: max_volume(8) == 18
    # Ideal sum/3 = 2.66. Sides should be 2, 3, 3. Sum=8. Vol=18.
    result_8 = max_volume(8)
    assert result_8 == 18, f"Failed for 8: expected 18, got {result_8}"

    # Test Case 2: max_volume(4) == 2
    # Ideal sum/3 = 1.33. Sides should be 1, 1, 2. Sum=4. Vol=2.
    result_4 = max_volume(4)
    assert result_4 == 2, f"Failed for 4: expected 2, got {result_4}"

    # Test Case 3: max_volume(1) == 0
    # Sum < 3, impossible to have positive integer sides.
    result_1 = max_volume(1)
    assert result_1 == 0, f"Failed for 1: expected 0, got {result_1}"

    print("All assertions passed.")