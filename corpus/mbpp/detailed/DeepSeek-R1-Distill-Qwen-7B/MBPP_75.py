def find_tuples(tuples_list, k):
    # Input validation
    if not tuples_list:
        return '[]'
    if k == 0:
        return '[]'

    # Check if all elements in the tuples are integers
    for t in tuples_list:
        if not isinstance(t, tuple) or any(not isinstance(x, int) for x in t):
            return '[]'

    valid_tuples = []
    for t in tuples_list:
        # Check if all elements are divisible by k
        all_divisible = True
        for x in t:
            if x % k != 0:
                all_divisible = False
                break
        if all_divisible:
            valid_tuples.append(t)

    # Convert the list of tuples to a string in the specified format
    result = ']['.join(map(str, valid_tuples)) + ']'
    return result