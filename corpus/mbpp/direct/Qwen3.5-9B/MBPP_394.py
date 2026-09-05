def check_distinct(t):
    """
    Check if all elements in the given tuple are distinct.

    Parameters:
    t (tuple): The tuple to check.

    Returns:
    bool: True if all elements are distinct, False otherwise.
    """
    return len(t) == len(set(t))