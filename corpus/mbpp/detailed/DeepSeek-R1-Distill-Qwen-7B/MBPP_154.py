def specified_element(matrix, k):
    # Input validation
    if not isinstance(matrix, list) or not all(isinstance(sublist, list) for sublist in matrix):
        return []
    if not isinstance(k, int):
        return []

    result = []

    # Iterate through each row in the matrix
    for row in matrix:
        # Check if the row has enough elements
        if len(row) > k:
            # Append the element at index k to the result list
            result.append(row[k])

    return result