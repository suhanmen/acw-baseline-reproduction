def list_split(lst, n):
    # Handle edge cases
    if not lst or n <= 0:
        return []

    num_sublists = n
    list_length = len(lst)

    # Calculate the size of each sublist
    sublist_size = list_length // num_sublists
    remainder = list_length % num_sublists

    # Initialize the sublists with empty lists
    sublists = [[] for _ in range(num_sublists)]

    # Distribute elements into sublists
    for i, element in enumerate(lst):
        # Determine which sublist the element belongs to
        sublist_index = i % num_sublists
        sublists[sublist_index].append(element)

    return sublists