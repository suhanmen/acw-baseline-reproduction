import math

def perimeter_pentagon(side_length: float) -> float:
    """
    Calculates the perimeter of a regular pentagon given the length of one side.

    A regular pentagon is a polygon with 5 equal sides. 
    The perimeter is the sum of the lengths of all five sides.

    Args:
        side_length (float): The length of a single side of the pentagon.
                              Must be a non-negative number.

    Returns:
        float: The total perimeter of the pentagon.

    Raises:
        ValueError: If the side_length is negative.
        TypeError: If the side_length is not an integer or a float.
    """
    # 1. Validate Input Type
    # Ensure that the input is either an integer or a float to prevent 
    # unexpected behavior from strings, lists, or None types.
    if not isinstance(side_length, (int, float)):
        raise TypeError(
            f"Input 'side_length' must be a numeric type (int or float). "
            f"Received: {type(side_length).__name__}"
        )

    # 2. Validate Input Value
    # A physical dimension like a side length cannot be negative.
    # We allow 0 as a degenerate case (a point), which results in a perimeter of 0.
    if side_length < 0:
        raise ValueError(
            f"Side length cannot be negative. Received: {side_length}"
        )

    # 3. Define Constant
    # A pentagon always has exactly 5 sides.
    NUMBER_OF_SIDES = 5

    # 4. Calculate Perimeter
    # The perimeter is the product of the number of sides and the length of one side.
    # Using multiplication instead of repeated addition for clarity and efficiency.
    perimeter = side_length * NUMBER_OF_SIDES

    # 5. Return Result
    # Return the calculated value as a float to maintain consistency.
    return float(perimeter)

# The provided assertions are verified as follows:
# perimeter_pentagon(5)  -> 5 * 5 = 25
# perimeter_pentagon(10) -> 10 * 5 = 50
# perimeter_pentagon(15) -> 15 * 5 = 75