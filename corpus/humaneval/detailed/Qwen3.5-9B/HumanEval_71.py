import math
import sys

def _validate_single_value(value: float) -> bool:
    """
    Validate that a single side length is numerically valid.
    A valid side length must be a finite number strictly greater than zero.

    This handles:
    - Non-numeric types (which should be caught by type hints or callers, 
      but we check isinstancce for safety)
    - Infinity (inf, -inf)
    - NaN (Not a Number)
    - Zero and negative numbers

    Returns True if valid, False otherwise.
    """
    # Check if the input is a number (int or float)
    if not isinstance(value, (int, float)):
        return False

    # Check for NaN (Not a Number). Comparisons with NaN always return False,
    # so we must use math.isnan specifically.
    if math.isnan(value):
        return False

    # Check for Infinity (positive or negative). Triangle sides must be finite.
    if math.isinf(value):
        return False

    # Check for non-positive values. Side lengths must be strictly positive.
    if value <= 0:
        return False

    return True

def _validate_triangle_sides(a: float, b: float, c: float) -> bool:
    """
    Validate the three sides to ensure they can form a valid, non-degenerate triangle.

    Conditions checked:
    1. Each individual side must be a valid positive finite number.
    2. The triangle inequality theorem must hold for all three combinations:
       - a + b > c
       - a + c > b
       - b + c > a

    Returns True if valid, False otherwise.
    """
    # Step 1: Validate individual sides
    if not _validate_single_value(a):
        return False
    if not _validate_single_value(b):
        return False
    if not _validate_single_value(c):
        return False

    # Step 2: Check Triangle Inequality Theorem
    # The sum of any two sides must be strictly greater than the third side.
    # We use a small epsilon for floating point comparison safety, though strict > 
    # is generally sufficient if inputs are exact. For robustness against 
    # floating point noise, we ensure the sum is not just >= but effectively >.

    sum_ab = a + b
    sum_ac = a + c
    sum_bc = b + c

    # Check if sum of a and b is greater than c
    if sum_ab <= c:
        return False

    # Check if sum of a and c is greater than b
    if sum_ac <= b:
        return False

    # Check if sum of b and c is greater than a
    if sum_bc <= a:
        return False

    return True

def _calculate_heron_area(a: float, b: float, c: float) -> float:
    """
    Calculate the area of a triangle using Heron's Formula.

    Formula:
    s = (a + b + c) / 2  (semi-perimeter)
    area = sqrt(s * (s - a) * (s - b) * (s - c))

    Parameters:
        a (float): Length of side a
        b (float): Length of side b
        c (float): Length of side c

    Returns:
        float: The area of the triangle

    Note: This function assumes the caller has already validated that 
    the sides form a valid triangle.
    """
    # Calculate semi-perimeter
    perimeter = a + b + c
    semi_perimeter = perimeter / 2.0

    # Calculate the term inside the square root
    # Since we validated that a triangle is possible, these values should be positive.
    # However, in floating point arithmetic, we guard against tiny negatives.
    term_a = semi_perimeter - a
    term_b = semi_perimeter - b
    term_c = semi_perimeter - c

    # Compute product
    product_inside_sqrt = semi_perimeter * term_a * term_b * term_c

    # Handle potential tiny floating point errors resulting in a slightly negative zero
    if product_inside_sqrt < 0:
        # If it's a very small negative number due to precision, treat as zero
        if product_inside_sqrt > -1e-12:
            product_inside_sqrt = 0.0
        else:
            # If it's significantly negative, something went wrong (shouldn't happen with valid input)
            raise ValueError("Invalid triangle area calculation: negative square root term")

    area = math.sqrt(product_inside_sqrt)

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
    # Explicit type hint check (optional but good for strictness)
    # While the problem implies numeric input, we validate content in helpers.

    # Validate the three sides collectively
    if not _validate_triangle_sides(a, b, c):
        return -1

    # Calculate the area using Heron's formula
    raw_area = _calculate_heron_area(a, b, c)

    # Round to 2 decimal points as required
    # Using round() which rounds to nearest even for .5 cases, standard for financial/decimal output.
    # Format to ensure display consistency if needed, but return value is float.
    rounded_area = round(raw_area, 2)

    return rounded_area