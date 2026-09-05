def modified_encode(input):
    if not input:
        return []
    result = []
    current = input[0]
    count = 1
    for elem in input[1:]:
        if elem == current:
            count += 1
        else:
            if count == 1:
                result.append([current])
            else:
                result.append([count, current])
            current = elem
            count = 1
    # Append the last element(s)
    if count == 1:
        result.append([current])
    else:
        result.append([count, current])
    # Handle cases where the last group should be a list
    if not isinstance(input, str):
        # If input was a list, the last element is a list only if count > 1
        # If input was a string, always append the count as a list
        return result
    else:
        # For strings, the last element must be a list
        if len(result) == 0:
            return []
        if isinstance(result[-1], list) and len(result[-1]) == 1:
            # Convert the single-element list to the actual element
            result[-1] = result[-1][0]
        return result