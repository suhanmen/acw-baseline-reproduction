def Check_Solution(a, b, c):
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return "No"

    # Handle the case where A = 0 (linear equation)
    if a == 0:
        if b == 0:
            return "Yes" if c == 0 else "No"
        else:
            return "No"  # Only one root in linear equation

    # General quadratic case
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No"

    # Check if discriminant is zero or positive
    if discriminant == 0:
        return "Yes" if a != 0 else "No"  # Both roots are same, which can only be zero

    # Check if discriminant is positive and condition holds
    if 2 * b**2 == 9 * a * c:
        return "Yes"
    else:
        return "No"