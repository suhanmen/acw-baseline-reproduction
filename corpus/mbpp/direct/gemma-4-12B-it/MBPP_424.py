def extract_rear(data: tuple) -> list:
    """
    Extracts the last character of each string in the given tuple.
    """
    return [item[-1] for item in data]