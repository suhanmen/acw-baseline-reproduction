def Find_Min(sublists):
    # Validate the input
    if not isinstance(sublists, list) or not all(isinstance(sublist, list) for sublist in sublists):
        raise ValueError("Invalid input: sublists must be a list of lists")

    if not sublists:
        return []

    # Get the lengths of each sublist
    lengths = [len(sublist) for sublist in sublists]

    # Find the minimum length
    min_length = min(lengths)

    # Find the first sublist with min_length
    for sublist in sublists:
        if len(sublist) == min_length:
            return sublist

    # If no sublist found (shouldn't happen due to earlier checks)
    return []