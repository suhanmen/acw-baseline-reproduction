def merge_dict(first, second):
    """
    Merges two dictionaries, with the second dictionary's values taking precedence over the first's.

    Args:
        first (dict): The first input dictionary.
        second (dict): The second input dictionary.

    Returns:
        dict: A merged dictionary where the second dictionary's values overwrite the first's if keys overlap.

    Raises:
        ValueError: If either input is not a dictionary.
    """
    # Check if both arguments are dictionaries
    if not isinstance(first, dict) or not isinstance(second, dict):
        raise ValueError("Both inputs must be dictionaries.")

    # Create a new dictionary to hold the merged results
    merged = {}

    # First, add all key-value pairs from the second dictionary
    for key, value in second.items():
        merged[key] = value

    # Then, add all key-value pairs from the first dictionary, overwriting existing keys
    for key, value in first.items():
        merged[key] = value

    # Return the merged dictionary
    return merged