def next_Power_Of_2(n: int) -> int:
    """
    Returns the smallest power of 2 greater than or equal to n.

    This function handles edge cases explicitly:
    - If n <= 0, it returns 1 (since 2^0 = 1 is the smallest positive power of 2).
    - If n is already a power of 2, it returns n itself.
    - If n is between two powers of 2, it returns the next higher power.

    Args:
        n (int): The input number.

    Returns:
        int: The smallest power of 2 >= n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n cannot be processed (should not happen with proper integer inputs).
    """

    # Step 1: Input validation
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received: {type(n).__name__}")

    # Step 2: Handle non-positive integers
    # According to requirements: next_Power_Of_2(0) == 1, and typically for negatives we return 1
    if n <= 0:
        return 1

    # Step 3: Handle the case where n is already a power of 2
    # A number x is a power of 2 if x > 0 and (x & (x - 1)) == 0
    if _is_power_of_two(n):
        return n

    # Step 4: If not a power of 2, find the next power of 2
    # We use bit manipulation to find the next power of 2 efficiently
    # This approach avoids potential overflow in some languages, though Python handles large integers
    result = _find_next_power_of_two(n)

    return result


def _is_power_of_two(n: int) -> bool:
    """
    Checks if a given integer is a power of two.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a power of two, False otherwise.
    """
    # Must be positive and have exactly one bit set
    if n <= 0:
        return False

    # Bitwise trick: n & (n - 1) == 0 for powers of two
    return (n & (n - 1)) == 0


def _find_next_power_of_two(n: int) -> int:
    """
    Finds the smallest power of 2 greater than n using bit manipulation.

    This function works by:
    1. Subtracting 1 from n to get all bits up to the highest set bit
    2. Setting all bits to the right of the highest set bit
    3. Shifting left by 1 to get the next power of 2

    Args:
        n (int): The number for which to find the next power of 2.

    Returns:
        int: The smallest power of 2 greater than n.
    """
    # Start with a mask that has all bits set to 1 up to the most significant bit of n-1
    value = n - 1

    # Set all bits to the right of the most significant bit to 1
    # We do this in a loop to handle 32-bit, 64-bit, or arbitrary precision integers
    mask = 1
    while mask <= value:
        mask = (mask << 1) - 1  # Create a mask with all 1s up to the current bit position

    # Add 1 to the mask to get the next power of 2
    # This effectively shifts the highest bit back up
    return mask + 1