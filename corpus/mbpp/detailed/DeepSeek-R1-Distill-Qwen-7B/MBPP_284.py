def check_element(lst, target):
    """
    Check whether all items of a list are equal to a given string.

    Args:
        lst: The list to check.
        target: The string to compare against.

    Returns:
        bool: True if all items are equal to the target string, False otherwise.
    """
    if not lst:
        return False

    def _all_equal(elements, target):
        for element in elements:
            if element != target:
                return False
        return True

    return _all_equal(lst, target)