import math

def find_Volume(base_a: float, base_b: float, base_c: float, height_prism: float) -> float:
    """
    Calculates the volume of a triangular prism.

    The volume is calculated by first finding the area of the triangular base
    using Heron's Formula, and then multiplying that area by the height 
    of the prism.

    Formula:
    1. Semi-perimeter (s) = (a + b + c) / 2
    2. Base Area = sqrt(s * (s - a) * (s - b) * (s - c))
    3. Volume = Base Area * height_prism

    Args:
        base_a (float): Length of side a of the triangular base.
        base_b (float): Length of side b of the triangular base.
        base_c (float): Length of side c of the triangular base.
        height_prism (float): The height (length) of the prism.

    Returns:
        float: The volume of the triangular prism.

    Raises:
        ValueError: If side lengths do not form a valid triangle or if 
                    dimensions are non-positive.
    """

    # Validate that all inputs are positive numbers.
    # A dimension of zero or less is physically impossible for a prism.
    dimensions = [base_a, base_b, base_c, height_prism]
    for dim in dimensions:
        if not isinstance(dim, (int, float)):
            raise ValueError(f"Input {dim} is not a numeric type.")
        if dim <= 0:
            raise ValueError(f"Dimension {dim} must be greater than zero.")

    # Check the Triangle Inequality Theorem:
    # The sum of the lengths of any two sides must be greater than the third side.
    # This ensures the base is a valid triangle.
    is_valid_triangle = (
        (base_a + base_b > base_c) and
        (base_a + base_c > base_b) and
        (base_b + base_c > base_a)
    )

    if not is_valid_triangle:
        raise ValueError(
            f"The sides {base_a}, {base_b}, and {base_c} do not form a valid triangle."
        )

    # Calculate the semi-perimeter of the triangular base.
    semi_perimeter = (base_a + base_b + base_c) / 2.0

    # Calculate the area of the triangular base using Heron's Formula.
    # We use max(0, ...) to avoid precision errors resulting in tiny negative numbers.
    term_a = semi_perimeter
    term_b = semi_perimeter - base_a
    term_c = semi_perimeter - base_b
    term_d = semi_perimeter - base_c

    area_product = term_a * term_b * term_c * term_d

    # In cases where the triangle is degenerate (flat), area_product might be 0.
    # Heron's formula is robust for valid triangles.
    base_area = math.sqrt(max(0.0, area_product))

    # Calculate the volume of the prism.
    # Volume = Area of Base * Height
    volume = base_area * height_prism

    # Return the result rounded to a reasonable precision to handle floating point noise.
    # The assertions provided use integers, so we return a float.
    return float(volume)

# Redefining the function signature specifically to match the requested assertions.
# The problem description asks for find_Volume(10, 8, 6) == 240.
# This implies the signature is find_Volume(a, b, c, height) where height is 
# provided or the prism height is implicit.
# Looking at the provided examples:
# 1. (10, 8, 6) -> Area of 10,8,6 is (1/2)*8*6 = 24 (Right triangle: 6^2+8^2=10^2).
#    If Volume = 240, Height must be 10.
# 2. (3, 2, 2) -> s = 3.5. Area = sqrt(3.5 * 0.5 * 1.5 * 1.5) = sqrt(3.9375) approx 1.98.
#    Wait, let's check the math for (3,2,2). s = (3+2+2)/2 = 3.5.
#    Area = sqrt(3.5 * (3.5-3) * (3.5-2) * (3.5-2)) = sqrt(3.5 * 0.5 * 1.5 * 1.5) = 1.984.
#    1.984 * Height = 6? Height would be ~3.02.
#
# Re-evaluating the logic: Perhaps the inputs are (base_side_1, base_side_2, height_prism)
# and it's a right-angled triangle? 
# 1. (10, 8, 6) -> (10 * 8 / 2) * 6 = 40 * 6 = 240. Correct!
# 2. (3, 2, 2) -> (3 * 2 / 2) * 2 = 3 * 2 = 6. Correct!
# 3. (1, 2, 1) -> (1 * 2 / 2) * 1 = 1 * 1 = 1. Correct!
#
# Conclusion: The signature find_Volume(a, b, c) takes:
# a: base_side_1 of a right-angled triangle
# b: base_side_2 of a right-angled triangle
# c: height of the prism
# The triangle base area is (a * b) / 2.

def find_Volume(base_side_1: float, base_side_2: float, height_prism: float) -> float:
    """
    Finds the volume of a triangular prism where the base is a right-angled triangle.

    Args:
        base_side_1 (float): One side of the right-angled triangular base.
        base_side_2 (float): The other side of the right-angled triangular base.
        height_prism (float): The height of the prism.

    Returns:
        float: The volume of the triangular prism.
    """
    # Input Validation
    if not all(isinstance(x, (int, float)) for x in [base_side_1, base_side_2, height_prism]):
        raise ValueError("All inputs must be numeric.")

    if base_side_1 <= 0 or base_side_2 <= 0 or height_prism <= 0:
        raise ValueError("All dimensions must be positive non-zero numbers.")

    # Step 1: Calculate the area of the triangular base.
    # Area of a right-angled triangle = (base * height_of_triangle) / 2
    # Here, base_side_1 and base_side_2 are the legs of the triangle.
    base_area = (base_side_1 * base_side_2) / 2.0

    # Step 2: Calculate the total volume.
    # Volume = Area of base * height of prism.
    volume = base_area * height_prism

    return float(volume)