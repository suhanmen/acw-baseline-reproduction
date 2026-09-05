def max_length_list(lst):
    # Handle empty input
    if not lst:
        return (0, None)

    # Determine the maximum length of the sublists
    max_len = max(len(sublist) for sublist in lst)

    # Filter all sublists with the maximum length
    max_lists = [sublist for sublist in lst if len(sublist) == max_len]

    # If only one sublist has max length, return it
    if len(max_lists) == 1:
        return (max_len, max_lists[0])

    # If multiple sublists have max length, sort them
    max_lists.sort()

    # Return the max length and the first sublist after sorting
    return (max_len, max_lists[0])