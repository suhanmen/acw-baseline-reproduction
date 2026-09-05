def triangle_area(a, b, c):
    # Validate the inputs to ensure they are positive numbers
    if (a <= 0) or (b <= 0) or (c <= 0):
        return -1

    # Check the triangle inequality theorem for all three combinations
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return -1

    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area_squared = s * (s - a) * (s - b) * (s - c)
    if area_squared <= 0:
        return -1  # This handles cases where the sides are colinear or invalid

    area = area_squared ** 0.5

    # Round to two decimal places
    return round(area, 2)