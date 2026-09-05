import math
from typing import Union

def babylonian_squareroot(number: Union[int, float]) -> float:
    """
    Computes the square root of a non-negative number using the 
    Babylonian method (also known as Hero's method or Newton's method).

    The Babylonian method is an iterative algorithm that starts with an 
    initial guess and refines it using the formula:
    x_{n+1} = 0.5 * (x_n + number / x_n)

    Args:
        number (Union[int, float]): The number to find the square root of.

    Returns:
        float: The approximate square root of the input number.

    Raises:
        ValueError: If the input number is negative.
        TypeError: If the input is not an integer or a float.
    """

    # --- Input Validation ---

    # Ensure the input type is numeric
    if not isinstance(number, (int, float)):
        raise TypeError(f"Input must be an integer or float, got {type(number).__name__}")

    # Square roots of negative numbers are not real numbers
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number.")

    # --- Handle Edge Cases ---

    # Case 1: The square root of 0 is 0.
    if number == 0:
        return 0.0

    # Case 2: The square root of 1 is 1.
    if number == 1:
        return 1.0

    # --- Babylonian Method Logic ---

    # Initial Guess: 
    # A common starting point is the number itself, or number / 2.
    # For very large numbers, number/2 is safe; for small numbers, 1.0 is safe.
    # Using the number itself as the starting point is mathematically robust.
    current_guess: float = float(number)

    # Define the precision threshold. 
    # The target values in the prompt imply standard 64-bit float precision.
    # We continue until the difference between iterations is negligible.
    epsilon: float = 1e-15

    # We use a maximum iteration count to prevent infinite loops in 
    # cases of extreme floating point precision issues.
    max_iterations: int = 1000

    for i in range(max_iterations):
        # Calculate the next guess based on the Babylonian formula:
        # next_guess = (current_guess + number / current_guess) / 2

        division_step: float = number / current_guess
        next_guess: float = 0.5 * (current_guess + division_step)

        # Calculate the absolute difference between the current guess and the next guess
        difference: float = abs(next_guess - current_guess)

        # Update the current guess for the next iteration
        current_guess = next_guess

        # Check if the change is smaller than our precision threshold
        if difference < epsilon:
            # Convergence reached
            break

    return current_guess

# The following assertions confirm the correctness of the implementation.
if __name__ == "__main__":
    # These are the required test cases from the problem description.
    # Using math.isclose is safer for floating point comparisons, but the 
    # prompt asks for exact matching or at least verification of these specific values.
    assert babylonian_squareroot(10) == 3.162277660168379
    assert babylonian_squareroot(2) == 1.414213562373095
    assert babylonian_squareroot(9) == 3.0