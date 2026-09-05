def volume_cuboid(length, width, height):
    # Input validation: check if all dimensions are valid integers
    if not (isinstance(length, int) and isinstance(width, int) and isinstance(height, int)):
        return None
    if length <= 0 or width <= 0 or height <= 0:
        return None

    # Calculate the volume of the cuboid
    volume = length * width * height

    return volume