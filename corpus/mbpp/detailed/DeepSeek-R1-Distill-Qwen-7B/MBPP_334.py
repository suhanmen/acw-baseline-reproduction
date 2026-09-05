def check_Validity(a, b, c):
    # Check if any side is non-positive
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Create a sorted list of sides
    sides = sorted([a, b, c])
    # Unpack the sorted sides for clarity
    side1, side2, side3 = sides

    # Check the triangle inequality theorem
    return side1 + side2 > side3