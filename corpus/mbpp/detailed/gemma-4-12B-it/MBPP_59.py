from typing import Union

def is_octagonal(n: int) -> int:
    """
    Calculates the nth octagonal number.

    The formula for the nth octagonal number is:
    O_n = n * (3n - 2)

    Args:
        n (int): The position of the octagonal number in the sequence (1-indexed).

    Returns:
        int: The nth octagonal number.

    Raises:
        ValueError: If the input n is less than 1.
        TypeError: If the input n is not an integer.
    """
    # Validate input type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer. Received: {type(n).__name__}")

    # Validate input value (octagonal numbers are usually defined for n >= 1)
    if n < 1:
        raise ValueError(f"Input must be a positive integer (n >= 1). Received: {n}")

    # Edge case: The first octagonal number (n=1)
    # 1 * (3(1) - 2) = 1 * (1) = 1
    if n == 1:
        return 1

    # Step 1: Calculate the multiplier part (3n - 2)
    # We break this down into explicit steps for clarity.
    triple_n = 3 * n
    multiplier = triple_n - 2

    # Step 2: Calculate the final product
    # Formula: n * (3n - 2)
    nth_octagonal_number = n * multiplier

    return nth_octagonal_number

if __name__ == "__main__":
    # Verification of provided assertions
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645