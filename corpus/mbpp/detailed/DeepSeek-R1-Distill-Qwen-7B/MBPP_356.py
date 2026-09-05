def find_angle(a, b):
    # Step 1: Validate the input angles
    def validate_triangle_angles(a, b):
        if a <= 0 or b <= 0 or (a + b) >= 180:
            return False
        return True

    if not validate_triangle_angles(a, b):
        raise ValueError("Invalid triangle angles: angles must be positive and sum to less than 180 degrees.")

    # Step 2: Calculate the third angle
    third_angle = 180 - (a + b)

    # Step 3: Return the calculated third angle
    return third_angle

# Example usage and assertions
print(find_angle(47, 89))  # Output: 44
print(find_angle(45, 95))  # Output: 40
print(find_angle(50, 40))  # Output: 90