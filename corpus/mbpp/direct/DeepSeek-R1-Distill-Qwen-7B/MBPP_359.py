def Check_Solution(a, b, c):
    from math import sqrt
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No"  # No real roots if discriminant is negative
    # Calculate roots
    root1 = (-b + sqrt(discriminant)) / (2*a)
    root2 = (-b - sqrt(discriminant)) / (2*a)
    # Check if one root is twice the other
    if (root1 == 2 * root2) or (root2 == 2 * root1):
        return "Yes"
    else:
        return "No"