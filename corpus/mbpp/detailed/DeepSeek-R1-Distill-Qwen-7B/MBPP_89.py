def closest_num(n):
    """
    Finds the closest smaller number than n.

    Args:
        n (int): The input number to find the closest smaller number for.

    Returns:
        int: The closest smaller number than n, or None if no such number exists.
    """
    # Handle the case where n is less than or equal to 0
    if n <= 0:
        return None

    # Create a set of numbers from 0 to n-1
    candidates = set(range(n))

    # If there are no candidates (only possible if n is 0 or 1)
    if not candidates:
        return None

    # Find the maximum number in the candidates set
    closest = max(candidates)

    return closest