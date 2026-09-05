def lateralsurface_cuboid(length, width, height):
    # Step 1: Input Validation
    # Check if all inputs are numbers and positive
    if not all(isinstancedim, (int, float)) for dim in (length, width, height)):
        return None
    if length <= 0 or width <= 0 or height <= 0:
        return None

    # Step 2: Calculate the Lateral Surface Area
    lateral_area = 2 * height * (length + width)

    # Step 3: Return the Result
    return lateral_area

# Example test cases
print(lateralsurface_cuboid(8, 5, 6))    # Output: 156
print(lateralsurface_cuboid(7, 9, 10))   # Output: 320
print(lateralsurface_cuboid(10, 20, 30))  # Output: 1800