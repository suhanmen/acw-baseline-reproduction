def freq_count(lst):
    # Handle the case of an empty list
    if not lst:
        return {}

    # Initialize a dictionary to store frequencies
    frequencies = {}

    # Iterate over each element in the list
    for element in lst:
        # If the element is already a key, increment its count
        if element in frequencies:
            frequencies[element] += 1
        else:
            # Otherwise, add the element to the dictionary with a count of 1
            frequencies[element] = 1

    # Return the dictionary of frequencies
    return frequencies