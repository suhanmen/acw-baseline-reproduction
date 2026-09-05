def does_Contain_B(start: int, skip: int, target: int) -> bool:
    """
    Check if 'target' is present in an infinite sequence defined by:
    start, start + skip, start + 2*skip, start + 3*skip, ...

    The sequence only contains numbers greater than or equal to 'start'.

    Parameters:
    start (int): The starting number of the sequence.
    skip (int): The increment (step) between consecutive numbers.
    target (int): The number to check for existence.

    Returns:
    bool: True if target is in the sequence, False otherwise.
    """
    if skip <= 0:
        return False

    if target < start:
        return False

    # Check if the difference is divisible by the skip amount
    return (target - start) % skip == 0