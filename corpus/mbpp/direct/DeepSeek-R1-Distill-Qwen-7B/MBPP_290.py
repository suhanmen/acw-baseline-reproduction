def max_length(lst):
    # Find the maximum length among all sublists
    max_len = max(len(sublist) for sublist in lst)
    # Filter all sublists that have the maximum length
    max_sublists = [sublist for sublist in lst if len(sublist) == max_len]
    # Return the maximum length and the sublist(s) with that length
    return (max_len, max_sublists if len(max_sublists) > 1 else max_sublists[0])