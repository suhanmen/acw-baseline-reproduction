def check_isosceles(a, b, c):
    """
    Checks if a triangle with side lengths a, b, and c is isosceles.
    An isosceles triangle must have at least two sides of equal length
    and must satisfy the triangle inequality theorem.
    """
    # First, check if the side lengths can form a valid triangle
    # The sum of any two sides must be greater than the third side.
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False

    # Check if at least two sides are equal
    if a == b or b == c or a == c:
        return True

    return False

if __name__ == "__main__":
    assert check_isosceles(6, 8, 12) == False
    assert check_isosceles(6, 6, 12) == True
    assert check_isosceles(6, 16, 20) == False