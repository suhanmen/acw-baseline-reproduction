def find_angle(angle1: int, angle2: int) -> int:
    """
    Calculates the third angle of a triangle given two angles.
    The sum of all angles in a triangle is always 180 degrees.
    """
    return 180 - (angle1 + angle2)