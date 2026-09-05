def check_value(d, value):
    """
    Check if all values in the dictionary are equal to the given value.

    Args:
        d (dict): The dictionary to check.
        value (int): The value to compare against.

    Returns:
        bool: True if all values match, False otherwise.

    Raises:
        TypeError: If the input dictionary is not a dictionary or if the values are of different types.
    """
    # Check if the input is a dictionary
    if not isinstance(d, dict):
        raise TypeError("The first argument must be a dictionary.")

    # If the dictionary is empty, return False
    if not d:
        return False

    # Get the first value to compare against
    first_value = next(iter(d.values()))

    # Check if all values are of the same type as the first value
    for k, v in d.items():
        if not isinstance(v, type(first_value)):
            return False

    # Compare each value to the first value
    for k, v in d.items():
        if v != first_value:
            return False

    # If all checks passed, return True
    return True