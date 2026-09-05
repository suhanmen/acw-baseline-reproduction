def check_isosceles(a, b, c):
    # Input validation: check that all sides are positive
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise ValueError("All sides must be numbers")
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive")

    # Check triangle inequality
    if not (a + b > c and a + c > b and b + c > a):
        return False

    # Check for isosceles condition
    isosceles = False
    if a == b or a == c or b == c:
        isosceles = True

    return isosceles