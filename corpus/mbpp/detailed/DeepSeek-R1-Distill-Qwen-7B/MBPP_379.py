def surfacearea_cuboid(l, w, h):
    # Input validation: check if all inputs are positive numbers
    if not (isinstance(l, (int, float)) and isinstance(w, (int, float)) and isinstance(h, (int, float))):
        raise ValueError("All dimensions must be numbers")
    if l <= 0 or w <= 0 or h <= 0:
        raise ValueError("Dimensions must be positive")

    # Calculate the areas of each pair of faces
    lw = l * w
    lh = l * h
    wh = w * h

    # Sum the areas and multiply by 2
    total_area = 2 * (lw + lh + wh)

    return total_area

# Verify the correctness of the function with provided test cases
assert surfacearea_cuboid(1, 2, 3) == 22, "Test case 1 failed"
assert surfacearea_cuboid(5, 7, 9) == 286, "Test case 2 failed"
assert surfacearea_cuboid(10, 15, 21) == 1350, "Test case 3 failed"
print("All test cases passed!")