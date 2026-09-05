def remove_matching_tuple(tup1, tup2):
    # Validate inputs
    if not isinstance(tup1, tuple) or not isinstance(tup2, tuple):
        raise TypeError("Both inputs must be tuples.")

    # Handle empty cases
    if not tup1:
        return ()
    if not tup2:
        return tup1

    # Create a list to hold the result
    result = []

    # Iterate over each tuple in tup1
    for item in tup1:
        # Check if the item is not in tup2
        if item not in tup2:
            result.append(item)

    # Return the filtered list as a tuple
    return tuple(result)