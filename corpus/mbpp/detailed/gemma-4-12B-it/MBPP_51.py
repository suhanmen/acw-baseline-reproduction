from typing import Union

def check_equilateral(side_a: Union[int, float], side_b: Union[int, float], side_c: Union[int, float]) -> bool:
    """
    Determines if three sides form an equilateral triangle.

    An equilateral triangle must satisfy two conditions:
    1. All three sides must be of equal length.
    2. The sides must form a valid triangle (the sum of any two sides 
       must be strictly greater than the third side).
       Note: In the specific case of equilateral triangles, if all sides 
       are equal and greater than zero, the triangle inequality is 
       automatically satisfied (e.g., x + x > x).

    Args:
        side_a: Length of the first side.
        side_b: Length of the second side.
        side_c: Length of the third side.

    Returns:
        bool: True if the sides form an equilateral triangle, False otherwise.

    Raises:
        ValueError: If any side length is non-positive.
        TypeError: If inputs are not numeric.
    """

    # Step 1: Validate that all inputs are numbers (int or float)
    inputs = [side_a, side_b, side_c]
    for value in inputs:
        if not isinstance(value, (int, float)):
            raise TypeError(f"All sides must be numeric. Received: {type(value)}")

    # Step 2: Validate that all side lengths are positive
    # A triangle cannot have a side of length 0 or a negative length.
    for value in inputs:
        if value <= 0:
            raise ValueError(f"Side lengths must be positive. Received: {value}")

    # Step 3: Check for equality of all sides
    # In an equilateral triangle, side_a == side_b and side_b == side_c.
    is_all_equal = (side_a == side_b) and (side_b == side_c)

    # Step 4: Check triangle inequality
    # Even if sides are equal, they must be able to form a triangle.
    # For equilateral triangles, this simplifies to: side_a + side_b > side_c
    # However, we keep it explicit for robustness.
    is_valid_triangle = (
        (side_a + side_b > side_c) and
        (side_a + side_c > side_b) and
        (side_b + side_c > side_a)
    )

    # Final Result
    # The triangle is equilateral if and only if all sides are equal 
    # AND it forms a valid triangle.
    if is_all_equal and is_valid_triangle:
        return True
    else:
        return False

# Assertions provided in the problem description
if __name__ == "__main__":
    assert check_equilateral(6, 8, 12) == False
    assert check_equilateral(6, 6, 12) == False
    assert check_equilateral(6, 6, 6) == True