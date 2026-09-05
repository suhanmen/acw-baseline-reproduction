import math

def triangle_area(a, b, c):
    # Check if the triangle is valid
    if (a + b > c) and (a + c > b) and (b + c > a):
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        # Calculate the area using Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        # Round to 2 decimal points
        return round(area, 2)
    else:
        return -1