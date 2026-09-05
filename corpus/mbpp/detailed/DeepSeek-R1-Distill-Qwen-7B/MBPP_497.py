import math

def surfacearea_cone(r, h):
    # Handle invalid inputs
    if not (isinstance(r, (int, float)) and isinstance(h, (int, float))):
        return "Invalid input"
    if r < 0 or h < 0:
        return "Invalid input"

    # Calculate the slant height
    l = math.sqrt(r**2 + h**2)

    # Calculate base area
    base_area = math.pi * r**2

    # Calculate lateral surface area
    lateral_area = math.pi * r * l

    # Total surface area
    total_area = base_area + lateral_area

    return total_area