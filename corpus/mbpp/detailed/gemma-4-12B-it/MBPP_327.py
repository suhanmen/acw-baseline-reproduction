from typing import Union

def is_valid_triangle(side1: float, side2: float, side3: float) -> bool:
    """
    Validates if three side lengths can form a valid triangle.
    A triangle is valid if the sum of any two sides is strictly greater 
    than the third side, and all sides have positive lengths.
    """
    # Validate that all sides are positive numbers
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False

    # Check the Triangle Inequality Theorem:
    # Sum of any two sides must be greater than the third side.
    condition1 = (side1 + side2 > side3)
    condition2 = (side1 + side3 > side2)
    condition3 = (side2 + side3 > side1)

    return condition1 and condition2 and condition3

def check_isosceles(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> bool:
    """
    Determines if a triangle with sides a, b, and c is isosceles.
    An isosceles triangle has at least two sides of equal length.
    The function first validates if the inputs form a valid triangle.

    Args:
        a (int/float): Length of the first side.
        b (int/float): Length of the second side.
        c (int/float): Length of the third side.

    Returns:
        bool: True if the triangle is isosceles, False otherwise.
    """
    # Step 1: Validate inputs for correct types
    # While Python is dynamically typed, we ensure we are dealing with numbers
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All side lengths must be integers or floats.")

    # Step 2: Validate if the lengths can actually form a triangle
    # If the dimensions don't form a triangle, it cannot be an isosceles triangle.
    is_valid = is_valid_triangle(a, b, c)
    if not is_valid:
        # Depending on requirements, we could raise an error or return False.
        # Given the assertions, if it's not a valid triangle, it's not an 
        # isosceles triangle in the context of geometry.
        return False

    # Step 3: Check for isosceles property
    # An isosceles triangle has at least two equal sides.
    side_a_equals_b = (a == b)
    side_a_equals_c = (a == c)
    side_b_equals_c = (b == c)

    # If any pair of sides is equal, it is isosceles.
    # Note: Equilateral triangles (all three sides equal) are also 
    # technically isosceles.
    is_isosceles = side_a_equals_b or side_a_equals_c or side_b_equals_c

    return is_isosceles

if __name__ == "__main__":
    # Test cases provided in the prompt
    assert check_isosceles(6, 8, 12) == False
    assert check_isosceles(6, 6, 12) == True
    assert check_isosceles(6, 16, 20) == False