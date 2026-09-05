def check_equilateral(a, b, c):
    """
    Checks if a triangle with side lengths a, b, and c is equilateral.
    A triangle is equilateral if all three sides are equal.
    Additionally, it must satisfy the triangle inequality (the sum of any two sides 
    must be greater than the third), though for equilateral triangles, 
    this simplifies to checking if a > 0.
    """
    # Check if all sides are equal
    if a == b == c:
        # Check if it's a valid triangle (sides must be greater than 0)
        if a > 0:
            return True
    return False

if __name__ == "__main__":
    assert check_equilateral(6, 8, 12) == False
    assert check_equilateral(6, 6, 12) == False
    assert check_equilateral(6, 6, 6) == True