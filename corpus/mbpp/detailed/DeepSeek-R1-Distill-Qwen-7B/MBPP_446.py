def count_Occurrence(elements_tuple, filter_list):
    # Step 1: Check if inputs are valid
    # Convert tuple to list to handle both mutable and immutable types
    elements = list(elements_tuple)
    # Check if all items in filter_list are hashable
    for item in filter_list:
        if not isinstance(item, hashable):
            return -1

    # Step 2: Count occurrences of each element in the tuple
    element_counts = {}
    for item in elements:
        if item in element_counts:
            element_counts[item] += 1
        else:
            element_counts[item] = 1

    # Step 3: Sum the occurrences of each item in filter_list
    total = 0
    for item in filter_list:
        total += element_counts.get(item, 0)

    # Step 4: Return the total count
    return total