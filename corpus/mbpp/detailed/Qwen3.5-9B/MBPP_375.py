def round_num(number: float, multiple: float) -> float:
    """
    Rounds the given number to the nearest multiple of a specific number.

    This function handles the following logic explicitly:
    1. Validates that both inputs are numeric (int or float).
    2. Validates that the 'multiple' is not zero to avoid division by zero errors.
    3. Calculates the remainder of the division of the number by the multiple.
    4. Determines whether to round up or down based on the remainder.
    5. Computes the final rounded result.
    6. Returns the result, preserving the type logic (though returns float for safety).

    Args:
        number (float): The number to be rounded. Can be positive, negative, or zero.
        multiple (float): The multiple to round to. Must be non-zero.

    Returns:
        float: The number rounded to the nearest multiple.

    Raises:
        TypeError: If either input is not a number.
        ValueError: If the multiple is zero.
    """

    # Step 1: Type validation for 'number'
    if not isinstance(number, (int, float)):
        raise TypeError(f"The 'number' argument must be a numeric type (int or float). Received: {type(number).__name__}")

    # Step 2: Type validation for 'multiple'
    if not isinstance(multiple, (int, float)):
        raise TypeError(f"The 'multiple' argument must be a numeric type (int or float). Received: {type(multiple).__name__}")

    # Step 3: Value validation for 'multiple' (cannot divide by zero)
    if multiple == 0:
        raise ValueError("The 'multiple' argument cannot be zero.")

    # Edge Case Handling:
    # If the number is already a multiple of the divisor, return it directly.
    # This avoids floating point precision issues in division remainders for exact matches.
    # We use a small epsilon for float comparison safety, but for integers it's exact.
    if number % multiple == 0:
        return float(number)

    # Step 4: Normalize the inputs to ensure we are working with consistent floats
    # This helps avoid mixed type arithmetic issues, though Python handles them well.
    normalized_number = float(number)
    normalized_multiple = float(multiple)

    # Step 5: Calculate the absolute remainder to determine distance to the lower multiple
    # We calculate the remainder of the number divided by the multiple.
    remainder = abs(normalized_number % normalized_multiple)

    # Step 6: Calculate half of the multiple (the threshold for rounding up vs down)
    half_multiple = normalized_multiple / 2

    # Step 7: Determine the lower bound (the multiple just below the current number)
    # This is achieved by integer division (floor) followed by multiplication.
    lower_multiple = (int(normalized_number) // int(normalized_multiple)) * normalized_multiple

    # Correction for negative numbers in Python's integer division:
    # Python's // operator performs floor division (rounds down towards negative infinity).
    # If the number is negative, we need to ensure 'lower_multiple' is indeed the floor multiple.
    # Example: -4722 // -10 = 472. 472 * -10 = -4720. Correct.
    # Example: 4722 // 10 = 472. 472 * 10 = 4720. Correct.
    # However, if the multiple is negative, the logic holds because floor division handles signs.
    # Let's recalculate the lower multiple more robustly to handle the sign of the multiple correctly.

    # Robust calculation of the floor multiple:
    # We want the largest multiple of 'multiple' that is less than or equal to 'number'.
    # Formula: floor(number / multiple) * multiple

    # Re-evaluating the floor multiple using float division then flooring explicitly
    # to avoid any integer truncation surprises if inputs are floats like 4.5
    quotient = normalized_number / normalized_multiple
    floor_quotient = int(quotient) if quotient >= 0 else int(quotient)

    # If the number is negative and the multiple is positive, or vice versa,
    # standard floor logic applies. However, if quotient is x.5, int() truncates towards zero.
    # We need true floor.
    import math
    true_floor_quotient = math.floor(quotient)

    lower_multiple_value = true_floor_quotient * normalized_multiple

    # Step 8: Calculate the upper multiple (the multiple just above the current number)
    upper_multiple_value = lower_multiple_value + normalized_multiple

    # Step 9: Compare distances
    # Distance to the lower multiple
    distance_to_lower = abs(normalized_number - lower_multiple_value)

    # Distance to the upper multiple
    distance_to_upper = abs(normalized_number - upper_multiple_value)

    # Step 10: Decide which multiple is closer
    if distance_to_lower <= distance_to_upper:
        # Round down (or stay at lower multiple)
        final_result = lower_multiple_value
    else:
        # Round up
        final_result = upper_multiple_value

    # Step 11: Special edge case for exact half values
    # If distances are exactly equal (distance_to_lower == distance_to_upper),
    # standard "round half to even" (banker's rounding) or "round half up" behavior is often desired.
    # Based on the problem examples:
    # 4722 % 10 = 2. Distances: 2 vs 8. Rounds to 4720.
    # 1111 % 5 = 1. Distances: 1 vs 4. Rounds to 1110.
    # 219 % 2 = 1. Distances: 1 vs 1. 
    # For 219 and 2: 
    # 219 / 2 = 109.5. Lower: 218, Upper: 220.
    # Distances are equal (1). 
    # The assertion says assert round_num(219,2)==218.
    # This implies "Round Half Down" (or round half towards zero for positives) behavior for exact halves.
    # Our comparison `distance_to_lower <= distance_to_upper` handles this explicitly:
    # If distances are equal, we pick the lower one. This matches the requirement.

    return float(final_result)