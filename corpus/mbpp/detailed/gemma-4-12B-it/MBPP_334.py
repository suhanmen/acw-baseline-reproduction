import math

def check_Validity(side_a: float, side_b: float, side_c: float) -> bool:
    """
    Determines whether three given side lengths can form a valid triangle.

    A triangle is valid if and only if the sum of the lengths of any two 
    sides is strictly greater than the length of the third side.

    Args:
        side_a (float): Length of the first side.
        side_b (float): Length of the second side.
        side_c (float): Length of the third side.

    Returns:
        bool: True if the sides form a valid triangle, False otherwise.

    Raises:
        TypeError: If any of the inputs are not numeric types.
        ValueError: If any of the side lengths are non-positive numbers.
    """

    # Step 1: Validate input types.
    # We ensure that all inputs are either integers or floats.
    inputs = [side_a, side_b, side_c]
    for value in inputs:
        if not isinstance(value, (int, float)):
            raise TypeError(f"All sides must be numeric. Received: {type(value)}")

    # Step 2: Validate input values (Physical constraints).
    # A side of a triangle must have a positive length.
    # Zero length or negative length makes a triangle impossible.
    for value in inputs:
        if value <= 0:
            # Raising a ValueError for non-positive side lengths to ensure 
            # the function handles degenerate/impossible geometry explicitly.
            raise ValueError(f"Side lengths must be greater than zero. Received: {value}")

    # Step 3: Apply the Triangle Inequality Theorem.
    # Theorem: a + b > c, a + c > b, and b + c > a.

    # Calculate sums of pairs
    sum_ab = side_a + side_b
    sum_ac = side_a + side_c
    sum_bc = side_b + side_c

    # Check inequality conditions
    # If any sum is equal to the third side, it is a "degenerate triangle" 
    # (a line segment), which is generally considered invalid in standard geometry.
    condition_1 = sum_ab > side_c
    condition_2 = sum_ac > side_b
    condition_3 = sum_bc > side_a

    # The triangle is valid if and only if all three conditions are met.
    is_valid = condition_1 and condition_2 and condition_3

    return is_valid

# The following logic is kept in the code block for structural completeness 
# as per instructions, though the primary task is the function definition.
if __name__ == "__main__":
    # Test cases provided in the prompt
    assert check_Validity(1, 2, 3) == False
    assert check_Validity(2, 3, 5) == False
    assert check_Validity(7, 10, 5) == True