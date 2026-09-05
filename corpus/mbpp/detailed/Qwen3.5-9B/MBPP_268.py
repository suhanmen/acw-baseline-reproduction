def validate_input(n):
    """
    Validates that the input n is a positive integer (n >= 1).
    Raises a TypeError if the input is not an integer.
    Raises a ValueError if the input is less than 1.
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    if n < 1:
        raise ValueError(f"Input must be a positive integer (>= 1), got {n}")

def calculate_star_number(n):
    """
    Calculates the n'th star number using the explicit mathematical formula.

    The formula for the n-th star number is:
    S(n) = 6 * n^2 - 6 * n + 1

    This corresponds to the center of a hexagonal star with n cells on each arm.
    For n=1: 6(1) - 6(1) + 1 = 1
    For n=2: 6(4) - 12 + 1 = 13
    For n=3: 6(9) - 18 + 1 = 37
    For n=4: 6(16) - 24 + 1 = 73
    For n=5: 6(25) - 30 + 1 = 121
    """
    # Calculate the square of n
    n_squared = n * n

    # Calculate the first term: 6 * n^2
    term_one = 6 * n_squared

    # Calculate the second term: 6 * n
    term_two = 6 * n

    # Calculate the subtraction part: term_one - term_two
    # Formula is 6n^2 - 6n, so we compute this intermediate sum/difference first
    variable_part = term_one - term_two

    # Add the constant 1 to get the final result
    result = variable_part + 1

    return result

def find_star_num(n):
    """
    Public function to find the n'th star number.

    This function acts as the entry point. It validates the input
    and delegates the calculation logic to calculate_star_number.

    Args:
        n (int): A positive integer representing the index of the star number.

    Returns:
        int: The n'th star number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is less than 1.
    """
    # Explicitly handle the validation step
    validate_input(n)

    # Delegate to the calculation helper
    return calculate_star_number(n)