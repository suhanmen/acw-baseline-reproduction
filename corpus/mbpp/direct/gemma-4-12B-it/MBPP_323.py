def re_arrange(arr, n):
    positives = []
    negatives = []

    for x in arr:
        if x >= 0:
            positives.append(x)
        else:
            negatives.append(x)

    result = []
    i = 0
    j = 0

    # The requirements show a specific logic: 
    # The first element is usually negative if available, 
    # followed by positive, then negative, etc.
    # If one list is exhausted, append the rest.

    # Looking at the test cases:
    # Case 1: [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8] -> [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]
    # Negatives: [-5, -2, -8], Positives: [5, 2, 4, 7, 1, 8, 0]
    # Sequence: Neg[0], Pos[0], Neg[1], Pos[1], Neg[2], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6]

    # Case 2: [1, 2, 3, -4, -1, 4] -> [-4, 1, -1, 2, 3, 4]
    # Negatives: [-4, -1], Positives: [1, 2, 3, 4]
    # Sequence: Neg[0], Pos[0], Neg[1], Pos[1], Pos[2], Pos[3]

    # Case 3: [4, 7, 9, 77, -4, 5, -3, -9] -> [-4, 4, -3, 7, -9, 9, 77, 5]
    # Negatives: [-4, -3, -9], Positives: [4, 7, 9, 77, 5]
    # Sequence: Neg[0], Pos[0], Neg[1], Pos[1], Neg[2], Pos[2], Pos[3], Pos[4]

    while i < len(negatives) and j < len(positives):
        result.append(negatives[i])
        result.append(positives[j])
        i += 1
        j += 1

    if i < len(negatives):
        result.extend(negatives[i:])
    if j < len(positives):
        result.extend(positives[j:])

    return result