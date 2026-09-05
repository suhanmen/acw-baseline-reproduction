from typing import List, Union

def find_angle(angle1: float, angle2: float) -> float:
    """
    Calculates the third angle of a triangle given two existing angles.

    The sum of all internal angles in a Euclidean triangle must equal exactly 180 degrees.
    This function validates that the input angles are physically possible for a triangle
    before calculating the result.

    Args:
        angle1 (float): The measure of the first angle in degrees.
        angle2 (float): The measure of the second angle in degrees.

    Returns:
        float: The measure of the third angle.

    Raises:
        ValueError: If angles are non-positive, if the sum of the two angles 
                    is greater than or equal to 180, or if the inputs are not numeric.
    """

    # Validate that inputs are numeric (int or float)
    if not isinstance(angle1, (int, float)) or not isinstance(angle2, (int, float)):
        raise ValueError("Both input angles must be numeric values (integers or floats).")

    # Validate that angles are positive
    # A triangle cannot have an angle of 0 or a negative value.
    if angle1 <= 0:
        raise ValueError(f"Angle 1 must be greater than 0. Received: {angle1}")
    if angle2 <= 0:
        raise ValueError(f"Angle 2 must be greater than 0. Received: {angle2}")

    # Calculate the sum of the two provided angles
    sum_of_two_angles = angle1 + angle2

    # Validate that the sum of the two angles is less than 180 degrees.
    # If the sum is >= 180, a third positive angle cannot exist.
    if sum_of_two_angles >= 180:
        raise ValueError(
            f"The sum of the two angles ({sum_of_two_angles}) must be less than 180 degrees "
            f"to form a valid triangle."
        )

    # The sum of all three angles in a triangle is exactly 180 degrees.
    # Formula: angle1 + angle2 + angle3 = 180
    # Therefore: angle3 = 180 - (angle1 + angle2)
    third_angle = 180.0 - sum_of_two_angles

    # Return the result, ensuring it's returned as an integer if the 
    # result has no fractional part, to match the expected assertion types.
    if third_angle == int(third_angle):
        return int(third_angle)

    return third_angle

if __name__ == "__main__":
    # The following assertions verify the requirements of the problem.
    assert find_angle(47, 89) == 44
    assert find_angle(45, 95) == 40
    assert find_angle(50, 40) == 90