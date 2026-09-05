def sort_mixed_list(lst):
    # Separate the list into integers and strings
    numbers = []
    strings = []
    for item in lst:
        if isinstance(item, int):
            numbers.append(item)
        else:
            strings.append(item)

    # Sort the numbers and strings individually
    numbers_sorted = sorted(numbers)
    strings_sorted = sorted(strings)

    # Combine the sorted numbers and strings while maintaining their types
    sorted_list = []
    i = 0  # Index for numbers_sorted
    j = 0  # Index for strings_sorted

    while i < len(numbers_sorted) and j < len(strings_sorted):
        if isinstance(numbers_sorted[i], int) and isinstance(strings_sorted[j], str):
            # Mix-sort: alternate placing int and string
            sorted_list.append(numbers_sorted[i])
            i += 1
        elif isinstance(numbers_sorted[i], int):
            sorted_list.append(numbers_sorted[i])
            i += 1
        else:
            sorted_list.append(strings_sorted[j])
            j += 1

    # Add any remaining elements
    while i < len(numbers_sorted):
        sorted_list.append(numbers_sorted[i])
        i += 1
    while j < len(strings_sorted):
        sorted_list.append(strings_sorted[j])
        j += 1

    return sorted_list