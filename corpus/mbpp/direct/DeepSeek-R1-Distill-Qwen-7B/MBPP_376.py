def remove_replica(t):
    # Create a dictionary to track occurrences of each element
    element_count = {}
    for element in t:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    # Prepare a list to build the result
    result = []
    # Track which elements have been added to the result list
    added_elements = set()
    # Iterate through each element in the input tuple
    for element in t:
        # If the element is a number and hasn't been added yet
        if isinstance(element, int) and element not in added_elements:
            result.append(element)
            added_elements.add(element)
        else:
            # Append 'MSP' instead of the duplicate elements
            result.append('MSP')
    # Convert the result list back to a tuple
    return tuple(result)

# Test cases
print(remove_replica((1, 1, 4, 4, 4, 5, 5, 6, 7, 7)))
print(remove_replica((2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9)))
print(remove_replica((2, 2, 5, 4, 5, 7, 5, 6, 7, 7)))