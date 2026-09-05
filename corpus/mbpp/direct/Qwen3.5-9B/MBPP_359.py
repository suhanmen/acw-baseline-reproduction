def Check_Solution(a, b, c):
    if a == 0:
        return "No"
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No"

    sqrt_disc = discriminant ** 0.5
    root1 = (-b - sqrt_disc) / (2 * a)
    root2 = (-b + sqrt_disc) / (2 * a)

    if root1 == 0 or root2 == 0:
        return "No"

    if root1 == 2 * root2:
        return "Yes"
    if root2 == 2 * root1:
        return "Yes"

    return "No"