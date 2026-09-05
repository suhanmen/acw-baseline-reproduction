def assign_freq(tuple_list):
    """
    Assigns the frequency of each unique tuple to itself in the order they first appear.
    """
    counts = {}
    for t in tuple_list:
        counts[t] = counts.get(t, 0) + 1

    result = []
    seen = set()
    for t in tuple_list:
        if t not in seen:
            # Create a new tuple containing the original elements plus the frequency
            result.append(t + (counts[t],))
            seen.add(t)

    return str(result)