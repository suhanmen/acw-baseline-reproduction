def perimeter_triangle(a, b, c):
    # Helper function to check if given sides form a valid triangle
    def is_valid_triangle(a, b, c):
        # Check for non-positive sides
        if a <= 0 or b <= 0 or c <= 0:
            return False
        # Check triangle inequality theorem
        return (a + b > c) and (a + c > b) and (b + c > a)

    # Helper function to calculate the sum of sides
    def sum_sides(a, b, c):
        return a + b + c

    # Check if all sides are valid
    if not is_valid_triangle(a, b, c):
        return None

    # Calculate and return the perimeter
    return sum_sides(a, b, c)