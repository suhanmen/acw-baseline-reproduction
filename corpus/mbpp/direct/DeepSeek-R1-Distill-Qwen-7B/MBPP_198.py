import math

def largest_triangle(a, b):
    # Calculate the area of the ellipse using the formula: π * a * b
    # The maximum inscribed triangle's area is (4/√3) times the area of the ellipse
    max_area = (4.0 / math.sqrt(3.0)) * math.pi * a * b
    return max_area

# Example usage:
# assert largest_triangle(4,2)==10.392304845413264
# assert largest_triangle(5,7)==4.639421805988064
# assert largest_triangle(9,1)==105.2220865598093