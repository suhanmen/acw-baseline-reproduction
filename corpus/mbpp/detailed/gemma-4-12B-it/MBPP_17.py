import math

def square_perimeter(side_length: float) -> float:
    """
    Calculates the perimeter of a square given the length of one side.

    A square has four equal sides. The perimeter is defined as the total 
    length of the boundary, which is side_length * 4.

    Args:
        side_length (float): The length of one side of the square. 
                              Must be a non-negative number.

    Returns:
        float: The perimeter of the square.

    Raises:
        ValueError: If the side_length is negative.
        TypeError: If the side_length is not a numeric type (int or float).
    """

    # 1. Validate input type
    # We ensure the input is either an integer or a float.
    # This prevents errors further down the pipeline if a string or list is passed.
    if not isinstance(side_length, (int, float)):
        raise TypeError(
            f"Input must be a number (int or float), "
            f"but received {type(side_length).__name__}."
        )

    # 2. Validate input value range
    # Geometrically, a side length cannot be negative.
    # We allow zero, which represents a degenerate square (a point) with zero perimeter.
    if side_length < 0:
        raise ValueError(
            f"Side length cannot be negative. Received: {side_length}"
        )

    # 3. Handle the calculation logic
    # Perimeter = side + side + side + side
    # Or Perimeter = 4 * side
    # We use the multiplication approach for clarity and performance.

    number_of_sides: int = 4
    perimeter: float = float(side_length * number_of_sides)

    # 4. Return the final calculated result
    return perimeter

# Verification of assertions
if __name__ == "__main__":
    # These assertions confirm the requirements provided in the problem statement.
    assert square_perimeter(10) == 40
    assert square_perimeter(5) == 20
    assert square_perimeter(4) == 16