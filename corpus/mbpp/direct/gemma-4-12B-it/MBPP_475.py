def sort_counter(counter: dict) -> list:
    """
    Sorts the items of a dictionary (counter) by their values in descending order.
    Returns a list of tuples.
    """
    # Convert dict items to a list and sort by the second element of the tuple (the value)
    # reverse=True ensures descending order
    return sorted(counter.items(), key=lambda item: item[1], reverse=True)