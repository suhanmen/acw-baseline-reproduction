def compute_Last_Digit(n_a: int, n_b: int) -> int:
    """
    Computes the last digit of (b! / a!) where a <= b.
    This is equivalent to finding the last digit of the product: (a+1) * (a+2) * ... * b.

    If a > b, the factorial division results in a fraction (0 in integer division context),
    but mathematically b!/a! is not an integer. We will raise an error for invalid input a > b.

    Edge cases handled:
    - Empty input is not possible due to type hints requiring integers.
    - Single element: if a == b, the result is 1 (last digit 1).
    - All-equal elements in range: handled naturally by the loop.
    - Zero and negative numbers: 
        * 0! = 1. 
        * Factorials are defined for non-negative integers only. Negative inputs raise ValueError.
    - Boundary values: n=0, n=1 are handled correctly by the logic.

    Args:
        n_a (int): The divisor's base factorial argument (a).
        n_b (int): The numerator's base factorial argument (b).

    Returns:
        int: The last digit of (b! // a!).

    Raises:
        ValueError: If n_a or n_b are negative, or if n_a > n_b.
        TypeError: If inputs are not integers.
    """

    # Step 1: Input Validation - Type Checking
    # Ensure both arguments are integers (but not bool, as bool is a subclass of int in Python)
    if not isinstance(n_a, int) or isinstance(n_a, bool):
        raise TypeError("n_a must be an integer.")
    if not isinstance(n_b, int) or isinstance(n_b, bool):
        raise TypeError("n_b must be an integer.")

    # Step 2: Input Validation - Domain Constraints
    # Factorials are not defined for negative numbers.
    if n_a < 0:
        raise ValueError("n_a must be a non-negative integer.")
    if n_b < 0:
        raise ValueError("n_b must be a non-negative integer.")

    # Mathematical constraint for b! / a! to be an integer is a <= b.
    if n_a > n_b:
        raise ValueError("n_a must be less than or equal to n_b for integer division.")

    # Step 3: Determine the calculation logic
    # We need to calculate (b! / a!).
    # This expands to the product of integers from (n_a + 1) to n_b inclusive.
    # Product = (n_a + 1) * (n_a + 2) * ... * n_b
    # If n_a == n_b, the product is empty (identity for multiplication), result is 1.

    # Determine the start and end of our multiplication range.
    start_multiplier = n_a + 1
    end_multiplier = n_b

    # Step 4: Handle the specific case where start > end
    # This happens if n_a == n_b. The range is empty.
    if start_multiplier > end_multiplier:
        # The product of an empty set is 1.
        # Last digit of 1 is 1.
        final_result = 1
    else:
        # Step 5: Initialize accumulator
        current_product = 1

        # Step 6: Explicitly iterate through the range [start_multiplier, end_multiplier]
        # We use a named loop variable for clarity.
        for current_factor in range(start_multiplier, end_multiplier + 1):
            # Multiply the current factor into our product
            current_product = current_product * current_factor

            # Optimization/Requirement: Keep numbers small to avoid huge integers
            # if not strictly necessary for correctness (Python handles big ints),
            # but we specifically need only the last digit.
            # However, the problem asks for the last digit of the division result.
            # We must compute the full product modulo 10.
            # Note: (A * B) % 10 == ((A % 10) * (B % 10)) % 10.
            # We can apply modulo at each step to keep numbers small.
            current_product = current_product % 10

        final_result = current_product

    return final_result