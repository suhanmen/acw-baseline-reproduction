def re_arrange(arr, length):
    if not isinstance(arr, list) or length <= 0 or length > len(arr):
        raise ValueError("Invalid input. 'arr' must be a list, 'length' must be between 1 and the length of 'arr' inclusive.")

    # Split the array into negatives and positives
    negatives = [x for x in arr if x < 0]
    positives = [x for x in arr if x >= 0]

    # Sort each list
    negatives.sort()  # Sorts in ascending order, so negatives[0] is the largest (closest to zero)
    positives.sort(reverse=True)  # Sorts in descending order

    # Prepare the result list
    result = []
    i = j = 0
    while i < len(negatives) or j < len(positives):
        if i < len(negatives):
            result.append(negatives[i])
            i += 1
        if j < len(positives):
            result.append(positives[j])
            j += 1

    return result