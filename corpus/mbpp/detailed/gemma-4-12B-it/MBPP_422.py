from typing import Union

def find_Average_Of_Cube(n: Union[int, float]) -> float:
    """
    Calculates the average of the cubes of the first n natural numbers.

    Natural numbers are defined here as positive integers (1, 2, 3, ...).
    The average is defined as: (1^3 + 2^3 + ... + n^3) / n.

    Args:
        n: The number of natural numbers to consider.

    Returns:
        The average of the cubes as a float.

    Raises:
        ValueError: If n is not a positive integer.
        TypeError: If n is not an integer type.
    """
    # --- Input Validation ---

    # Check if input is an integer type
    # Note: Using isinstance(n, int) and not isinstance(n, bool) 
    # because bools are subclasses of int in Python.
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Input 'n' must be an integer. Received: {type(n).__name__}")

    # Check if n is a positive natural number
    # Natural numbers in this context starts from 1.
    if n <= 0:
        raise ValueError(f"Input 'n' must be a positive natural number (greater than 0). Received: {n}")

    # --- Calculation ---

    # We can calculate the sum of cubes using the mathematical formula:
    # Sum = [n * (n + 1) / 2]^2
    # Or we can calculate it iteratively. Given the requirement for 
    # explicit steps and production-grade code, we will perform the 
    # calculation clearly.

    total_sum_of_cubes: int = 0

    # Iterate from 1 to n (inclusive)
    for current_number in range(1, n + 1):
        # Calculate the cube of the current number
        cube_value: int = current_number ** 3

        # Accumulate the sum
        total_sum_of_cubes += cube_value

    # The average is the total sum divided by the count of numbers (n)
    # We cast to float explicitly to ensure the result is a float.
    average_value: float = float(total_sum_of_cubes) / float(n)

    return average_value

# Testing the assertions provided in the problem description
if __name__ == "__main__":
    # Test Case 1: n = 2
    # Cubes: 1^3=1, 2^3=8. Sum = 9. Average = 9/2 = 4.5
    assert find_Average_Of_Cube(2) == 4.5

    # Test Case 2: n = 3
    # Cubes: 1^3=1, 2^3=8, 3^3=27. Sum = 36. Average = 36/3 = 12.0
    assert find_Average_Of_Cube(3) == 12.0

    # Test Case 3: n = 1
    # Cubes: 1^3=1. Sum = 1. Average = 1/1 = 1.0
    assert find_Average_Of_Cube(1) == 1.0