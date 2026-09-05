from typing import Tuple, Union

Number = Union[int, float]

def _validate_angles(angle_a: Number, angle_b: Number) -> None:
    """
    Validates that the two input angles are valid for a triangle.

    Rules:
    1. Both inputs must be numeric (int or float).
    2. Both inputs must be positive.
    3. The sum of the two angles must be less than 180 (since the third angle must be positive).
    4. The sum of the two angles cannot be exactly 180 (which would imply the third is 0).
    """
    # Check if inputs are numbers
    if not isinstance(angle_a, (int, float)) or not isinstance(angle_b, (int, float)):
        raise TypeError("Both angles must be numeric (int or float).")

    # Check for NaN (Not a Number)
    if isinstance(angle_a, float) and (angle_a != angle_a):  # NaN check
        raise ValueError("An angle cannot be NaN.")
    if isinstance(angle_b, float) and (angle_b != angle_b):  # NaN check
        raise ValueError("An angle cannot be NaN.")

    # Check for Infinity
    if isinstance(angle_a, float) and (angle_a == float('inf') or angle_a == float('-inf')):
        raise ValueError("An angle cannot be infinite.")
    if isinstance(angle_b, float) and (angle_b == float('inf') or angle_b == float('-inf')):
        raise ValueError("An angle cannot be infinite.")

    # Check if angles are positive
    if angle_a <= 0:
        raise ValueError(f"An angle must be positive, but received: {angle_a}.")
    if angle_b <= 0:
        raise ValueError(f"An angle must be positive, but received: {angle_b}.")

    # Check if the sum is valid for a triangle
    sum_ab = angle_a + angle_b
    if sum_ab >= 180:
        raise ValueError(
            f"The sum of the two angles ({sum_ab}) must be strictly less than 180 "
            f"to form a valid triangle."
        )

def calculate_third_angle(angle_a: Number, angle_b: Number) -> Number:
    """
    Calculates the third angle of a triangle given two angles.

    Logic:
    The sum of internal angles in a Euclidean triangle is always 180 degrees.
    Therefore, angle_c = 180 - (angle_a + angle_b).

    This function validates inputs and performs the arithmetic explicitly.
    """
    # 1. Validate the inputs before calculation
    _validate_angles(angle_a, angle_b)

    # 2. Calculate the sum of the provided angles
    sum_of_given_angles = angle_a + angle_b

    # 3. Calculate the third angle by subtracting the sum from 180
    third_angle = 180.0 - sum_of_given_angles

    # 4. Re-validate the result to ensure it's positive (defensive check)
    if third_angle <= 0:
        # This should have been caught by the sum check, but explicit here for clarity
        raise ValueError("Calculated third angle is not positive, indicating invalid input.")

    return third_angle

def find_angle(angle_a: Number, angle_b: Number) -> Number:
    """
    Public interface to find the third angle of a triangle.

    Wrapper function that delegates to calculate_third_angle.
    Maintains the exact signature required by the problem.
    """
    return calculate_third_angle(angle_a, angle_b)