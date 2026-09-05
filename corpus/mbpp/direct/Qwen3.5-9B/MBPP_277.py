def dict_filter(d: dict, value: any) -> dict:
    """
    Filters a dictionary to include only entries where the value matches the specified target value.

    Args:
        d (dict): The input dictionary.
        value (any): The target value to filter by.

    Returns:
        dict: A new dictionary containing only entries with matching values.
    """
    return {k: v for k, v in d.items() if v == value}