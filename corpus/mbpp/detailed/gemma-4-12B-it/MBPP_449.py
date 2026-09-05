import math
from typing import Union

def check_Triangle(x1: Union[int, float], y1: Union[int, float], 
                    x2: Union[int, float], y2: Union[int, float], 
                    x3: Union[int, float], y3: Union[int, float]) -> str:
    """
    Determines if three given points (x1, y1), (x2, y2), and (x3, y3) 
    form a valid triangle.

    A triangle is valid if:
    1. The three points are not collinear (they do not lie on the same line).
    2. The three points are distinct (no two points are the same).
    3. The sum of any two sides is strictly greater than the third side.

    Args:
        x1, y1: Coordinates of the first point.
        x2, y2: Coordinates of the second point.
        x3, y3: Coordinates of the third point.

    Returns:
        'Yes' if the points form a valid triangle, 'No' otherwise.
    """

    # --- Input Validation ---
    # Ensure all inputs are numeric (integers or floats)
    inputs = [x1, y1, x2, y2, x3, y3]
    for val in inputs:
        if not isinstance(val, (int, float)):
            raise ValueError(f"All coordinates must be numeric. Received: {type(val)}")

    # --- Calculate Side Lengths ---
    # Side A is the distance between Point 1 and Point 2
    dist_sq_1_2 = (x2 - x1)**2 + (y2 - y1)**2
    side_a = math.sqrt(dist_sq_1_2)

    # Side B is the distance between Point 2 and Point 3
    dist_sq_2_3 = (x3 - x2)**2 + (y3 - y2)**2
    side_b = math.sqrt(dist_sq_2_3)

    # Side C is the distance between Point 3 and Point 1
    dist_sq_3_1 = (x1 - x3)**2 + (y1 - y3)**2
    side_c = math.sqrt(dist_sq_3_1)

    # --- Check for Degenerate Cases ---

    # Case 1: Check if any points are identical (side length is zero)
    # A triangle cannot have a side of length 0.
    if side_a == 0 or side_b == 0 or side_c == 0:
        return 'No'

    # Case 2: Check for Collinearity using the Area method
    # The area of a triangle formed by (x1,y1), (x2,y2), (x3,y3) is:
    # Area = 0.5 * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|
    # If the area is 0, the points are collinear.

    term1 = x1 * (y2 - y3)
    term2 = x2 * (y3 - y1)
    term3 = x3 * (y1 - y2)

    double_area = abs(term1 + term2 + term3)

    # Using a small epsilon for floating point comparison
    if double_area < 1e-9:
        return 'No'

    # Case 3: Triangle Inequality Theorem
    # Sum of any two sides must be strictly greater than the third side.
    # This is mathematically equivalent to the non-zero area check for 3 points,
    # but we perform it explicitly to satisfy production-grade logic requirements.

    is_valid_inequality = (
        (side_a + side_b > side_c) and
        (side_a + side_c > side_b) and
        (side_b + side_c > side_a)
    )

    if is_valid_inequality:
        return 'Yes'
    else:
        return 'No'