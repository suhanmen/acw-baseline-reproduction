import math

def volume_sphere(radius: float) -> float:
    """
    Calculates the volume of a sphere given its radius.

    Formula: V = (4/3) * pi * r^3

    Args:
        radius (float): The radius of the sphere. Must be a non-negative number.

    Returns:
        float: The volume of the sphere.

    Raises:
        TypeError: If the input is not an integer or a float.
        ValueError: If the input radius is negative.
    """

    # --- Input Validation ---

    # Check if the input type is valid
    if not isinstance(radius, (int, float)):
        raise TypeError(
            f"Input radius must be a number, but received {type(radius).__name__}."
        )

    # Check for negative radius (a sphere cannot have a negative radius)
    if radius < 0:
        raise ValueError(
            f"Radius cannot be negative. Received: {radius}"
        )

    # Handle edge case: Radius is zero
    # A sphere with radius 0 has 0 volume.
    if radius == 0:
        return 0.0

    # --- Calculation Logic ---

    # Step 1: Calculate the cube of the radius (r^3)
    # We use the power operator for clarity.
    radius_cubed = math.pow(radius, 3)

    # Step 2: Define the constant pi
    # Using math.pi for maximum precision.
    pi_constant = math.pi

    # Step 3: Calculate the multiplier (4/3)
    # We use floating point division to ensure precision.
    fraction_multiplier = 4.0 / 3.0

    # Step 4: Combine components to find the volume
    # Volume = (4/3) * pi * r^3
    volume = fraction_multiplier * pi_constant * radius_cubed

    return volume

# The following assertions verify the correctness of the implementation.
if __name__ == "__main__":
    # Test Case 1: Radius 10
    # (4/3) * pi * 10^3 = (4/3) * pi * 1000 = 1333.333... * pi
    assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=1e-9)

    # Test Case 2: Radius 25
    # (4/3) * pi * 25^3 = (4/3) * pi * 15625 = 20833.333... * pi
    assert math.isclose(volume_sphere(25), 65449.84694978735, rel_tol=1e-9)

    # Test Case 3: Radius 20
    # (4/3) * pi * 20^3 = (4/3) * pi * 8000 = 10666.666... * pi
    assert math.isclose(volume_sphere(20), 33510.32163829113, rel_tol=1e-9)

    # Test Case 4: Radius 0
    assert volume_sphere(0) == 0.0