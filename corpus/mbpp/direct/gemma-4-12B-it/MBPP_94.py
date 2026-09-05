def index_minimum(data: list) -> str:
    """
    Extracts the name (first element) of the tuple with the minimum value (second element)
    from a list of tuples.
    """
    if not data:
        return None

    # Use min with a key function that looks at the second element of each tuple
    min_tuple = min(data, key=lambda x: x[1])
    return min_tuple[0]