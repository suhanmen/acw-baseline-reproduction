def min_length_list(lists):
    # Validate input: ensure that the input is a list of lists
    if not isinstance(lists, list):
        raise ValueError("Invalid input: the first argument must be a list of lists.")
    for sub in lists:
        if not isinstance(sub, list):
            raise ValueError("Invalid input: each element must be a list.")

    # Handle empty input
    if not lists:
        raise ValueError("Invalid input: the list of lists cannot be empty.")

    # Check if all sublists have the same length
    lengths = [len(sub) for sub in lists]
    if all(l == lengths[0] for l in lengths):
        return (lengths[0], lists[0])

    # Find the sublist with the minimum length
    min_len = min(lengths)
    min_indices = [i for i, l in enumerate(lengths) if l == min_len]

    # Return the shortest sublist; choose the first one if multiple
    return (min_len, lists[min_indices[0]])