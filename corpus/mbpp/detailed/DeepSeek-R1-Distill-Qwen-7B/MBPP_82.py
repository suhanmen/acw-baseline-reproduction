import math

def volume_sphere(radius):
    """
    Calculate the volume of a sphere given its radius.

    Parameters
    ----------
    radius : float
        The radius of the sphere.

    Returns
    -------
    float
        The volume of the sphere.

    Raises
    ------
    ValueError
        If the radius is not a positive number.
    """
    # Validate the input
    if not isinstance(radius, float):
        raise ValueError("Radius must be a float.")

    if radius <= 0:
        raise ValueError("Radius must be a positive number.")

    # Calculate the volume using the formula
    volume = (4/3) * math.pi * (radius ** 3)

    # Return the result rounded to 9 decimal places
    return round(volume, 9)