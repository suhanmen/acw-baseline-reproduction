from typing import Union

def minimum(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """
    Finds and returns the minimum of two numbers.

    Args:
        num1: The first number (integer or float).
        num2: The second number (integer or float).

    Returns:
        The smaller of the two provided numbers.

    Raises:
        TypeError: If either input is not an instance of int or float.
    """
    # Validate that the first input is a number
    if not isinstance(num1, (int, float)):
        raise TypeError(
            f"Input num1 must be an int or float, but got {type(num1).__name__}"
        )

    # Validate that the second input is a number
    if not isinstance(num2, (int, float)):
        raise TypeError(
            f"Input num2 must be an int or float, but got {type(num2).__name__}"
        )

    # Determine the minimum value using explicit comparison
    # We handle equality, greater than, and less than cases explicitly.
    if num1 < num2:
        result = num1
    elif num2 < num1:
        result = num2
    else:
        # This handles the case where num1 == num2, including 0 == 0
        # or cases with the same negative or positive values.
        result = num1

    return result

# Assertions to verify correctness
if __name__ == "__main__":
    # Provided test cases
    assert minimum(1, 2) == 1
    assert minimum(-5, -4) == -5
    assert minimum(0, 0) == 0

    # Additional edge cases
    assert minimum(10.5, 10.5) == 10.5
    assert minimum(-100, 50) == -100
    assert minimum(100, 50) == 50
    assert minimum(0, -1) == -1