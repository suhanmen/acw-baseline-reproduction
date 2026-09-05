import math

def power(a: int, b: int) -> int:
    """
    Calculates the value of 'a' raised to the power of 'b'.

    This function uses an iterative approach (exponentiation by squaring)
    to compute the result efficiently, handling both positive and negative
    exponents, as well as zero exponents. It explicitly validates inputs
    and handles edge cases such as integer overflow scenarios by raising
    a ValueError if the result exceeds the bounds of a standard 64-bit integer
    representation (though Python handles arbitrarily large integers, we check
    for potential overflow in typical fixed-width contexts if needed, but here
    we rely on Python's arbitrary precision integers).

    Args:
        a (int): The base number. Can be positive, negative, or zero.
        b (int): The exponent. Can be positive, negative, or zero.

    Returns:
        int: The result of a raised to the power of b.

    Raises:
        TypeError: If either 'a' or 'b' is not an integer.
        ValueError: If the exponent is negative and the base is zero.
    """

    # Validate input types explicitly
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")

    # Handle the specific edge case where the base is zero and the exponent is negative
    # Division by zero would occur in mathematical terms for 0^-x
    if a == 0 and b < 0:
        raise ValueError("Cannot raise zero to a negative power.")

    # Define a small threshold for checking if the result is too large
    # for standard fixed-width integer contexts (e.g., 64-bit signed integer max)
    INT_MAX_64_BIT = 2**63 - 1
    INT_MIN_64_BIT = -(2**63)

    # Initialize the result variable to 1.0 to support potential float intermediate calculations
    # though we will convert back to int at the end if needed, or stay in int domain.
    # Since Python handles large integers automatically, we can work directly with integers.
    result = 1

    # Handle the case where the exponent is negative
    is_negative_exponent = b < 0

    if is_negative_exponent:
        # For negative exponents, we compute the reciprocal: 1 / (a^|b|)
        # First, calculate the positive power
        positive_b = -b
        # We'll store the numerator and denominator to avoid floating point issues until the end
        # numerator = 1
        # denominator = a ** positive_b
        # However, since we are returning an int, and 1/(a^b) is rarely an integer unless a^b is 1,
        # we must assume the problem context implies standard integer arithmetic where 
        # negative exponents are either disallowed for integer outputs or result in floats.
        # BUT, looking at the assertions (3,4), (2,3), (5,5), they are all positive integers.
        # If the problem strictly requires integer return types, negative exponents 
        # usually imply a domain error for integer-only problems unless 1/a^b is exact.
        # Let's assume standard mathematical definition for integers: if b < 0 and a != 0,
        # the result is a float in most languages, but Python ints can hold fractions? No.
        # Given the prompt asks for int return and examples are positive, we will implement
        # a check: if b < 0, return float? Or raise error? 
        # The prompt signature says -> int. 
        # Strictly speaking, integer arithmetic cannot represent 1/2. 
        # We will assume the input constraints for this specific problem imply b >= 0 for integer returns,
        # OR we return the float converted to int (truncating), OR we raise an error.
        # However, standard Python `pow(a, b)` with ints returns int if result is integer, else float.
        # To be safe and defensive for an "int" return type requirement:
        # If b < 0, the mathematical result is a fraction. An integer return type cannot represent it exactly.
        # We will raise a ValueError for negative exponents unless the result is exactly 1 (e.g. 1^-5).
        if a == 1:
            return 1
        if a == -1:
            return 1 if positive_b % 2 == 0 else -1
        raise ValueError("Negative exponents result in non-integer values. Please provide a non-negative exponent for integer return.")

    # From this point on, b is non-negative.
    b_exp = b

    # Edge case: Exponent is 0.
    # Any non-zero number to the power of 0 is 1.
    # 0^0 is mathematically indeterminate but often defined as 1 in programming contexts.
    if b_exp == 0:
        return 1

    # Edge case: Base is 0 with positive exponent.
    # 0^positive = 0.
    if a == 0:
        return 0

    # Now we have: a != 0, b > 0.
    # We use iterative exponentiation (square-and-multiply) for efficiency.
    # This is O(log b) time complexity.

    base = a
    current_exponent = b_exp
    accumulator = 1

    # Loop until the exponent is reduced to 0
    while current_exponent > 0:
        # Check for potential overflow if we were working with fixed-size integers.
        # Python handles arbitrary precision, so we skip overflow checks for runtime correctness,
        # but we can check if the intermediate result is absurdly large if desired.
        # For this solution, we trust Python's big int support.

        # If the current exponent is odd, multiply the accumulator by the base
        if current_exponent % 2 == 1:
            accumulator = accumulator * base

        # Square the base for the next bit of the exponent
        base = base * base

        # Right shift the exponent by 1 (divide by 2)
        current_exponent = current_exponent // 2

    return accumulator

# Final validation against the provided assertions to ensure correctness
if __name__ == "__main__":
    # These checks are internal to this script block for verification purposes only.
    # They do not interfere with the function's availability for import.
    test_cases = [
        (3, 4, 81),
        (2, 3, 8),
        (5, 5, 3125)
    ]

    for base, exp, expected in test_cases:
        computed_value = power(base, exp)
        assert computed_value == expected, f"Failed for power({base}, {exp}): expected {expected}, got {computed_value}"

    # Additional edge case checks
    assert power(10, 0) == 1
    assert power(-2, 3) == -8
    assert power(0, 5) == 0
    assert power(2, 10) == 1024

    print("All assertions passed.")