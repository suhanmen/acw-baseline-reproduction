import math

def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''

    def validate_input_type(value):
        """Ensures the input is a numeric type."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"Input {value} is not a numeric type.")

    def is_valid_triangle_side(side):
        """Checks if a side length is positive and non-zero."""
        if side <= 0:
            return False
        return True

    # Step 1: Validate input types
    validate_input_type(a)
    validate_input_type(b)
    validate_input_type(c)

    # Step 2: Validate that sides form a physical triangle
    # All sides must be greater than zero.
    if not is_valid_triangle_side(a) or \
       not is_valid_triangle_side(b) or \
       not is_valid_triangle_side(c):
        return False

    # Step 3: Triangle Inequality Theorem
    # The sum of any two sides must be strictly greater than the third side.
    # This handles degenerate triangles (where sum equals third side) or impossible ones.
    sides = sorted([a, b, c])
    side_1 = sides[0]
    side_2 = sides[1]
    hypotenuse_candidate = sides[2]

    if (side_1 + side_2) <= hypotenuse_candidate:
        return False

    # Step 4: Pythagorean Theorem Check
    # For a right-angled triangle, a^2 + b^2 = c^2 where c is the longest side.
    # Because of floating point precision, we use math.isclose for comparisons.

    sq_side_1 = side_1 ** 2
    sq_side_2 = side_2 ** 2
    sq_hypotenuse = hypotenuse_candidate ** 2

    sum_of_squares = sq_side_1 + sq_side_2

    # Check if the sum of the squares of the two shorter sides equals 
    # the square of the longest side.
    is_right_angled = math.isclose(sum_of_squares, sq_hypotenuse, rel_tol=1e-9)

    return is_right_angled