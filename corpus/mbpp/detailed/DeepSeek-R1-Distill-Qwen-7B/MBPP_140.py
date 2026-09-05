def extract_singly(tuples_list):
    # Flatten the list of tuples into a single list of elements
    flattened = [element for tup in tuples_list for element in tup]

    # Count occurrences of each element
    counts = {}
    for element in flattened:
        counts[element] = counts.get(element, 0) + 1

    # Extract elements that occur exactly once
    result = [element for element in counts if counts[element] == 1]

    # Return the sorted result as per the examples
    return sorted(result)