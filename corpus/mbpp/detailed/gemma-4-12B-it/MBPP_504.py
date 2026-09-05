from typing import Any


def sum_Of_Series(n: Any) -> int:
    """
    Calculates the sum of the cubes of the first n natural numbers.
    The formula for the sum of cubes of the first n natural numbers is:
    S = (n * (n + 1) / 2)^2

    Args:
        n (Any): The number of natural numbers to include in the sum.

    Returns:
        int: The sum of the cubes of the first n natural numbers.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is a negative integer.
    """

    # Step 1: Validate the input type
    # We explicitly check if the input is an integer to avoid unexpected behavior
    # with floats or other numeric types that might pass mathematical operations
    # but do not represent "natural numbers" in this context.
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer. Received: {type(n).__name__}")

    # Step 2: Validate the input value
    # Natural numbers are typically defined as positive integers (1, 2, 3...).
    # However, if n is 0, the sum is 0. Negative numbers are invalid.
    if n < 0:
        raise ValueError(f"Input must be a non-negative integer. Received: {n}")

    # Step 3: Handle the edge case for zero
    # If n is 0, there are no numbers to cube and sum.
    if n == 0:
        return 0

    # Step 4: Calculate the sum using the mathematical formula
    # The formula for the sum of the first n integers is: (n * (n + 1)) / 2
    # The sum of their cubes is the square of that result.

    # Step 4a: Calculate the sum of the first n numbers
    # We use integer division // to ensure the result remains an integer type.
    # Since (n * (n + 1)) is always even, the remainder will always be 0.
    sum_of_first_n_numbers = (n * (n + 1)) // 2

    # Step 4b: Square the result to get the sum of cubes
    cube_sum = sum_of_first_n_numbers ** 2

    # Step 5: Return the final result
    return int(cube_sum)


if __name__ == "__main__":
    # Testing the requirements provided in the prompt
    assert sum_Of_Series(5) == 225
    assert sum_Of_Series(2) == 9
    assert sum_Of_Series(3) == 36

    # Additional boundary cases
    assert sum_Of_Series(0) == 0
    assert sum_Of_Series(1) == 1