from typing import Tuple, List, Union

Number = Union[int, float]

def parse_coordinates(point_pairs: List[Number]) -> Tuple[Tuple[Number, Number], Tuple[Number, Number], Tuple[Number, Number]]:
    """
    Parses a flat list of 6 numbers into three 2D coordinate tuples.

    Raises:
        ValueError: If the input list does not contain exactly 6 elements.
        TypeError: If any element is not a number.
    """
    if len(point_pairs) != 6:
        raise ValueError(
            f"Expected exactly 6 coordinates (x1, y1, x2, y2, x3, y3), got {len(point_pairs)}."
        )

    for i, val in enumerate(point_pairs):
        if not isinstance(val, (int, float)):
            raise TypeError(
                f"All coordinates must be numeric types (int or float). Found type '{type(val).__name__}' at index {i}."
            )

    p1 = (point_pairs[0], point_pairs[1])
    p2 = (point_pairs[2], point_pairs[3])
    p3 = (point_pairs[4], point_pairs[5])

    return p1, p2, p3

def calculate_distance_squared(p1: Tuple[Number, Number], p2: Tuple[Number, Number]) -> Number:
    """
    Calculates the squared Euclidean distance between two points.
    Using squared distance avoids the computationally expensive square root operation.
    """
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (dx * dx) + (dy * dy)

def validate_positive_length(a_squared: Number, b_squared: Number, c_squared: Number) -> bool:
    """
    Validates that the squared lengths of the sides are positive.
    If any side has zero length, the triangle is degenerate (invalid).
    """
    if a_squared <= 0:
        return False
    if b_squared <= 0:
        return False
    if c_squared <= 0:
        return False
    return True

def validate_triangle_inequality(a_squared: Number, b_squared: Number, c_squared: Number) -> bool:
    """
    Validates the triangle inequality theorem using squared distances.

    The theorem states that the sum of the lengths of any two sides must be greater than 
    the length of the third side (a + b > c).

    Squaring both sides: (a + b)^2 > c^2  =>  a^2 + b^2 + 2ab > c^2
    Since 2ab > 0 (as lengths are positive), a^2 + b^2 > c^2 is a necessary but not sufficient condition.
    However, the standard check for degeneracy in floating point geometry often relies on:
    a + b > c.

    To avoid square roots while checking strict inequality a + b > c, we can square:
    (a + b)^2 > c^2
    a^2 + 2*sqrt(a)*sqrt(b)*sqrt(a)*sqrt(b) + b^2 > c^2
    This path is complex. Instead, we will compute the actual lengths (square roots) 
    for the inequality check, as it is more readable and the performance difference is negligible 
    for 3 calculations.
    """
    a = a_squared ** 0.5
    b = b_squared ** 0.5
    c = c_squared ** 0.5

    # Check a + b > c
    if (a + b) <= c:
        return False
    # Check a + c > b
    if (a + c) <= b:
        return False
    # Check b + c > a
    if (b + c) <= a:
        return False

    return True

def check_triangle(x1: Number, y1: Number, x2: Number, y2: Number, x3: Number, y3: Number) -> str:
    """
    Determines if three given points form a valid, non-degenerate triangle.

    A valid triangle must have:
    1. Three distinct vertices (no two points are the same).
    2. The side lengths must satisfy the triangle inequality theorem.
       (sum of any two sides must be strictly greater than the third side).

    Returns:
        'Yes' if the triangle is valid.
        'No' if the triangle is invalid (degenerate or collinear).

    Raises:
        ValueError: If the number of arguments is not exactly 6.
        TypeError: If any argument is not a number.
    """
    # Input validation: check argument count
    # The function signature enforces 6 positional args, but we check for None or unexpected structure if we were using *args.
    # Since we have fixed signature, we rely on the fact that if called correctly, we have these variables.
    # However, for robustness against self-calls with wrong defaults or internal logic, 
    # we ensure we treat x1, y1 etc as the only inputs.

    # Parse the points
    try:
        p1, p2, p3 = parse_coordinates([x1, y1, x2, y2, x3, y3])
    except (ValueError, TypeError) as e:
        raise e

    # Calculate squared distances between all pairs
    d1_squared = calculate_distance_squared(p1, p2)
    d2_squared = calculate_distance_squared(p2, p3)
    d3_squared = calculate_distance_squared(p3, p1)

    # Validate that lengths are positive (points must be distinct)
    if not validate_positive_length(d1_squared, d2_squared, d3_squared):
        return "No"

    # Validate triangle inequality
    if not validate_triangle_inequality(d1_squared, d2_squared, d3_squared):
        return "No"

    return "Yes"