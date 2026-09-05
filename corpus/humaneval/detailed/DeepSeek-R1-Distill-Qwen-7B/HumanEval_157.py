def right_angle_triangle(a, b, c):
    # Validate inputs
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Check if sides can form a triangle
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False

    # Sort the sides
    sides = sorted([a, b, c])
    a, b, c = sides

    # Apply Pythagoras theorem
    return a * a + b * b == c * c