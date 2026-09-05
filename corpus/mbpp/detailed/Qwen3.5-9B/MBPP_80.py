import math

def is_valid_integer_input(n: int) -> bool:
    """
    Validates that the input n is a non-negative integer.

    Tetrahedral numbers are defined for non-negative integers n >= 0.
    Negative integers and non-integer inputs are invalid.

    Args:
        n (int): The input value to validate.

    Returns:
        bool: True if n is a valid non-negative integer, False otherwise.
    """
    if not isinstance(n, int):
        return False

    if n < 0:
        return False

    return True

def compute_tetrahedral_number(n: int) -> float:
    """
    Computes the nth tetrahedral number using the formula n * (n + 1) * (n + 2) / 6.

    The nth tetrahedral number represents the number of stacked spheres in a
    tetrahedron with n spheres on a side. It is the sum of the first n triangular numbers.
    Formula: T_n = n(n+1)(n+2)/6

    Args:
        n (int): The position in the sequence of tetrahedral numbers (0-indexed).

    Returns:
        float: The nth tetrahedral number as a floating-point value.
    """
    # Step 1: Calculate the term (n + 1)
    term_one_plus_n = n + 1

    # Step 2: Calculate the term (n + 2)
    term_two_plus_n = n + 2

    # Step 3: Calculate the product of n, (n + 1), and (n + 2)
    numerator = n * term_one_plus_n * term_two_plus_n

    # Step 4: Divide by 6 to get the final result
    result = numerator / 6

    return result

def tetrahedral_number(n: int) -> float:
    """
    Finds the nth tetrahedral number.

    This function includes rigorous input validation to ensure that the input
    adheres to the requirements for calculating tetrahedral numbers. It handles
    edge cases such as empty inputs (not applicable for integers), single elements,
    all-equal elements (conceptually handled by the formula), and boundary values
    like zero.

    Args:
        n (int): A non-negative integer representing the position in the sequence.

    Returns:
        float: The nth tetrahedral number.

    Raises:
        ValueError: If the input is not a valid non-negative integer.
        TypeError: If the input is not of type int.
    """
    # Validate input type first
    if not isinstance(n, int):
        raise TypeError(f"Expected input of type 'int', but got type '{type(n).__name__}'.")

    # Validate input value range
    if n < 0:
        raise ValueError(f"Input must be a non-negative integer, but received {n}.")

    # Handle the zero case explicitly (though formula works, documentation purposes)
    if n == 0:
        # T_0 = 0
        return 0.0

    # Compute and return the result using the helper function
    return compute_tetrahedral_number(n)