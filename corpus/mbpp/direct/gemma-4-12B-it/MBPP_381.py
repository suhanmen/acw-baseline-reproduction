def index_on_inner_list(data, index):
    """
    Sorts a list of lists (or tuples) by a specific index of the inner elements.

    Args:
        data (list): A list of sequences (e.g., tuples or lists).
        index (int): The index within the inner sequences to sort by.

    Returns:
        list: The sorted list.
    """
    return sorted(data, key=lambda x: x[index])