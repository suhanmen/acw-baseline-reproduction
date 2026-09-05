from typing import Any

def centered_hexagonal_number(n: int) -> int:
    """
    Calculates the nth centered hexagonal number.

    The formula for the nth centered hexagonal number is given by:
    H(n) = 3 * n * (n - 1) + 1

    Where:
    - n = 1 yields 1
    - n = 2 yields 7
    - n = 3 yields 19
    - n = 4 yields 37
    - etc.

    Args:
        n (int): The position in the sequence (must be a positive integer).

    Returns:
        int: The nth centered hexagonal number.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is not a positive integer (n < 1).
    """

    # Validate input type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer. Received: {type(n).__name__}")

    # Validate input value (n must be 1, 2, 3, ...)
    # Note: Some definitions start at n=0 (H(0)=1), but the provided assertions 
    # (n=2 -> 7, n=9 -> 217) confirm the standard sequence starting at n=1.
    if n < 1:
        raise ValueError(f"Input must be a positive integer (n >= 1). Received: {n}")

    # Edge case: n = 1
    # H(1) = 3 * 1 * (1 - 1) + 1 = 1
    if n == 1:
        return 1

    # Calculation of the nth centered hexagonal number
    # Formula: H(n) = 3n(n-1) + 1

    # Step 1: Calculate (n - 1)
    previous_index = n - 1

    # Step 2: Calculate the product of n and (n - 1)
    product_n_prev = n * previous_index

    # Step 3: Multiply the product by 3
    triple_product = 3 * product_n_prev

    # Step 4: Add 1 to get the final centered hexagonal number
    result = triple_product + 1

    return result

# Verification against provided assertions:
# assert centered_hexagonal_number(10) == 271  -> 3*10*(9) + 1 = 270 + 1 = 271
# assert centered_hexagonal_number(2) == 7     -> 3*2*(1) + 1 = 6 + 1 = 7
# assert centered_hexagonal_number(9) == 217   -> 3*9*(8) + 1 = 216 + 1 = 217