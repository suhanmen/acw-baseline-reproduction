def first_element(arr, k, find):
    # Validate inputs
    if not isinstance(arr, list) or not isinstance(k, int) or not isinstance(find, int):
        raise ValueError("Invalid input types")
    if k < 0:
        raise ValueError("k must be a non-negative integer")
    if not arr:
        raise ValueError("Array is empty")

    # Count occurrences of each element
    element_counts = {}
    for element in arr:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    # Scan the array to find the first element with exactly k occurrences
    for element in arr:
        if element_counts[element] == k:
            return element
    # If no element found with exact count
    return None