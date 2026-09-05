from typing import Union

def maximum(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """
    Finds and returns the maximum of two numbers.

    Args:
        num1 (Union[int, float]): The first number to compare.
        num2 (Union[int, float]): The second number to compare.

    Returns:
        Union[int, float]: The larger of the two input numbers.

    Raises:
        TypeError: If either input is not an integer or a float.
        ValueError: If inputs are NaN (Not a Number).
    """
    # Step 1: Validate that inputs are numbers (int or float)
    # We check types explicitly to ensure production-grade robustness.
    if not isinstance(num1, (int, float)):
        raise TypeError(f"Input num1 must be an int or float, got {type(num1).__name__}")

    if not isinstance(num2, (int, float)):
        raise TypeError(f"Input num2 must be an int or float, got {type(num2).__name__}")

    # Step 2: Handle NaN (Not a Number) edge cases
    # Comparison logic with NaN can lead to non-deterministic results in some contexts.
    if num1 != num1:
        raise ValueError("Input num1 is NaN (Not a Number)")
    if num2 != num2:
        raise ValueError("Input num2 is NaN (Not a Number)")

    # Step 3: Perform the comparison logic
    # We use explicit control flow to determine the result.
    if num1 > num2:
        result = num1
    elif num2 > num1:
        result = num2
    else:
        # This handles the case where numbers are exactly equal.
        # In such a case, either number is the maximum.
        result = num1

    return result

if __name__ == "__main__":
    # Verification of provided assertions
    assert maximum(5, 10) == 10
    assert maximum(-1, -2) == -1
    assert maximum(9, 7) == 9