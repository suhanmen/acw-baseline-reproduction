def count(true Booleans in the given list):
    """Count the number of True booleans in the given list.

    Args:
        list: The list to be processed. Must be a list.

    Raises:
        TypeError: If the input is not a list.

    Returns:
        int: The count of True booleans in the list.
    """
    if not isinstance(input, list):
        raise TypeError("Input must be a list.")

    true_count = 0
    for element in input:
        if isinstance(element, bool) and element:
            true_count += 1

    return true_count

# Examples
assert count([True, False, True]) == 2
assert count([False, False]) == 0
assert count([True, True, True]) == 3