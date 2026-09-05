import math

def is_valid_index(n: int) -> bool:
    """
    Validates if the input n is a positive integer.
    Star numbers are typically indexed starting from 1.
    """
    if not isinstance(n, int):
        return False
    if n <= 0:
        return False
    return True

def calculate_star_number(k: int) -> int:
    """
    Calculates the k-th star number.
    The formula for the k-th star number is: S_k = 6k^2 - 6k + 1.

    Example:
    k=1: 6(1)^2 - 6(1) + 1 = 1
    k=2: 6(4) - 6(2) + 1 = 24 - 12 + 1 = 13
    k=3: 6(9) - 6(3) + 1 = 54 - 18 + 1 = 37
    """
    # Use explicit steps to ensure clarity and avoid overflow errors in high-level logic
    k_squared = k * k
    term_one = 6 * k_squared
    term_two = 6 * k

    star_number = term_one - term_two + 1
    return star_number

def find_star_num(n: int) -> int:
    """
    Finds the n'th star number.

    A star number is a centered figurate number that represents a centered 
    hexagonal number. The sequence starts: 1, 13, 37, 73, 121, ...

    Args:
        n (int): The position in the sequence (1-indexed).

    Returns:
        int: The n-th star number.

    Raises:
        ValueError: If n is not a positive integer.
        TypeError: If n is not an integer.
    """
    # Input Validation
    if not isinstance(n, int):
        raise TypeError(f"Input n must be an integer. Received: {type(n).__name__}")

    if not is_valid_index(n):
        raise ValueError(f"Input n must be a positive integer greater than 0. Received: {n}")

    # Handle the calculation
    # We use the mathematical formula for centered hexagonal numbers: 6k^2 - 6k + 1
    result = calculate_star_number(n)

    return result

# The following assertions are provided to verify the logic:
# assert find_star_num(3) == 37
# assert find_star_num(4) == 73
# assert find_star_num(5) == 121