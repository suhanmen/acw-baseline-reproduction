import math
from typing import Any, Union

Number = Union[int, float]

def _is_valid_positive_number(value: Any) -> bool:
    '''
    Check if the provided value is a valid positive number (int or float)
    strictly greater than zero.

    A side length of a triangle must be:
    1. A number (int or float).
    2. Greater than zero (positive).

    Returns:
        bool: True if valid, False otherwise.
    '''
    if not isinstance(value, (int, float)):
        return False
    return value > 0

def _validate_triangle_sides(a: Number, b: Number, c: Number) -> None:
    '''
    Validate that all three sides are valid positive numbers.

    Raises:
        TypeError: If any side is not an int or float.
        ValueError: If any side is less than or equal to zero.
    '''
    if not _is_valid_positive_number(a):
        if not isinstance(a, (int, float)):
            raise TypeError(f"Side 'a' must be a number, got {type(a).__name__}")
        else:
            raise ValueError(f"Side 'a' must be greater than zero, got {a}")

    if not _is_valid_positive_number(b):
        if not isinstance(b, (int, float)):
            raise TypeError(f"Side 'b' must be a number, got {type(b).__name__}")
        else:
            raise ValueError(f"Side 'b' must be greater than zero, got {b}")

    if not _is_valid_positive_number(c):
        if not isinstance(c, (int, float)):
            raise TypeError(f"Side 'c' must be a number, got {type(c).__name__}")
        else:
            raise ValueError(f"Side 'c' must be greater than zero, got {c}")

def _are_sides_ordered(sides: tuple) -> tuple:
    '''
    Sort the three sides in ascending order to facilitate hypotenuse calculation.

    Returns:
        tuple: A new tuple of sides sorted from smallest to largest.
    '''
    return sorted(sides)

def _is_degenerate_triangle(sides: tuple) -> bool:
    '''
    Check if the sides form a degenerate triangle.

    A non-degenerate triangle must satisfy the strict triangle inequality:
    The sum of any two sides must be strictly greater than the third side.
    When sorted as (x, y, z) where x <= y <= z, we only need to check:
    x + y > z

    Returns:
        bool: True if the triangle is degenerate (invalid), False otherwise.
    '''
    smallest, middle, largest = sides
    # Use a small epsilon for floating point comparison safety if needed,
    # but strict inequality is the definition.
    return (smallest + middle) <= largest

def _is_right_angle_triangle(sides: tuple) -> bool:
    '''
    Check if the sorted sides form a right-angled triangle.

    For a right-angled triangle with sorted sides (leg1, leg2, hypotenuse):
    leg1^2 + leg2^2 == hypotenuse^2

    Returns:
        bool: True if it satisfies the Pythagorean theorem, False otherwise.
    '''
    leg1, leg2, hypotenuse = sides

    # Calculate squares explicitly
    square_leg1 = leg1 * leg1
    square_leg2 = leg2 * leg2
    square_hypotenuse = hypotenuse * hypotenuse

    # Sum of squares of legs
    sum_leg_squares = square_leg1 + square_leg2

    # Check equality. Using a tolerance for floating point comparisons is safer,
    # though exact equality works perfectly for small integers.
    tolerance = 1e-9
    return abs(sum_leg_squares - square_hypotenuse) < tolerance

def right_angle_triangle(a: Number, b: Number, c: Number) -> bool:
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.

    Args:
        a (int or float): Length of the first side.
        b (int or float): Length of the second side.
        c (int or float): Length of the third side.

    Returns:
        bool: True if the sides form a right-angled triangle, False otherwise.

    Raises:
        TypeError: If any argument is not an int or float.
        ValueError: If any argument is not greater than zero.

    Examples:
        right_angle_triangle(3, 4, 5) == True
        right_angle_triangle(1, 2, 3) == False
        right_angle_triangle(0, 4, 5) raises ValueError
    '''

    # Step 1: Validate inputs
    _validate_triangle_sides(a, b, c)

    # Step 2: Store sides in a list for processing
    sides_list = [a, b, c]

    # Step 3: Sort sides to identify the potential hypotenuse
    # Sorting helps ensure we compare the two smaller sides against the largest.
    ordered_sides = _are_sides_ordered(tuple(sides_list))

    # Step 4: Check for degenerate triangle condition
    # A valid triangle must satisfy the triangle inequality theorem.
    if _is_degenerate_triangle(ordered_sides):
        return False

    # Step 5: Check the Pythagorean theorem
    # a^2 + b^2 = c^2 (where c is the largest side)
    is_right = _is_right_angle_triangle(ordered_sides)

    return is_right