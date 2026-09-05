def check_isosceles(a, b, c):
    # Check if any two sides are equal
    if a == b or b == c or a == c:
        return True
    return False