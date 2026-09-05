def count_With_Odd_SetBits(n: int) -> int:
    """
    Counts the number of integers between 1 and n (inclusive) that have an odd number of set bits (1s in binary).

    Parameters:
        n (int): The upper bound of the range to consider. Must be a positive integer.

    Returns:
        int: The count of integers in the range [1, n] with an odd number of set bits.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is less than 1.
    """
    # Validate input type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received {type(n).__name__}")

    # Validate input value
    if n < 1:
        raise ValueError(f"Input must be greater than or equal to 1, received {n}")

    count = 0

    # Iterate through each number from 1 to n inclusive
    for current_number in range(1, n + 1):
        # Count the number of set bits (1s) for the current number
        set_bits_count = bin(current_number).count('1')

        # Check if the count of set bits is odd
        if set_bits_count % 2 == 1:
            count += 1

    return count