import math
from typing import Union

def hexagonal_num(n: Union[int, float]) -> int:
    """
    Calculates the nth hexagonal number.

    The formula for the nth hexagonal number is:
    H(n) = n * (2n - 1)

    Args:
        n: The position in the hexagonal number sequence. 
           Must be a positive integer.

    Returns:
        The nth hexagonal number as an integer.

    Raises:
        ValueError: If n is not a positive integer.
        TypeError: If n is not an integer or a float that represents an integer.
    """
    # Step 1: Validate Input Type
    # We allow floats that are mathematically integers (e.g., 5.0), 
    # but we must ensure they are numeric.
    if not isinstance(n, (int, float)):
        raise TypeError(f"Input 'n' must be a number, received {type(n).__name__}.")

    # Step 2: Validate Input Value
    # Hexagonal numbers are defined for n = 1, 2, 3...
    # We check if it is a mathematical integer first.
    if n != int(n):
        raise ValueError(f"Input 'n' must be an integer, received {n}.")

    # Convert to integer for consistent arithmetic
    n_int = int(n)

    if n_int <= 0:
        raise ValueError(f"Input 'n' must be a positive integer (n > 0), received {n_int}.")

    # Step 3: Handle Edge Cases
    # n = 1 is the first hexagonal number: 1 * (2*1 - 1) = 1
    if n_int == 1:
        return 1

    # Step 4: Perform Calculation
    # Formula: H(n) = n(2n - 1)
    # We break this down into explicit intermediate steps to ensure clarity.

    # Calculate the multiplier (2n - 1)
    two_n = 2 * n_int
    multiplier = two_n - 1

    # Final calculation
    result = n_int * multiplier

    # Step 5: Return Result
    return result

# Assertions for verification
if __name__ == "__main__":
    assert hexagonal_num(10) == 190
    assert hexagonal_num(5) == 45
    assert hexagonal_num(7) == 91