def rear_extract(records):
    """
    Performs the rear element extraction from a list of tuples records.
    Returns a list of the last elements from each tuple.
    """
    return [record[-1] for record in records]