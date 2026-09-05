from typing import Union

def min_of_three(num1: Union[int, float], num2: Union[int, float], num3: Union[int, float]) -> Union[int, float]:
    """
    Finds the minimum of three numbers provided as arguments.

    Args:
        num1: The first number.
        num2: The second number.
        num3: The third number.

    Returns:
        The smallest of the three numbers.

    Raises:
        TypeError: If any of the inputs are not integers or floats.
    """

    # Validate that all inputs are numeric (int or float)
    # Defensive programming ensures we catch invalid types early.
    inputs = [num1, num2, num3]
    for item in inputs:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All inputs must be integers or floats. Received: {type(item).__name__}")

    # Step 1: Identify the smallest between the first two numbers
    # We use explicit comparison rather than a built-in min() to show logic.
    if num1 < num2:
        current_min = num1
    else:
        current_min = num2

    # Step 2: Compare the current minimum with the third number
    if num3 < current_min:
        final_min = num3
    else:
        final_min = current_min

    # Step 3: Return the final result
    return final_min

# Testing logic to verify the requirements provided in the prompt
if __name__ == "__main__":
    # Standard assertions provided in the problem description
    assert min_of_three(10, 20, 0) == 0
    assert min_of_three(19, 15, 18) == 15
    assert min_of_three(-10, -20, -30) == -30

    # Additional edge case checks for production-grade robustness
    # All equal elements
    assert min_of_three(5, 5, 5) == 5
    # Large numbers
    assert min_of_three(1000000, 2000000, 3000000) == 1000000
    # Floating point numbers
    assert min_of_three(1.5, 0.5, 2.5) == 0.5
    # Zeroes and Negatives
    assert min_of_three(0, -1, 1) == -1