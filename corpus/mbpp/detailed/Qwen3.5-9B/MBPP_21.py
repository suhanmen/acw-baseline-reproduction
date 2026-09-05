def multiples_of_num(n: int, m: int) -> list[int]:
    """
    Find m number of multiples of n.

    The function returns a list containing the first m positive multiples of n.
    Multiples are generated in increasing order starting from 1*n.

    Parameters:
    n (int): The base number to find multiples of.
    m (int): The number of multiples to return.

    Returns:
    list[int]: A list of m multiples of n.

    Raises:
    ValueError: If m is negative or zero.
    TypeError: If n or m is not an integer.
    """

    # Input validation for type checking
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Parameter 'n' must be an integer, got {type(n).__name__}")

    if not isinstance(m, int) or isinstance(m, bool):
        raise TypeError(f"Parameter 'm' must be an integer, got {type(m).__name__}")

    # Input validation for value constraints
    if m < 0:
        raise ValueError(f"Parameter 'm' must be non-negative, got {m}")

    # Handle the edge case where zero multiples are requested
    if m == 0:
        return []

    # Initialize the result list to store the multiples
    result: list[int] = []

    # Loop exactly m times to generate m multiples
    for count in range(m):
        # Calculate the current multiple: n * (count + 1)
        # We use (count + 1) because count starts at 0, but the first multiple is 1*n
        current_multiple = n * (count + 1)

        # Append the calculated multiple to the result list
        result.append(current_multiple)

    # Return the populated list of multiples
    return result