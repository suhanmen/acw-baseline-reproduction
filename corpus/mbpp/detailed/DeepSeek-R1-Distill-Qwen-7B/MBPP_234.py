def volume_cube(edge):
    # Input validation
    if not isinstance(edge, int) or edge < 0:
        raise ValueError("Edge length must be a non-negative integer")

    # Calculate the volume
    volume = edge ** 3

    return volume

# Testing the function with the provided assertions
print(volume_cube(3))  # Output: 27
print(volume_cube(2))  # Output: 8
print(volume_cube(5))  # Output: 125