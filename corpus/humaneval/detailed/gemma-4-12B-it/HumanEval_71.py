import math

def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """
    Checks if three side lengths can form a valid non-degenerate triangle.
    A triangle is valid if the sum of any two sides is strictly greater 
    than the third side.
    """
    # Side lengths must be positive numbers
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Triangle Inequality Theorem checks
    condition1 = (a + b > c)
    condition2 = (a + c > b)
    condition3 = (b + c > a)

    # All three conditions must be true
    is_valid = condition1 and condition2 and condition3
    return is_valid

def calculate_heron_area(a: float, b: float, c: float) -> float:
    """
    Calculates the area of a triangle using Heron's Formula.
    Area = sqrt(s * (s - a) * (s - b) * (s - c))
    where s is the semi-perimeter.
    """
    # Calculate semi-perimeter
    perimeter = a + b + c
    semi_perimeter = perimeter / 2.0

    # Calculate the radicand (the value inside the square root)
    # Because we validated the triangle, these terms are guaranteed non-negative
    term1 = semi_perimeter
    term2 = semi_perimeter - a
    term3 = semi_perimeter - b
    term4 = semi_perimeter - c

    radicand = term1 * term2 * term3 * term4

    # Use max(0, radicand) to handle floating point precision errors 
    # where radicand might be a tiny negative number like -1e-15
    area = math.sqrt(max(0.0, radicand))
    return area

def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    # Input Validation: Ensure all inputs are numeric
    # This handles cases where non-numeric types might be passed
    try:
        side_a = float(a)
        side_b = float(b)
        side_c = float(c)
    except (ValueError, TypeError):
        # If inputs cannot be converted to floats, it is not a valid triangle
        return -1

    # Check for valid triangle side lengths
    # (Handles non-positive numbers and the triangle inequality theorem)
    is_valid = is_valid_triangle(side_a, side_b, side_c)

    if not is_valid:
        return -1

    # Calculate the area using Heron's Formula
    area = calculate_heron_area(side_a, side_b, side_c)

    # Round to 2 decimal points as requested
    # Note: We return a float. If the result is 6.0, it represents 6.00.
    final_area = round(area, 2)

    return final_area