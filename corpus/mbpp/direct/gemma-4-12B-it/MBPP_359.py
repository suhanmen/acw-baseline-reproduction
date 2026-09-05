import math

def Check_Solution(a, b, c):
    """
    Checks whether one root of the quadratic equation ax^2 + bx + c = 0
    is twice of the other.
    """
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "No"

    # Calculate the two roots using the quadratic formula
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)

    # Check if one root is twice the other
    # Using math.isclose to handle potential floating point inaccuracies
    if math.isclose(root1, 2 * root2) or math.isclose(root2, 2 * root1):
        return "Yes"
    else:
        return "No"