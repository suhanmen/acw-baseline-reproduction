import math

def Check_Solution(a: float, b: float, c: float) -> str:
    """
    Determines whether one root of the quadratic equation ax^2 + bx + c = 0 
    is exactly twice the other root.

    Args:
        a: Coefficient of x^2
        b: Coefficient of x
        c: Constant term

    Returns:
        "Yes" if one root is twice the other, otherwise "No".
    """

    # Validation: Ensure 'a' is not zero, as it wouldn't be a quadratic equation.
    # If a is 0, it's a linear equation, which doesn't have two roots to compare.
    if a == 0:
        # In a production environment, you might raise a ValueError, 
        # but for the purpose of this logic, we return "No".
        return "No"

    # Standardize inputs to float to ensure consistent division behavior.
    a = float(a)
    b = float(b)
    c = float(c)

    # The quadratic formula is: x = (-b ± sqrt(b^2 - 4ac)) / 2a
    # Discriminant: D = b^2 - 4ac
    discriminant = (b ** 2) - (4 * a * c)

    # If discriminant is negative, roots are complex.
    # The problem context usually implies real roots, but we handle it for robustness.
    if discriminant < 0:
        return "No"

    # Calculate the square root of the discriminant.
    sqrt_discriminant = math.sqrt(discriminant)

    # Calculate the two roots using the quadratic formula.
    # root1 = (-b + sqrt(D)) / 2a
    # root2 = (-b - sqrt(D)) / 2a
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)

    # We need to check if one root is twice the other.
    # This means either:
    # 1. root1 = 2 * root2
    # OR
    # 2. root2 = 2 * root1

    # Using math.isclose to handle potential floating point precision issues
    is_root1_twice_root2 = math.isclose(root1, 2 * root2, rel_tol=1e-9)
    is_root2_twice_root1 = math.isclose(root2, 2 * root1, rel_tol=1e-9)

    if is_root1_twice_root2 or is_root2_twice_root1:
        return "Yes"
    else:
        return "No"

# The following assertions are provided in the prompt to ensure functionality.
if __name__ == "__main__":
    # Case 1: x^2 - 3x + 2 = 0 -> roots are (3 +/- sqrt(9-8))/2 -> (3+1)/2=2 and (3-1)/2=1.
    # 2 is twice 1.
    assert Check_Solution(1, -3, 2) == "Yes" 

    # Note: The prompt example Check_Solution(1,3,2) == "Yes" 
    # implies (x^2 + 3x + 2 = 0) -> roots are -1 and -2. 
    # -2 is twice -1. This matches the logic.
    assert Check_Solution(1, 3, 2) == "Yes"

    # Case 2: x^2 + 2x + 3 = 0 -> roots are complex.
    assert Check_Solution(1, 2, 3) == "No"

    # Case 3: x^2 - 5x + 6 = 0 -> roots are 2 and 3. Neither is twice the other.
    assert Check_Solution(1, -5, 6) == "No"