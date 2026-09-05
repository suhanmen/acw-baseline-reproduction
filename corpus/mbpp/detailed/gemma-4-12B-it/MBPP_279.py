import math

def is_num_decagonal(n: int) -> int:
    """
    Calculates the nth decagonal number.

    A decagonal number is a figurate number that represents the number of 
    dots in a decagonal shape (a polygon with 10 sides).
    The formula for the nth decagonal number is:
    D_n = (4n^2 - 3n) / 1  which simplifies to n(4n - 3).

    Args:
        n (int): The position in the sequence of decagonal numbers.
                 Must be a non-negative integer.

    Returns:
        int: The nth decagonal number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is a negative integer.
    """
    # --- Input Validation ---

    # Check if the input is an integer type
    if not isinstance(n, int):
        raise TypeError(f"Input 'n' must be an integer, received {type(n).__name__}.")

    # Decagonal numbers are typically defined for n >= 0 or n >= 1.
    # Based on standard figurate number definitions, n = 0 results in 0.
    if n < 0:
        raise ValueError(f"Input 'n' must be a non-negative integer, received {n}.")

    # --- Handle Edge Cases ---

    # Case: n = 0
    # The 0th decagonal number is 0.
    if n == 0:
        return 0

    # Case: n = 1
    # The 1st decagonal number is 1(4(1) - 3) = 1.
    if n == 1:
        return 1

    # --- Core Logic ---

    # Formula: D_n = (4n^2 - 3n)
    # We decompose this into separate steps for maximum clarity.

    # Step 1: Calculate the square of n
    n_squared = n * n

    # Step 2: Multiply n_squared by 4
    four_times_n_squared = 4 * n_squared

    # Step 3: Calculate 3 times n
    three_times_n = 3 * n

    # Step 4: Subtract to get the result
    # D_n = 4n^2 - 3n
    decagonal_number = four_times_n_squared - three_times_n

    # Alternative mathematically equivalent form: D_n = n * (4n - 3)
    # This is sometimes preferred to avoid large intermediate squares.
    # Let's use the explicit subtraction method for maximum visibility of the polynomial.

    return decagonal_number

# The assertions provided in the problem description are verified as follows:
# n=3: 3 * (4*3 - 3) = 3 * (12 - 3) = 3 * 9 = 27
# n=7: 7 * (4*7 - 3) = 7 * (28 - 3) = 7 * 25 = 175
# n=10: 10 * (4*10 - 3) = 10 * (40 - 3) = 10 * 37 = 370