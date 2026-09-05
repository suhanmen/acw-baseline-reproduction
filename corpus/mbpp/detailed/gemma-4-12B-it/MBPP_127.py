from typing import Any

def multiply_int(a: int, b: int) -> int:
    """
    Multiplies two integers without using the * operator.

    This implementation uses the concept of repeated addition.
    To ensure efficiency and handle negative numbers correctly, 
    it calculates the absolute values and determines the final sign.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of a and b.

    Raises:
        TypeError: If inputs are not integers.
    """

    # Step 1: Input Validation
    # Ensure that both inputs are strictly of the type 'int'
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(f"Inputs must be integers. Received: {type(a).__name__} and {type(b).__name__}")

    # Step 2: Handle the Zero Case
    # Any number multiplied by zero is zero.
    if a == 0 or b == 0:
        return 0

    # Step 3: Determine the sign of the result
    # A product is negative if exactly one of the factors is negative.
    is_negative = False
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        is_negative = True

    # Step 4: Work with absolute values
    # This simplifies the repeated addition logic.
    abs_a = abs(a)
    abs_b = abs(b)

    # Step 5: Optimization - Use the smaller number as the counter
    # To minimize the number of iterations in the addition loop, 
    # we ensure 'count' is the smaller of the two absolute values.
    if abs_a < abs_b:
        count = abs_a
        value_to_add = abs_b
    else:
        count = abs_b
        value_to_add = abs_a

    # Step 6: Repeated Addition
    # Accumulate the result by adding the value 'count' times.
    total_sum = 0
    for _ in range(count):
        total_sum += value_to_add

    # Step 7: Apply the sign
    # If the result was determined to be negative, negate the sum.
    if is_negative:
        result = -total_sum
    else:
        result = total_sum

    return result

if __name__ == "__main__":
    # Assertion tests as requested by the problem
    assert multiply_int(10, 20) == 200
    assert multiply_int(5, 10) == 50
    assert multiply_int(4, 8) == 32

    # Additional Edge Case Tests
    assert multiply_int(0, 100) == 0
    assert multiply_int(-5, 10) == -50
    assert multiply_int(-5, -5) == 25
    assert multiply_int(1, 1000) == 1000
    assert multiply_int(-1, 1) == -1