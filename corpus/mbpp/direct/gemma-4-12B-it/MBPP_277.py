def dict_filter(data: dict, threshold: int) -> dict:
    """
    Filters a dictionary to keep only the items where the value is greater than 
    or equal to the provided threshold.
    """
    return {key: value for key, value in data.items() if value >= threshold}