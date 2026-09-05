def multiply_int(a: int, b: int) -> int:
    """
    Multiplies two integers without using the * operator.

    Handles:
    - Positive integers
    - Negative integers
    - Zero
    - Large integers (within Python's arbitrary precision limits)

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of a and b.

    Raises:
        TypeError: If either argument is not an integer.
    """
    # Step 1: Validate input types explicitly
    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError(f"First operand must be an integer, got {type(a).__name__}")

    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError(f"Second operand must be an integer, got {type(b).__name__}")

    # Step 2: Handle the edge case where either number is zero
    # Any number multiplied by zero is zero.
    if a == 0 or b == 0:
        return 0

    # Step 3: Determine the absolute values for the core multiplication logic
    # We will calculate the magnitude separately and handle the sign at the end.
    abs_a = abs(a)
    abs_b = abs(b)

    # Step 4: Determine the sign of the result
    # The result is negative if one of the operands is negative,
    # but not both (unless one is zero, which we already handled).
    # Logic: (a < 0) ^ (b < 0) results in True if exactly one is negative.
    is_negative = (a < 0) != (b < 0)

    # Step 5: Core multiplication using repeated addition
    # We choose the smaller absolute value to be the counter to minimize iterations.
    counter = abs_a
    multiplier = abs_b

    if counter > multiplier:
        # Swap to minimize the number of addition operations
        counter, multiplier = multiplier, counter

    # Initialize result accumulator
    result = 0

    # Step 6: Perform repeated addition
    # We add 'multiplier' to 'result', 'counter' times.
    for _ in range(counter):
        result += multiplier

    # Step 7: Apply the sign to the calculated magnitude
    if is_negative:
        result = -result

    # Step 8: Return the final result
    return result


if __name__ == "__main__":
    # Basic verification of the provided assertions
    assert multiply_int(10, 20) == 200
    assert multiply_int(5, 10) == 50
    assert multiply_int(4, 8) == 32

    # Additional edge case tests to ensure robustness
    assert multiply_int(0, 100) == 0
    assert multiply_int(-5, 5) == -25
    assert multiply_int(-5, -5) == 25
    assert multiply_int(1, 1000000) == 1000000
    assert multiply_int(-1, 100) == -100