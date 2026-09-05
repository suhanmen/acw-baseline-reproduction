import math

def count_Rectangles(r):
    if r < 0:
        return 0
    diameter_squared = (2 * r) ** 2
    count = 0
    for a in range(1, int(math.sqrt(diameter_squared)) + 1):
        b_squared = diameter_squared - a ** 2
        if b_squared < a ** 2:  # Ensure b >= a to avoid duplicates
            continue
        b = math.isqrt(b_squared)
        if b * b == b_squared and a <= b:
            count += 1
    return count if r != 0 else 0

# Test cases
assert count_Rectangles(2) == 8, "Test case 1 failed"
assert count_Rectangles(1) == 1, "Test case 2 failed"
assert count_Rectangles(0) == 0, "Test case 3 failed"