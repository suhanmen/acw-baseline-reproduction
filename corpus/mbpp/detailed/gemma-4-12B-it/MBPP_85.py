import math

def surfacearea_sphere(radius: float) -> float:
    """
    Calculates the surface area of a sphere given its radius.

    The formula for the surface area of a sphere is:
    A = 4 * pi * r^2

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The calculated surface area.

    Raises:
        ValueError: If the radius is negative.
        TypeError: If the radius is not a real number.
    """

    # --- Input Validation ---

    # Check if the input is of a numeric type (int or float)
    # Note: bool is a subclass of int in Python, so we check specifically for types
    if not isinstance(radius, (int, float)) or isinstance(radius, bool):
        raise TypeError(
            f"Input radius must be a numeric value (int or float). "
            f"Received type: {type(radius).__name__}"
        )

    # The radius of a physical sphere cannot be negative.
    # A radius of zero results in a surface area of zero (a degenerate sphere/point).
    if radius < 0:
        raise ValueError(
            f"Radius cannot be negative. Received value: {radius}"
        )

    # --- Calculation ---

    # Handle the degenerate case where radius is zero explicitly for clarity,
    # although the formula handles it naturally.
    if radius == 0:
        return 0.0

    # Define the constant pi using the math library for maximum precision.
    pi_constant = math.pi

    # Step 1: Calculate the square of the radius (r^2).
    radius_squared = radius ** 2

    # Step 2: Multiply by 4.
    multiplied_by_four = 4 * radius_squared

    # Step 3: Multiply by pi to get the final surface area.
    surface_area = multiplied_by_four * pi_constant

    return float(surface_area)

# The following assertions verify the correctness of the implementation.
if __name__ == "__main__":
    # Test cases provided in the requirements
    assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=1e-15)
    assert math.isclose(surfacearea_sphere(15), 2827.4333882308138, rel_tol=1e-15)
    assert math.isclose(surfacearea_sphere(20), 5026.548245743669, rel_tol=1e-15)