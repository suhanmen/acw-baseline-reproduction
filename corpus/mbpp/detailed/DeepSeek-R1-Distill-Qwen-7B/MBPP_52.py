def parallelogram_area(base, height):
    # Validate the inputs: base and height must be integers and non-negative
    if not isinstance(base, int) or not isinstance(height, int):
        return None
    if base < 0 or height < 0:
        return None

    # Calculate the area of the parallelogram
    area = base * height

    return area

# Test cases to verify the correctness of the function
assert parallelogram_area(10, 20) == 200, "Test case 1 failed"
assert parallelogram_area(15, 20) == 300, "Test case 2 failed"
assert parallelogram_area(8, 9) == 72, "Test case 3 failed"
print("All test cases passed successfully")