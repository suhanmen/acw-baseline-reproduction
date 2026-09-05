def assign_freq(tuples_list):
    from collections import defaultdict

    # Validate input: check if tuples_list is a list and each element is a tuple
    if not isinstance(tuples_list, list):
        raise ValueError("Input must be a list of tuples.")
    for t in tuples_list:
        if not isinstance(t, tuple) or len(t) < 1:
            raise ValueError("Each element in the list must be a non-empty tuple.")

    # Count the frequency of each tuple
    tuple_counts = defaultdict(int)
    for t in tuples_list:
        tuple_counts[t] += 1

    # Create a list of tuples, each appended with their frequency
    result = []
    for t in tuples_list:
        # Use the count from the dictionary, defaulting to 1 if the tuple doesn't appear again
        freq = tuple_counts[t] if t in tuple_counts else 1
        result.append(list(t) + [freq])

    # Return the result as a string in the required format
    return '[' + ', '.join(str(list(t) + [freq]) for t in set(tuples_list)) + ']'

# Test cases
print(assign_freq([(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]))
print(assign_freq([(4, 2, 4), (7, 1), (4, 8), (4, 2, 4), (9, 2), (7, 1)]))
print(assign_freq([(11, 13, 10), (17, 21), (4, 2, 3), (17, 21), (9, 2), (4, 2, 3)]))