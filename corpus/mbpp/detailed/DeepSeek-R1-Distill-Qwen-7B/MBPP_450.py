def extract_string(string_list, size):
    # Input validation
    if not string_list or size <= 0:
        return []

    # Determine the number of elements to take
    sublist_length = min(size, len(string_list))

    # Extract the last 'sublist_length' elements
    extracted = string_list[-sublist_length:]

    return extracted