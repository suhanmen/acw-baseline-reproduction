import math
from typing import Union

def otherside_rightangle(side_a: Union[int, float], side_b: Union[int, float]) -> float:
    """
    Calculates the length of the hypotenuse of a right-angled triangle 
    given the lengths of the two shorter sides (legs).

    The formula used is the Pythagorean theorem: c = sqrt(a^2 + b^2).

    Args:
        side_a: The length of the first side.
        side_b: The length of the second side.

    Returns:
        float: The length of the hypotenuse.

    Raises:
        ValueError: If either input side is non-positive (length must be > 0).
        TypeError: If inputs are not numeric types.
    """
    # Validate input types
    if not isinstance(side_a, (int, float)) or not isinstance(side_b, (int, float)):
        raise TypeError("Both sides must be numeric values (int or float).")

    # Validate that side lengths are positive
    # A triangle side cannot be zero or negative in Euclidean geometry
    if side_a <= 0:
        raise ValueError(f"Side A must be greater than zero. Received: {side_a}")

    if side_b <= 0:
        raise ValueError(f"Side B must be greater than zero. Received: {side_b}")

    # Step 1: Calculate the square of the first side
    # Using explicit steps to ensure clarity and prevent precision loss in intermediate steps
    sq_side_a = side_a ** 2

    # Step 2: Calculate the square of the second side
    sq_side_b = side_b ** 2

    # Step 3: Sum the squares of the two legs
    # According to Pythagoras: a^2 + b^2 = c^2
    sum_of_squares = sq_side_a + sq_side_b

    # Step 4: Calculate the square root of the sum to find the hypotenuse
    # math.sqrt is preferred over ** 0.5 for clarity and standard library efficiency
    hypotenuse = math.sqrt(sum_of_squares)

    return hypotenuse

if __name__ == "__main__":
    # Test cases provided in the problem description
    # Using math.isclose for floating point comparisons to handle precision
    assert math.isclose(otherside_rightangle(7, 8), 10.63014581273465, rel_tol=1e-9)
    assert math.isclose(otherside_rightangle(3, 4), 5.0, rel_tol=1e-9)
    assert math.isclose(otherside_rightangle(7, 15), 16.55294535724685, rel_tol=1e-9)