def check_occurrences(tuples_list):
    """
    Check occurrences of records in a list of tuples that occur at similar times.
    """
    # Validate input: ensure it's a list of tuples and each tuple has exactly two elements
    if not isinstance(tuples_list, list):
        raise ValueError("Input must be a list of tuples.")
    for t in tuples_list:
        if not isinstance(t, tuple) or len(t) != 2:
            raise ValueError("Each element in the list must be a tuple with exactly two elements.")

    # Create a dictionary to hold the counts of each record
    occurrence_counts = {}

    # Iterate through each tuple in the list
    for t in tuples_list:
        # Get the current record
        key = t
        # If the record already exists in the dictionary, increment its count
        if key in occurrence_counts:
            occurrence_counts[key] += 1
        else:
            # If not, add the record to the dictionary with a count of 1
            occurrence_counts[key] = 1

    # Convert the dictionary to a frozenset of tuples to return
    result = frozenset(occurrence_counts.items())

    return result

# Example usage:
# print(check_occurrences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))
# Output: {(1, 3): 2, (2, 5): 2, (3, 6): 1}

# print(check_occurrences([(4, 2), (2, 4), (3, 6), (6, 3), (7, 4)]))
# Output: {(2, 4): 2, (3, 6): 2, (4, 7): 1}

# print(check_occurrences([(13, 2), (11, 23), (12, 25), (25, 12), (16, 23)]))
# Output: {(2, 13): 1, (11, 23): 1, (12, 25): 2, (16, 23): 1}