def check_distinct(t):
    """
    Check if all elements in the given tuple are distinct.

    Args:
        t (tuple): The input tuple to check.

    Returns:
        bool: True if all elements are distinct, False otherwise.
    """
    # Convert the tuple to a set to remove duplicates
    unique_elements = set(t)

    # Compare the length of the original tuple with the set
    if len(t) == len(unique_elements):
        return True
    else:
        return False