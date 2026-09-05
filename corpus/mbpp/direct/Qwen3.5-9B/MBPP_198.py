import math

def largest_triangle(a, b):
    # The largest triangle inscribed in an ellipse with semi-axes a and b
    # has area = (3 * sqrt(3) / 2) * a * b
    return (3 * math.sqrt(3) / 2) * a * b