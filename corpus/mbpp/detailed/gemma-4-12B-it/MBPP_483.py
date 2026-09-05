import math

def first_Factorial_Divisible_Number(x: int) -> int:
    """
    Finds the first natural number n (n >= 1) such that n! is divisible by x.

    A natural number is defined as a positive integer {1, 2, 3, ...}.
    The factorial of n (n!) is the product of all positive integers less than or equal to n.

    Args:
        x (int): The divisor to check against.

    Returns:
        int: The smallest natural number n such that n! % x == 0.

    Raises:
        ValueError: If x is not a positive integer.
    """

    # --- Input Validation ---
    # The problem implies x should be a value such that a factorial can divide it.
    # Factorials are always positive. Division by zero is undefined.
    # If x is 1, 1! is divisible by 1, so the answer is 1.
    if not isinstance(x, int):
        raise ValueError("Input x must be an integer.")

    if x <= 0:
        raise ValueError("Input x must be a positive integer (natural number).")

    # --- Edge Case Handling ---
    # If x is 1, the first natural number whose factorial is divisible by 1 is 1.
    if x == 1:
        return 1

    # --- Iterative Search ---
    # We start checking from n = 1 upwards.
    # We keep track of the running factorial to avoid recomputing products.
    # To handle very large numbers of x, we use the property that n! % x == 0.
    # However, since x is the divisor, we can also check if the current factorial
    # product is a multiple of x.

    current_n = 1
    current_factorial = 1

    while True:
        # Calculate n!
        # Instead of using math.factorial(current_n) every time (O(n^2)),
        # we multiply the previous result by the current n (O(n)).
        current_factorial *= current_n

        # Check if current_factorial is divisible by x
        remainder = current_factorial % x

        if remainder == 0:
            return current_n

        # Increment to check the next natural number
        current_n += 1

        # Safety break for extremely large values (optional but good for production)
        # Mathematically, for any x, the answer is at most x (since x! is divisible by x).
        if current_n > x:
            # This part should theoretically never be reached for x > 0
            # because x! is always divisible by x.
            return x

# Helper functions are not strictly needed for this logic, 
# but we ensure the flow is clear and explicit.