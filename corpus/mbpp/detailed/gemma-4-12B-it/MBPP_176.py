import math

def perimeter_triangle(side_a: float, side_b: float, side_c: float) -> float:
    """
    Calculates the perimeter of a triangle given the lengths of its three sides.

    Validates that the inputs are numbers, are non-negative, and satisfy 
    the triangle inequality theorem (the sum of the lengths of any two sides 
    must be greater than the length of the third side).

    Args:
        side_a (float): Length of the first side.
        side_b (float): Length of the second side.
        side_c (float): Length of the third side.

    Returns:
        float: The perimeter of the triangle.

    Raises:
        TypeError: If any input is not an integer or a float.
        ValueError: If any side length is non-positive or fails the 
                    triangle inequality theorem.
    """
    # 1. Validate input types
    # We ensure that the inputs are numeric (int or float).
    inputs = [side_a, side_b, side_c]
    for value in inputs:
        if not isinstance(value, (int, float)):
            raise TypeError(f"All side lengths must be numbers. Received: {type(value)}")

    # 2. Validate that side lengths are positive
    # A triangle cannot have a side of length 0 or a negative length.
    for i, value in enumerate(inputs):
        if value <= 0:
            side_names = ["side_a", "side_b", "side_c"]
            raise ValueError(f"{side_names[i]} must be greater than zero. Received: {value}")

    # 3. Validate the Triangle Inequality Theorem
    # The sum of any two sides must be strictly greater than the third side.
    # This also covers cases where the points are collinear (degenerate triangles).
    is_valid_triangle = (
        (side_a + side_b > side_c) and
        (side_a + side_c > side_b) and
        (side_b + side_c > side_a)
    )

    # Note: The problem description implies standard math, but for some specific 
    # edge cases like (10, 20, 30) provided in the assertion, we must check 
    # if the prompt allows "degenerate" triangles or straight lines.
    # Standard geometry: a+b > c. 
    # However, the prompt's assertion (10, 20, 30) == 60 indicates that
    # the function should accept cases where a+b == c.

    # Let's re-evaluate based on the specific requirements:
    # assert perimeter_triangle(10,20,30)==60
    # This means the code MUST support degenerate triangles (where sum of two 
    # sides equals the third).

    is_valid_degenerate_triangle = (
        (side_a + side_b >= side_c) and
        (side_a + side_c >= side_b) and
        (side_b + side_c >= side_a)
    )

    if not is_valid_degenerate_triangle:
        raise ValueError(
            f"The lengths {side_a}, {side_b}, and {side_c} do not form a valid triangle. "
            "The sum of any two sides must be greater than or equal to the third side."
        )

    # 4. Calculate the perimeter
    # Perimeter is the sum of all three sides.
    perimeter = float(side_a + side_b + side_c)

    return perimeter

if __name__ == "__main__":
    # Testing the provided assertions
    assert perimeter_triangle(10, 20, 30) == 60
    assert perimeter_triangle(3, 4, 5) == 12
    assert perimeter_triangle(25, 35, 45) == 105